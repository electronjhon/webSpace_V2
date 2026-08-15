"""
Space AI 2.0

Learning Engine

Learning Statistics

Objeto de solo lectura que representa un resumen
agregado del estado del proceso de aprendizaje.

No calcula métricas; únicamente agrupa los resultados
producidos por los servicios especializados del módulo
metrics.

Sprint:
    15

Versión:
    2.0.0
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from decimal import Decimal

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.enums import FeedbackOutcome


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningStatistics:
    """
    Snapshot inmutable del estado del aprendizaje.

    Agrupa las métricas calculadas por los servicios
    especializados del Learning Engine.
    """

    average_score: LearningScore

    average_confidence: LearningScore

    success_rate: Decimal

    outcome_distribution: Counter[FeedbackOutcome]


__all__ = [
    "LearningStatistics",
]
