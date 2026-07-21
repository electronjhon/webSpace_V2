"""
Space AI 2.0

Learning Engine

Confidence Metrics

Calcula estadísticas relacionadas con la confianza
de las señales generadas por el sistema.

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


class ConfidenceMetrics:
    """
    Métricas relacionadas con la confianza del sistema.
    """

    @staticmethod
    def average_confidence(
        history: ResultHistory,
    ) -> LearningScore:
        """
        Calcula la confianza promedio observada.
        """

        if history.is_empty:
            return LearningScore.of(Decimal("0.0"))

        total = sum(
            (record.feedback.signal.confidence.value for record in history),
            start=Decimal("0.0"),
        )

        average = total / Decimal(history.size)

        return LearningScore.of(average)


__all__ = [
    "ConfidenceMetrics",
]
