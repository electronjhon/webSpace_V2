"""
Space AI 2.0

Learning Engine

Incremental Learner

Responsable de incorporar nuevos registros de aprendizaje
al repositorio del Learning Engine.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.learning_engine.models.learning_record import (
    LearningRecord,
)
from ia.learning_engine.repository.learning_repository import (
    LearningRepository,
)


class IncrementalLearner:
    """
    Ejecuta el aprendizaje incremental del sistema.
    """

    @staticmethod
    def learn(
        *,
        repository: LearningRepository,
        record: LearningRecord,
    ) -> LearningRepository:
        """
        Incorpora un nuevo registro al historial.
        """

        return repository.save(record)


__all__ = [
    "IncrementalLearner",
]
