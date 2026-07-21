"""
Space AI 2.0

Dashboard - Statistics Model

Representa las estadísticas agregadas del Dashboard.

Este modelo resume el estado de la última ejecución del
pipeline de inteligencia artificial utilizando únicamente
información obtenida desde las interfaces públicas de los
motores.

No contiene lógica de negocio ni realiza cálculos.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DashboardStatistics:
    """
    Estadísticas agregadas del Dashboard.
    """

    signal_accepted: bool

    has_learning_history: bool

    @property
    def is_complete(self) -> bool:
        """
        Indica si existe una señal aceptada y el sistema
        dispone de historial de aprendizaje.
        """

        return self.signal_accepted and self.has_learning_history


__all__ = [
    "DashboardStatistics",
]
