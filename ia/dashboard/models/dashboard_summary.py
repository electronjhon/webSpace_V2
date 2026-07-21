"""
Space AI 2.0

Dashboard - Summary Model

Representa el resumen general del Dashboard.

Este modelo encapsula el estado global del Dashboard y el
estado operativo de cada uno de los motores que participan
en el pipeline de inteligencia artificial.

No contiene lógica de negocio ni realiza cálculos.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from ia.dashboard.enums import (
    DashboardStatus,
    EngineStatus,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DashboardSummary:
    """
    Resumen general del Dashboard.

    Contiene el estado consolidado del sistema y el estado
    operativo de cada uno de los motores de IA.
    """

    dashboard_status: DashboardStatus

    predictor_status: EngineStatus

    state_engine_status: EngineStatus

    decision_engine_status: EngineStatus

    signal_engine_status: EngineStatus

    learning_engine_status: EngineStatus

    @property
    def is_operational(self) -> bool:
        """
        Indica si todos los motores se encuentran disponibles.
        """

        return (
            self.dashboard_status is DashboardStatus.READY
            and self.predictor_status is EngineStatus.AVAILABLE
            and self.state_engine_status is EngineStatus.AVAILABLE
            and self.decision_engine_status is EngineStatus.AVAILABLE
            and self.signal_engine_status is EngineStatus.AVAILABLE
            and self.learning_engine_status is EngineStatus.AVAILABLE
        )


__all__ = [
    "DashboardSummary",
]
