"""
Space AI 2.0

Prediction Policy

Evaluates whether a prediction strategy is ready
to execute.
"""

from __future__ import annotations

from config.constants import MIN_MARKOV_TRANSITIONS
from predictor.prediction_status import PredictionStatus
from predictor.strategies.strategy_type import StrategyType
from state_engine.state_history import StateHistory


class PredictionPolicy:
    """
    Encapsulates the execution policy for every
    prediction strategy.
    """

    @staticmethod
    def evaluate(
        strategy: StrategyType,
        history: StateHistory,
    ) -> PredictionStatus:
        """
        Evaluate whether the selected strategy is
        ready to execute.

        Parameters
        ----------
        strategy:
            Prediction strategy.

        history:
            Current immutable state history.

        Returns
        -------
        PredictionStatus
            Current availability of the strategy.
        """

        match strategy:

            case StrategyType.MARKOV:

                if len(history.transitions) < MIN_MARKOV_TRANSITIONS:
                    return PredictionStatus.WARMUP

                return PredictionStatus.READY

            case _:
                return PredictionStatus.READY


__all__ = [
    "PredictionPolicy",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# NO
#
# Versión:
# 2.0.0
# ---------------------------------------------------------------------
