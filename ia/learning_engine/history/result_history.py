"""
Space AI 2.0

Learning Engine

Result History

Gestiona el historial inmutable de registros de
aprendizaje producidos por el Learning Engine.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from ia.learning_engine.models.learning_record import (
    LearningRecord,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class ResultHistory:
    """
    Historial inmutable de registros de aprendizaje.
    """

    records: tuple[LearningRecord, ...] = field(
        default_factory=tuple,
    )

    @property
    def size(self) -> int:
        """
        Número de registros almacenados.
        """

        return len(self.records)

    @property
    def is_empty(self) -> bool:
        """
        Indica si el historial está vacío.
        """

        return not self.records

    def append(
        self,
        record: LearningRecord,
    ) -> ResultHistory:
        """
        Devuelve un nuevo historial con el registro agregado.
        """

        return ResultHistory(
            records=(
                *self.records,
                record,
            ),
        )

    def __iter__(self) -> Iterator[LearningRecord]:
        """
        Iterador sobre los registros.
        """

        return iter(self.records)

    def __len__(self) -> int:
        """
        Número de registros.
        """

        return self.size


__all__ = [
    "ResultHistory",
]
