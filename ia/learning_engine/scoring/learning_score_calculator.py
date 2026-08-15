"""
Space AI 2.0

Learning Engine

Learning Score Calculator

Calcula la calidad de una predicción comparando sus
StateLabels con los StateLabels observados posteriormente.

Sprint:
    15
Versión:
    1.0.0
"""

from __future__ import annotations

from decimal import Decimal

from ia.core.value_objects.learning_score import LearningScore
from ia.learning_engine.models.observed_outcome import ObservedOutcome
from predictor.prediction import Prediction


class LearningScoreCalculator:
    """
    Calcula un LearningScore a partir de una predicción
    y del estado realmente observado.
    """

    _DIMENSION_COUNT = Decimal("6")

    @staticmethod
    def calculate(
        prediction: Prediction,
        observed_outcome: ObservedOutcome,
    ) -> LearningScore:
        """
        Calcula el score de aprendizaje.

        Cada una de las seis dimensiones de StateLabels
        aporta una coincidencia cuando el valor predicho
        coincide exactamente con el valor observado.
        """

        predicted = prediction.labels
        observed = observed_outcome.labels

        matches = sum(
            (
                predicted.trend == observed.trend,
                predicted.momentum == observed.momentum,
                predicted.entropy == observed.entropy,
                predicted.compression == observed.compression,
                predicted.balance == observed.balance,
                predicted.volatility == observed.volatility,
            ),
        )

        score = Decimal(matches) / LearningScoreCalculator._DIMENSION_COUNT

        return LearningScore(
            value=score,
        )


__all__ = [
    "LearningScoreCalculator",
]
