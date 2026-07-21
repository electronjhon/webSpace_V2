"""
Space AI 2.0

Ensemble Prediction Strategy

Prediction strategy combining multiple prediction
strategies.
"""

from __future__ import annotations

from feature_engine.models.feature_vector import FeatureVector
from predictor.prediction_result import PredictionResult
from predictor.strategies.base_strategy import BaseStrategy
from predictor.strategies.bayesian_strategy import BayesianStrategy
from predictor.strategies.markov_strategy import MarkovStrategy
from state_engine.models.classification_result import (
    ClassificationResult,
)
from state_engine.state_history import StateHistory


class EnsembleStrategy(BaseStrategy):
    """
    Prediction strategy that combines multiple
    prediction strategies.

    Version 1.0 selects the prediction with the
    highest confidence.
    """

    def __init__(self) -> None:
        self._markov = MarkovStrategy()
        self._bayesian = BayesianStrategy()

    def predict(
        self,
        feature_vector: FeatureVector,
        classification: ClassificationResult,
        history: StateHistory,
    ) -> PredictionResult:
        """
        Predict the next state by combining the
        available prediction strategies.
        """

        markov_result = self._markov.predict(
            feature_vector=feature_vector,
            classification=classification,
            history=history,
        )

        bayesian_result = self._bayesian.predict(
            feature_vector=feature_vector,
            classification=classification,
            history=history,
        )

        if (
            markov_result.prediction.confidence.value
            >= bayesian_result.prediction.confidence.value
        ):
            return markov_result

        return bayesian_result


__all__ = [
    "EnsembleStrategy",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
