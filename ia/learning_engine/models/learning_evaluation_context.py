"""
Space AI 2.0

Learning Engine

Learning Evaluation Context

Conserva el contexto necesario para evaluar una predicción
cuando se disponga del estado observado de la siguiente
iteración del pipeline.

Sprint:
    15
Versión:
    1.1.0
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.prediction import Prediction
from state_engine.models.classification_result import ClassificationResult


@dataclass(
    frozen=True,
    slots=True,
)
class LearningEvaluationContext:
    """
    Contexto inmutable de una evaluación predictiva pendiente.

    Contiene los elementos generados por una misma
    iteración que deberán conservarse hasta disponer
    del estado observado posterior.
    """

    classification: ClassificationResult

    prediction: Prediction


__all__ = [
    "LearningEvaluationContext",
]
