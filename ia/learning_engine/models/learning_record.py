"""
Space AI 2.0

Learning Engine

Learning Record

Aggregate Root del Learning Engine.

Representa un evento completo de aprendizaje, agrupando
la predicción, la clasificación del estado y la
retroalimentación obtenida tras evaluar el resultado real.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from ia.learning_engine.exceptions import (
    InvalidLearningRecordError,
)
from ia.learning_engine.models.feedback import Feedback
from predictor.prediction import Prediction
from state_engine.models.classification_result import (
    ClassificationResult,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningRecord:
    """
    Aggregate Root del Learning Engine.

    Representa un único evento histórico de aprendizaje.
    """

    record_id: UUID = field(
        default_factory=uuid4,
    )

    prediction: Prediction

    classification: ClassificationResult

    feedback: Feedback

    created_at: datetime = field(
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

        if self.created_at.tzinfo is None:
            raise InvalidLearningRecordError(
                "created_at debe contener información " "de zona horaria."
            )


__all__ = [
    "LearningRecord",
]
