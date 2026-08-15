"""
Space AI 2.0

Learning Engine

Facade principal del Learning Engine.

Coordina el procesamiento del feedback, la persistencia
del aprendizaje y la evaluación independiente de
predicciones.

Sprint:
    15

Versión:
    1.2.0
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.enums import FeedbackOutcome
from ia.learning_engine.feedback.feedback_processor import (
    FeedbackProcessor,
)
from ia.learning_engine.feedback.feedback_rules import (
    FeedbackRules,
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
from ia.learning_engine.learning_statistics import (
    LearningStatistics,
)
from ia.learning_engine.metrics.confidence_metrics import (
    ConfidenceMetrics,
)
from ia.learning_engine.metrics.learning_statistics_builder import (
    LearningStatisticsBuilder,
)
from ia.learning_engine.metrics.performance_metrics import (
    PerformanceMetrics,
)
from ia.learning_engine.metrics.prediction_metrics import (
    PredictionMetrics,
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

    Mantiene dos caminos de aprendizaje independientes:

    1. Evaluación de señales mediante Feedback y LearningRecord.
    2. Evaluación directa del rendimiento predictivo mediante
       PredictionMetrics.

    El segundo camino permite evaluar una predicción aunque
    no exista una señal aceptada.
    """

    repository: LearningRepository

    prediction_metrics: PredictionMetrics = field(
        default_factory=PredictionMetrics,
    )

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
        Evalúa una señal y devuelve una nueva instancia
        del Learning Engine junto con el Feedback generado.

        Este flujo conserva el comportamiento original del
        Learning Engine para señales.
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
                prediction_metrics=self.prediction_metrics,
            ),
            feedback,
        )

    def evaluate_prediction(
        self,
        *,
        prediction: Prediction,
        classification: ClassificationResult,
        observed_outcome: ObservedOutcome,
        learning_score: LearningScore,
    ) -> tuple[LearningEngine, FeedbackOutcome]:
        """
        Evalúa directamente una predicción frente al estado
        observado posteriormente.

        Este flujo no requiere una Signal y, por tanto,
        permite que el Predictor sea evaluado aunque el
        Decision Engine no produzca una señal aceptada.
        """

        del classification
        del observed_outcome

        outcome = FeedbackRules.classify(
            learning_score,
        )

        metrics_outcome = {
            FeedbackOutcome.SUCCESS: "CORRECT",
            FeedbackOutcome.PARTIAL_SUCCESS: "PARTIAL",
            FeedbackOutcome.FAILURE: "INCORRECT",
        }[outcome]

        updated_metrics = self.prediction_metrics.add(
            outcome=metrics_outcome,
            score=learning_score.value,
        )

        return (
            LearningEngine(
                repository=self.repository,
                prediction_metrics=updated_metrics,
            ),
            outcome,
        )

    @property
    def history(self) -> ResultHistory:
        """
        Historial completo de aprendizaje de señales.
        """

        return self.repository.history

    @property
    def average_score(self) -> LearningScore:
        """
        LearningScore promedio del historial de señales.
        """

        return PerformanceMetrics.average_score(
            self.history,
        )

    @property
    def average_confidence(self) -> LearningScore:
        """
        Confianza promedio del historial de señales.
        """

        return ConfidenceMetrics.average_confidence(
            self.history,
        )

    @property
    def statistics(self) -> LearningStatistics:
        """
        Devuelve un snapshot del estado actual del
        proceso de aprendizaje de señales.
        """

        return LearningStatisticsBuilder.build(
            self.history,
        )

    @property
    def strategy_distribution(
        self,
    ) -> Counter[FeedbackOutcome]:
        """
        Distribución de resultados del historial de señales.
        """

        return StrategyOptimizer.optimize(
            self.history,
        )

    @property
    def prediction_metrics_summary(self) -> str:
        """
        Devuelve un resumen textual de las métricas
        acumuladas del Predictor.

        Esta propiedad no escribe en consola. Su objetivo es
        proporcionar al nivel de aplicación una representación
        lista para mostrar en terminal o dashboard.
        """

        metrics = self.prediction_metrics

        return (
            "========== PREDICTION METRICS ==========\n"
            f"Evaluated : {metrics.total}\n"
            f"Success   : {metrics.correct}\n"
            f"Partial   : {metrics.partial}\n"
            f"Failure   : {metrics.incorrect}\n"
            f"Accuracy  : {metrics.accuracy:.2%}\n"
            f"Avg score : {metrics.average_score:.4f}\n"
            "========================================="
        )


__all__ = [
    "LearningEngine",
]
