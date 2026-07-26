"""
Space AI 2.0

AI Pipeline

Coordinates the complete AI processing pipeline.

This component represents the boundary between the
integration layer and the AI core.

It orchestrates every engine while remaining free of
business rules.

Author: Space AI 2.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from core.types import Number
from core.windows import RollingWindow
from feature_engine.feature_engine import FeatureEngine
from ia.decision_engine.decision_context import DecisionContext
from ia.decision_engine.decision_engine import DecisionEngine
from ia.learning_engine.learning_engine import LearningEngine
from ia.signal_engine.configuration import SignalConfiguration
from ia.signal_engine.context import SignalContext
from ia.signal_engine.signal_engine import SignalEngine
from predictor.predictor_engine import PredictorEngine
from predictor.strategies.strategy_type import StrategyType
from state_engine.models.state_engine_result import (
    StateEngineResult,
)
from state_engine.state_engine import StateEngine
from state_engine.state_history import StateHistory


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

        #
        # Feature extraction
        #

        feature_vector = FeatureEngine.extract(
            window,
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
        # Decision
        #

        decision_result = self.decision_engine.decide(
            DecisionContext(
                prediction=prediction_result.prediction,
            ),
        )

        #
        # Signal
        #

        self.signal_engine.generate(
            SignalContext(
                decision=decision_result,
                configuration=SignalConfiguration(),
                timestamp=datetime.now(UTC),
            ),
        )

        #
        # Remaining stages will be connected
        # progressively while preserving the
        # architecture of each engine.
        #
