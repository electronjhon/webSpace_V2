"""
Space AI 2.0

Learning Engine

Learning History

Gestiona el historial completo de snapshots generados
por el Learning Engine durante su ciclo de vida.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from ia.learning_engine.models.learning_snapshot import (
    LearningSnapshot,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningHistory:
    """
    Historial inmutable de snapshots del Learning Engine.
    """

    snapshots: tuple[LearningSnapshot, ...] = field(
        default_factory=tuple,
    )

    @property
    def size(self) -> int:
        """
        Devuelve el número de snapshots almacenados.
        """

        return len(self.snapshots)

    @property
    def is_empty(self) -> bool:
        """
        Indica si el historial está vacío.
        """

        return not self.snapshots

    def append(
        self,
        snapshot: LearningSnapshot,
    ) -> LearningHistory:
        """
        Devuelve un nuevo historial con el snapshot agregado.
        """

        return LearningHistory(
            snapshots=(
                *self.snapshots,
                snapshot,
            ),
        )

    def latest(self) -> LearningSnapshot | None:
        """
        Devuelve el snapshot más reciente.
        """

        if self.is_empty:
            return None

        return self.snapshots[-1]

    def __iter__(self) -> Iterator[LearningSnapshot]:
        """
        Iterador sobre los snapshots.
        """

        return iter(self.snapshots)

    def __len__(self) -> int:
        """
        Devuelve el número de snapshots.
        """

        return self.size


__all__ = [
    "LearningHistory",
]
