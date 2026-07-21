"""
Space AI 2.0

Dashboard - Snapshot Model

Representa una fotografía inmutable del estado del Dashboard.

Un DashboardSnapshot consolida la información presentada por el
Dashboard en un instante determinado. No contiene lógica de
negocio ni realiza cálculos.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ia.dashboard.exceptions import DashboardSnapshotError
from ia.dashboard.models.dashboard_metrics import DashboardMetrics
from ia.dashboard.models.dashboard_statistics import (
    DashboardStatistics,
)
from ia.dashboard.models.dashboard_summary import DashboardSummary


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DashboardSnapshot:
    """
    Fotografía inmutable del estado del Dashboard.

    Agrupa todos los modelos que representan el estado
    consolidado del Dashboard en un instante determinado.
    """

    summary: DashboardSummary

    metrics: DashboardMetrics

    statistics: DashboardStatistics

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:
        """
        Valida las invariantes del dominio.
        """

        self._validate_timestamp()

    def _validate_timestamp(self) -> None:
        """
        Garantiza que el timestamp sea timezone-aware.
        """

        if self.generated_at.tzinfo is None:
            raise DashboardSnapshotError(
                "generated_at debe contener información de zona horaria."
            )


__all__ = [
    "DashboardSnapshot",
]
