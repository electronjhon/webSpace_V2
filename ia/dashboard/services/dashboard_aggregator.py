"""
Space AI 2.0

Dashboard Aggregator

Responsable de construir un DashboardSnapshot a partir de la
información proporcionada por el DashboardRepository.

El DashboardAggregator no contiene lógica de negocio.
Su única responsabilidad consiste en transformar los datos
provenientes de los motores del sistema en modelos propios
del Dashboard.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.dashboard.enums import (
    DashboardStatus,
    EngineStatus,
)
from ia.dashboard.models.dashboard_metrics import DashboardMetrics
from ia.dashboard.models.dashboard_snapshot import DashboardSnapshot
from ia.dashboard.models.dashboard_statistics import (
    DashboardStatistics,
)
from ia.dashboard.models.dashboard_summary import DashboardSummary
from ia.dashboard.repository.dashboard_repository import (
    DashboardRepository,
)


class DashboardAggregator:
    """
    Servicio responsable de construir un DashboardSnapshot.
    """

    @staticmethod
    def build_snapshot(
        *,
        repository: DashboardRepository,
    ) -> DashboardSnapshot:
        """
        Construye un DashboardSnapshot a partir de la
        información consolidada del DashboardRepository.
        """

        return DashboardSnapshot(
            summary=DashboardAggregator._build_summary(
                repository=repository,
            ),
            metrics=DashboardAggregator._build_metrics(
                repository=repository,
            ),
            statistics=DashboardAggregator._build_statistics(
                repository=repository,
            ),
        )

    @staticmethod
    def _build_summary(
        *,
        repository: DashboardRepository,
    ) -> DashboardSummary:
        """
        Construye el resumen general del Dashboard.
        """

        dashboard_status = (
            DashboardStatus.READY
            if (
                repository.signal_result.accepted
                and not repository.learning_engine.history.is_empty
            )
            else DashboardStatus.DEGRADED
        )

        return DashboardSummary(
            dashboard_status=dashboard_status,
            predictor_status=EngineStatus.AVAILABLE,
            state_engine_status=EngineStatus.AVAILABLE,
            decision_engine_status=EngineStatus.AVAILABLE,
            signal_engine_status=EngineStatus.AVAILABLE,
            learning_engine_status=EngineStatus.AVAILABLE,
        )

    @staticmethod
    def _build_metrics(
        *,
        repository: DashboardRepository,
    ) -> DashboardMetrics:
        """
        Construye las métricas globales del Dashboard.
        """

        return DashboardMetrics(
            average_learning_score=(repository.learning_engine.average_score),
            average_confidence=(repository.learning_engine.average_confidence),
        )

    @staticmethod
    def _build_statistics(
        *,
        repository: DashboardRepository,
    ) -> DashboardStatistics:
        """
        Construye las estadísticas agregadas del Dashboard.
        """

        return DashboardStatistics(
            signal_accepted=repository.signal_result.accepted,
            has_learning_history=(not repository.learning_engine.history.is_empty),
        )


__all__ = [
    "DashboardAggregator",
]
