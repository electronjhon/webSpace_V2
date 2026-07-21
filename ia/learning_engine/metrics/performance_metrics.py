"""
Space AI 2.0

Learning Engine

Performance Metrics

Calcula métricas globales de desempeño a partir del
historial de aprendizaje.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from decimal import Decimal

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.history.result_history import (
    ResultHistory,
)


class PerformanceMetrics:
    """
    Calcula métricas globales del Learning Engine.
    """

    @staticmethod
    def average_score(
        history: ResultHistory,
    ) -> LearningScore:
        """
        Calcula el LearningScore promedio del historial.
        """

        if history.is_empty:
            return LearningScore.of(Decimal("0.0"))

        total = sum(
            (record.feedback.learning_score.value for record in history),
            start=Decimal("0.0"),
        )

        average = total / Decimal(history.size)

        return LearningScore.of(average)

    @staticmethod
    def success_rate(
        history: ResultHistory,
    ) -> Decimal:
        """
        Calcula la tasa de éxito del historial.
        """

        if history.is_empty:
            return Decimal("0.0")

        successes = sum(
            1 for record in history if record.feedback.outcome.value == "success"
        )

        return Decimal(successes) / Decimal(history.size)


__all__ = [
    "PerformanceMetrics",
]
