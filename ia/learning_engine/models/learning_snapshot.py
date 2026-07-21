"""
Space AI 2.0

Learning Engine

Learning Snapshot

Representa una instantánea inmutable del estado del
Learning Engine en un momento determinado.

Un LearningSnapshot resume el conocimiento consolidado
hasta un instante específico y será utilizado por el
Dashboard, procesos de análisis y futuras exportaciones.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ia.learning_engine.exceptions import (
    InvalidLearningSnapshotError,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningSnapshot:
    """
    Snapshot inmutable del estado del Learning Engine.
    """

    total_records: int

    successful_records: int

    partial_successful_records: int

    failed_records: int

    average_score: float

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:
        """
        Valida las invariantes del dominio.
        """

        self._validate_counts()
        self._validate_average_score()
        self._validate_timestamp()

    def _validate_counts(self) -> None:
        """
        Valida que los contadores sean consistentes.
        """

        counters = (
            self.total_records,
            self.successful_records,
            self.partial_successful_records,
            self.failed_records,
        )

        if any(value < 0 for value in counters):
            raise InvalidLearningSnapshotError(
                "Los contadores no pueden ser negativos."
            )

        if (
            self.successful_records
            + self.partial_successful_records
            + self.failed_records
            != self.total_records
        ):
            raise InvalidLearningSnapshotError(
                "La suma de los registros no coincide con " "total_records."
            )

    def _validate_average_score(self) -> None:
        """
        Valida el rango permitido del promedio.
        """

        if not 0.0 <= self.average_score <= 1.0:
            raise InvalidLearningSnapshotError(
                "average_score debe estar entre 0.0 y 1.0."
            )

    def _validate_timestamp(self) -> None:
        """
        Garantiza que created_at sea timezone-aware.
        """

        if self.created_at.tzinfo is None:
            raise InvalidLearningSnapshotError(
                "created_at debe contener información " "de zona horaria."
            )


__all__ = [
    "LearningSnapshot",
]
