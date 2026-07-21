"""
Space AI 2.0

Learning Engine

Learning Repository

Repositorio inmutable responsable de gestionar el acceso
a los registros de aprendizaje del dominio.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from ia.learning_engine.history.result_history import (
    ResultHistory,
)
from ia.learning_engine.models.learning_record import (
    LearningRecord,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningRepository:
    """
    Repositorio del dominio para LearningRecord.

    Actualmente mantiene un historial inmutable en memoria.
    La persistencia física será integrada posteriormente
    mediante SQLite sin modificar el dominio.
    """

    history: ResultHistory

    def save(
        self,
        record: LearningRecord,
    ) -> LearningRepository:
        """
        Devuelve una nueva instancia del repositorio con el
        registro agregado.
        """

        return LearningRepository(
            history=self.history.append(record),
        )

    def all(self) -> tuple[LearningRecord, ...]:
        """
        Devuelve todos los registros almacenados.
        """

        return self.history.records

    def latest(self) -> LearningRecord | None:
        """
        Devuelve el último registro disponible.
        """

        if self.history.is_empty:
            return None

        return self.history.records[-1]

    @property
    def size(self) -> int:
        """
        Número de registros almacenados.
        """

        return self.history.size

    @property
    def is_empty(self) -> bool:
        """
        Indica si el repositorio está vacío.
        """

        return self.history.is_empty


__all__ = [
    "LearningRepository",
]
