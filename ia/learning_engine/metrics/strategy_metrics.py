"""
Space AI 2.0

Learning Engine

Strategy Metrics

Calcula métricas de desempeño para futuras estrategias
de aprendizaje.

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


class StrategyMetrics:
    """
    Métricas descriptivas del historial de aprendizaje.
    """

    @staticmethod
    def outcome_distribution(
        history: ResultHistory,
    ) -> Counter[FeedbackOutcome]:
        """
        Devuelve la distribución de resultados.
        """

        return Counter(record.feedback.outcome for record in history)


__all__ = [
    "StrategyMetrics",
]
