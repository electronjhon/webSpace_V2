"""
Space AI 2.0

Learning Engine

Observed Outcome

Representa el resultado real observado después de la
ejecución de una señal.

Este Value Object constituye la referencia contra la
cual el Learning Engine evalúa la calidad de las
predicciones, decisiones y señales generadas por el
pipeline de IA.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ia.learning_engine.exceptions import (
    InvalidObservedOutcomeError,
)
from state_engine.state_labels import StateLabels


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class ObservedOutcome:
    """
    Resultado real observado por el sistema.

    Este modelo representa el estado finalmente
    confirmado tras la ejecución de una señal.
    """

    labels: StateLabels

    observed_at: datetime = field(
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

        if self.observed_at.tzinfo is None:
            raise InvalidObservedOutcomeError(
                "observed_at debe contener información " "de zona horaria."
            )


__all__ = [
    "ObservedOutcome",
]
