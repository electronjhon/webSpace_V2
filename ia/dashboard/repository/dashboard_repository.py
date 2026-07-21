"""
Space AI 2.0

Dashboard Repository

Contrato de acceso a la información utilizada por el Dashboard.

El DashboardRepository actúa como adaptador entre los distintos
motores del sistema y el DashboardAggregator.

No contiene lógica de negocio ni realiza cálculos. Su única
responsabilidad consiste en proporcionar acceso uniforme a los
objetos del dominio necesarios para construir un
DashboardSnapshot.

Sprint:
    9

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from ia.decision_engine.decision import Decision
from ia.learning_engine.learning_engine import LearningEngine
from ia.signal_engine.result import SignalResult
from predictor.prediction import Prediction
from state_engine.models.classification_result import (
    ClassificationResult,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class DashboardRepository:
    """
    Adaptador de lectura utilizado por el Dashboard.

    Agrupa los resultados producidos por los distintos motores
    del sistema sin introducir lógica de negocio.
    """

    prediction: Prediction

    classification: ClassificationResult

    decision: Decision

    signal_result: SignalResult

    learning_engine: LearningEngine


__all__ = [
    "DashboardRepository",
]
