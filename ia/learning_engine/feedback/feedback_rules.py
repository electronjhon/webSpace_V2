"""
Space AI 2.0

Learning Engine

Feedback Rules

Define las reglas oficiales del dominio para evaluar
la calidad de una predicción mediante un LearningScore
y clasificar el resultado obtenido.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from decimal import Decimal

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.enums import FeedbackOutcome


class FeedbackRules:
    """
    Reglas oficiales del dominio para clasificar Feedback.
    """

    SUCCESS_THRESHOLD = Decimal("0.90")

    PARTIAL_SUCCESS_THRESHOLD = Decimal("0.60")

    @classmethod
    def classify(
        cls,
        score: LearningScore,
    ) -> FeedbackOutcome:
        """
        Clasifica un LearningScore en un FeedbackOutcome.
        """

        value = score.value

        if value >= cls.SUCCESS_THRESHOLD:
            return FeedbackOutcome.SUCCESS

        if value >= cls.PARTIAL_SUCCESS_THRESHOLD:
            return FeedbackOutcome.PARTIAL_SUCCESS

        return FeedbackOutcome.FAILURE


__all__ = [
    "FeedbackRules",
]
