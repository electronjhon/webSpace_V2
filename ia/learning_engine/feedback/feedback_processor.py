"""
Space AI 2.0

Learning Engine

Feedback Processor

Construye objetos Feedback a partir de una Signal,
un ObservedOutcome y un LearningScore.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.feedback.feedback_rules import (
    FeedbackRules,
)
from ia.learning_engine.models.feedback import Feedback
from ia.learning_engine.models.observed_outcome import (
    ObservedOutcome,
)
from ia.signal_engine.value_objects.signal import Signal


class FeedbackProcessor:
    """
    Responsable de construir Feedback del dominio.
    """

    @staticmethod
    def create(
        *,
        signal: Signal,
        observed_outcome: ObservedOutcome,
        learning_score: LearningScore,
    ) -> Feedback:
        """
        Construye un Feedback completamente validado.
        """

        return Feedback(
            signal=signal,
            observed_outcome=observed_outcome,
            outcome=FeedbackRules.classify(
                learning_score,
            ),
            learning_score=learning_score,
        )


__all__ = [
    "FeedbackProcessor",
]
