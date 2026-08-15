"""
Space AI 2.0

Learning Engine

Learning Statistics Builder

Construye un snapshot de LearningStatistics utilizando
los distintos servicios especializados del módulo
metrics.

Sprint:
    15

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.learning_engine.history.result_history import (
    ResultHistory,
)
from ia.learning_engine.learning_statistics import (
    LearningStatistics,
)
from ia.learning_engine.metrics.confidence_metrics import (
    ConfidenceMetrics,
)
from ia.learning_engine.metrics.performance_metrics import (
    PerformanceMetrics,
)
from ia.learning_engine.metrics.strategy_metrics import (
    StrategyMetrics,
)


class LearningStatisticsBuilder:
    """
    Construye un snapshot inmutable de LearningStatistics
    a partir del historial del Learning Engine.
    """

    @staticmethod
    def build(
        history: ResultHistory,
    ) -> LearningStatistics:
        """
        Construye un resumen agregado del estado actual
        del proceso de aprendizaje.
        """

        return LearningStatistics(
            average_score=PerformanceMetrics.average_score(
                history,
            ),
            average_confidence=ConfidenceMetrics.average_confidence(
                history,
            ),
            success_rate=PerformanceMetrics.success_rate(
                history,
            ),
            outcome_distribution=StrategyMetrics.outcome_distribution(
                history,
            ),
        )


__all__ = [
    "LearningStatisticsBuilder",
]
