"""
Space AI 2.0
------------

Dashboard - Enumerations

Define todas las enumeraciones utilizadas por el Dashboard.

Principios de diseño
--------------------
- Uso de StrEnum para facilitar serialización y logging.
- Compatible con Python 3.13.5.
- Sin dependencias del resto del módulo.
- Archivo estable (no debe modificarse salvo decisión arquitectónica).
"""

from __future__ import annotations

from enum import StrEnum, auto


class DashboardStatus(StrEnum):
    """
    Estado general del Dashboard.
    """

    READY = auto()
    UPDATING = auto()
    DEGRADED = auto()
    ERROR = auto()


class EngineStatus(StrEnum):
    """
    Estado de un motor monitoreado por el Dashboard.
    """

    AVAILABLE = auto()
    UNAVAILABLE = auto()
    WARNING = auto()
    ERROR = auto()


class MetricTrend(StrEnum):
    """
    Tendencia observada en una métrica.
    """

    IMPROVING = auto()
    STABLE = auto()
    DEGRADING = auto()
    UNKNOWN = auto()


class DashboardSection(StrEnum):
    """
    Secciones funcionales del Dashboard.
    """

    STATE_ENGINE = auto()
    PREDICTOR = auto()
    DECISION_ENGINE = auto()
    SIGNAL_ENGINE = auto()
    LEARNING_ENGINE = auto()
    OVERVIEW = auto()


class SnapshotStatus(StrEnum):
    """
    Estado de generación de un DashboardSnapshot.
    """

    COMPLETE = auto()
    PARTIAL = auto()
    FAILED = auto()


__all__ = [
    "DashboardSection",
    "DashboardStatus",
    "EngineStatus",
    "MetricTrend",
    "SnapshotStatus",
]
