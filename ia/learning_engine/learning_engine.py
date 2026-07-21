"""
Space AI 2.0

Learning Engine

Facade principal del Learning Engine.

Coordina el procesamiento del feedback, la persistencia
del aprendizaje y el cálculo de métricas del sistema.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.enums import FeedbackOutcome
from ia.learning_engine.feedback.feedback_processor import (
    FeedbackProcessor,
)
from ia.learning_engine.history.result_history import (
    ResultHistory,
)
from ia.learning_engine.learner.incremental_learner import (
    IncrementalLearner,
)
from ia.learning_engine.learner.strategy_optimizer import (
    StrategyOptimizer,
)
from ia.learning_engine.metrics.confidence_metrics import (
    ConfidenceMetrics,
)
from ia.learning_engine.metrics.performance_metrics import (
    PerformanceMetrics,
)
from ia.learning_engine.models.feedback import Feedback
from ia.learning_engine.models.learning_record import (
    LearningRecord,
)
from ia.learning_engine.models.observed_outcome import (
    ObservedOutcome,
)
from ia.learning_engine.repository.learning_repository import (
    LearningRepository,
)
from ia.signal_engine.value_objects.signal import Signal
from predictor.prediction import Prediction
from state_engine.models.classification_result import (
    ClassificationResult,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningEngine:
    """
    Facade principal del Learning Engine.
    """

    repository: LearningRepository

    def evaluate(
        self,
        *,
        prediction: Prediction,
        classification: ClassificationResult,
        signal: Signal,
        observed_outcome: ObservedOutcome,
        learning_score: LearningScore,
    ) -> tuple[LearningEngine, Feedback]:
        """
        Evalúa un resultado y devuelve una nueva instancia
        del Learning Engine junto con el Feedback generado.
        """

        feedback = FeedbackProcessor.create(
            signal=signal,
            observed_outcome=observed_outcome,
            learning_score=learning_score,
        )

        record = LearningRecord(
            prediction=prediction,
            classification=classification,
            feedback=feedback,
        )

        repository = IncrementalLearner.learn(
            repository=self.repository,
            record=record,
        )

        return (
            LearningEngine(
                repository=repository,
            ),
            feedback,
        )

    @property
    def history(self) -> ResultHistory:
        """
        Historial completo de aprendizaje.
        """

        return self.repository.history

    @property
    def average_score(self) -> LearningScore:
        """
        LearningScore promedio del historial.
        """

        return PerformanceMetrics.average_score(
            self.history,
        )

    @property
    def average_confidence(self) -> LearningScore:
        """
        Confianza promedio del historial.
        """

        return ConfidenceMetrics.average_confidence(
            self.history,
        )

    @property
    def strategy_distribution(
        self,
    ) -> Counter[FeedbackOutcome]:
        """
        Distribución de resultados del historial.
        """

        return StrategyOptimizer.optimize(
            self.history,
        )


__all__ = [
    "LearningEngine",
]
