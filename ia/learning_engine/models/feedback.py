"""
Space AI 2.0

Learning Engine

Feedback

Value Object que representa la evaluación de una señal
emitida por el sistema frente al resultado realmente
observado.

Feedback constituye la unidad básica de retroalimentación
del Learning Engine y será utilizado posteriormente por
los componentes de métricas, aprendizaje incremental y
optimización.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.enums import FeedbackOutcome
from ia.learning_engine.exceptions import InvalidFeedbackError
from ia.learning_engine.models.observed_outcome import (
    ObservedOutcome,
)
from ia.signal_engine.value_objects.signal import Signal


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class Feedback:
    """
    Value Object que representa la evaluación de una señal.

    Un Feedback relaciona una Signal emitida por el sistema
    con el resultado finalmente observado, indicando tanto
    la evaluación cualitativa como la puntuación obtenida
    durante el proceso de aprendizaje.
    """

    signal: Signal

    observed_outcome: ObservedOutcome

    outcome: FeedbackOutcome

    learning_score: LearningScore

    evaluated_at: datetime = field(
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

        if self.evaluated_at.tzinfo is None:
            raise InvalidFeedbackError(
                "evaluated_at debe contener información " "de zona horaria."
            )


__all__ = [
    "Feedback",
]
