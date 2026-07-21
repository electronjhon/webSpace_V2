"""
Space AI 2.0

Learning Engine

Strategy Optimizer

Responsable de calcular estadísticas que permitirán
optimizar futuras estrategias de decisión.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from collections import Counter

from ia.learning_engine.enums import FeedbackOutcome
from ia.learning_engine.history.result_history import (
    ResultHistory,
)
from ia.learning_engine.metrics.strategy_metrics import (
    StrategyMetrics,
)


class StrategyOptimizer:
    """
    Calcula información útil para optimizar estrategias.
    """

    @staticmethod
    def optimize(
        history: ResultHistory,
    ) -> Counter[FeedbackOutcome]:
        """
        Devuelve la distribución de resultados obtenidos.
        """

        return StrategyMetrics.outcome_distribution(
            history,
        )


__all__ = [
    "StrategyOptimizer",
]
