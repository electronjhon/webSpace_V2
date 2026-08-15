from __future__ import annotations

from dataclasses import dataclass

from ia.learning_engine.models.learning_record import (
    LearningRecord,
)


@dataclass(frozen=True, slots=True)
class LearningResult:
    """
    Resultado producido por el Learning Engine después de
    procesar un nuevo evento de aprendizaje.

    Encapsula el registro generado y las métricas
    globales actualizadas del sistema.
    """

    record: LearningRecord

    total_samples: int

    accuracy: float

    updated: bool
