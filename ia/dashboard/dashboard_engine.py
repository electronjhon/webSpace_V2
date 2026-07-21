"""
Space AI 2.0

Dashboard Engine

Facade principal del Dashboard.

Coordina la construcción de un DashboardSnapshot utilizando
la información consolidada por el DashboardRepository.

Toda la lógica de agregación permanece encapsulada dentro
del DashboardAggregator.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.dashboard.models.dashboard_snapshot import (
    DashboardSnapshot,
)
from ia.dashboard.repository.dashboard_repository import (
    DashboardRepository,
)
from ia.dashboard.services.dashboard_aggregator import (
    DashboardAggregator,
)


class DashboardEngine:
    """
    Facade principal del Dashboard.
    """

    @staticmethod
    def build(
        *,
        repository: DashboardRepository,
    ) -> DashboardSnapshot:
        """
        Construye un DashboardSnapshot a partir del
        DashboardRepository.
        """

        return DashboardAggregator.build_snapshot(
            repository=repository,
        )


__all__ = [
    "DashboardEngine",
]
