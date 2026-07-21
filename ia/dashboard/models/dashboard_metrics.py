"""
Space AI 2.0

Dashboard - Metrics Model

Define el Value Object que representa las métricas
consolidadas del Dashboard.

Este modelo encapsula los principales indicadores de
rendimiento obtenidos del Learning Engine y expuestos
por el Dashboard.

No contiene lógica de negocio ni realiza cálculos.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from ia.core.value_objects.learning_score import LearningScore


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DashboardMetrics:
    """
    Métricas consolidadas del Dashboard.

    Representa los indicadores globales de rendimiento
    calculados por el Learning Engine.
    """

    average_learning_score: LearningScore

    average_confidence: LearningScore

    @property
    def has_learning_data(self) -> bool:
        """
        Indica si existen métricas de aprendizaje
        distintas de cero.
        """

        return (
            not self.average_learning_score.is_zero
            or not self.average_confidence.is_zero
        )


__all__ = [
    "DashboardMetrics",
]
