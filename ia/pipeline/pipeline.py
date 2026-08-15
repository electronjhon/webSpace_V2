"""
Space AI 2.0

AI Pipeline

Coordinates the complete AI processing pipeline.

This component represents the boundary between the
integration layer and the AI core.

It orchestrates every engine while remaining free of
business rules.

Author: Space AI 2.0

Sprint:
    15
Version:
    1.2.0
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime

from core.logging.logger import Logger
from core.types import Number
from core.windows import RollingWindow
from feature_engine.feature_engine import FeatureEngine
from ia.decision_engine.decision_context import DecisionContext
from ia.decision_engine.decision_engine import DecisionEngine
from ia.learning_engine.learning_engine import LearningEngine
from ia.learning_engine.models.learning_evaluation_context import (
    LearningEvaluationContext,
)
from ia.learning_engine.models.observed_outcome import (
    ObservedOutcome,
)
from ia.learning_engine.scoring.learning_score_calculator import (
    LearningScoreCalculator,
)
from ia.signal_engine.configuration import SignalConfiguration
from ia.signal_engine.context import SignalContext
from ia.signal_engine.signal_engine import SignalEngine
from predictor.prediction_status import PredictionStatus
from predictor.predictor_engine import PredictorEngine
from predictor.strategies.strategy_type import StrategyType
from state_engine.models.state_engine_result import (
    StateEngineResult,
)
from state_engine.state_engine import StateEngine
from state_engine.state_history import StateHistory

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class AIPipeline:
    """
    Coordinates the AI engines.

    The pipeline is responsible only for orchestrating
    the execution flow between engines.

    No business logic belongs here.
    """

    state_engine: StateEngine

    predictor_engine: PredictorEngine

    decision_engine: DecisionEngine

    signal_engine: SignalEngine

    learning_engine: LearningEngine

    prediction_strategy: StrategyType = StrategyType.MARKOV

    _history: StateHistory = field(
        default_factory=StateHistory,
        init=False,
        repr=False,
    )

    _pending_learning: LearningEvaluationContext | None = field(
        default=None,
        init=False,
        repr=False,
    )

    _round_count: int = field(
        default=0,
        init=False,
        repr=False,
    )

    def process(
        self,
        window: RollingWindow[Number],
    ) -> None:
        """
        Execute one AI pipeline iteration.

        Parameters
        ----------
        window:
            Rolling window produced by the integration
            layer.
        """

        self._round_count += 1

        Logger.info(
            f"[Pipeline Round {self._round_count}]",
        )

        logger.debug(
            "[Pipeline] Received window: capacity=%d, size=%d, values=%s",
            window.capacity,
            len(window),
            window.to_tuple(),
        )

        #
        # Feature extraction
        #

        feature_vector = FeatureEngine.extract(
            window,
        )

        logger.debug(
            "[Feature] Extracted features: window_size=%d, statistics=%s, "
            "trend=%s, pattern=%s, quality=%s, transition=%s",
            feature_vector.window_size,
            feature_vector.statistics,
            feature_vector.trend,
            feature_vector.pattern,
            feature_vector.quality,
            feature_vector.transition,
        )

        #
        # State processing
        #

        state_result: StateEngineResult = self.state_engine.process(
            history=self._history,
            features=feature_vector,
        )

        #
        # Persist the updated immutable history.
        #

        self._history = state_result.history

        Logger.info_block(
            "STATE HISTORY",
            (
                f"States      : {len(self._history.states)}\n"
                f"Transitions : {len(self._history.transitions)}"
            ),
        )

        logger.debug(
            "[State] Generated classification: labels=%s, confidence=%s, "
            "states=%d, transitions=%d",
            state_result.classification.labels,
            state_result.classification.confidence,
            len(self._history.states),
            len(self._history.transitions),
        )

        #
        # Prediction evaluation
        #
        # The current classification represents the observed state
        # against which the previous prediction is evaluated.
        #
        # This evaluation is independent from Decision and Signal.
        #

        if self._pending_learning is not None:
            observed_outcome = ObservedOutcome(
                labels=state_result.classification.labels,
            )

            learning_score = LearningScoreCalculator.calculate(
                prediction=self._pending_learning.prediction,
                observed_outcome=observed_outcome,
            )

            self.learning_engine, outcome = self.learning_engine.evaluate_prediction(
                prediction=self._pending_learning.prediction,
                classification=self._pending_learning.classification,
                observed_outcome=observed_outcome,
                learning_score=learning_score,
            )

            Logger.info(
                "[Learning] Prediction evaluation completed: "
                f"score={learning_score.value}, "
                f"outcome={outcome.value}",
            )

            #
            # Show accumulated prediction metrics every
            # 10 completed evaluations.
            #

            evaluated = self.learning_engine.prediction_metrics.total

            if evaluated > 0 and evaluated % 10 == 0:
                Logger.info(
                    self.learning_engine.prediction_metrics_summary,
                )

            self._pending_learning = None

        #
        # Prediction
        #

        prediction_result = self.predictor_engine.predict(
            strategy_type=self.prediction_strategy,
            feature_vector=feature_vector,
            classification=state_result.classification,
            history=self._history,
        )

        #
        # Predictor warm-up.
        #

        if prediction_result.status is not PredictionStatus.READY:
            logger.info(
                "[Prediction] %s",
                prediction_result.reason,
            )

            Logger.info(
                f"[Prediction] {prediction_result.reason}",
            )

            return

        assert prediction_result.prediction is not None

        logger.debug(
            "[Prediction] Generated prediction: strategy=%s, labels=%s, "
            "probability=%s, confidence=%s",
            self.prediction_strategy,
            prediction_result.prediction.labels,
            prediction_result.prediction.probability,
            prediction_result.prediction.confidence,
        )

        #
        # Store the prediction immediately.
        #
        # Learning no longer depends on Signal acceptance.
        #

        self._pending_learning = LearningEvaluationContext(
            classification=state_result.classification,
            prediction=prediction_result.prediction,
        )

        Logger.info(
            "[Learning] Pending prediction stored",
        )

        #
        # Decision
        #

        decision_result = self.decision_engine.decide(
            DecisionContext(
                prediction=prediction_result.prediction,
            ),
        )

        logger.debug(
            "[Decision] Generated decision: action=%s, confidence=%s, reason=%s",
            decision_result.action,
            decision_result.confidence,
            decision_result.reason,
        )

        #
        # Signal
        #

        signal_result = self.signal_engine.generate(
            SignalContext(
                decision=decision_result,
                configuration=SignalConfiguration(),
                timestamp=datetime.now(UTC),
            ),
        )

        logger.debug(
            "[Signal] Generated signal result: accepted=%s, reason=%s, signal=%s",
            signal_result.accepted,
            signal_result.reason,
            signal_result.signal,
        )

        #
        # Diagnostic information for the learning integration.
        #

        Logger.info(
            "[Signal] "
            f"accepted={signal_result.accepted}, "
            f"reason={signal_result.reason}, "
            f"signal={signal_result.signal}",
        )

        #
        # Signal-based learning remains available independently.
        #
        # At this stage the predictive-learning context is already
        # stored above. A rejected signal therefore does not prevent
        # prediction evaluation.
        #
