"""
Space AI 2.0

Learning Engine

Confidence Updater

Componente encargado de recalcular métricas relacionadas
con la confianza del sistema.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.history.result_history import (
    ResultHistory,
)
from ia.learning_engine.metrics.confidence_metrics import (
    ConfidenceMetrics,
)


class ConfidenceUpdater:
    """
    Actualiza la confianza global del sistema.
    """

    @staticmethod
    def update(
        history: ResultHistory,
    ) -> LearningScore:
        """
        Calcula la confianza promedio observada.
        """

        return ConfidenceMetrics.average_confidence(
            history,
        )


__all__ = [
    "ConfidenceUpdater",
]
