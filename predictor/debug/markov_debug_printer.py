"""
Space AI 2.0

Markov Debug Printer

Centralized diagnostic output for the
Markov prediction subsystem.
"""

from __future__ import annotations

from predictor.models.markov_state import MarkovState
from predictor.models.transition_probability import (
    TransitionProbability,
)
from predictor.prediction_status import PredictionStatus


class MarkovDebugPrinter:
    """
    Prints diagnostic information related to
    Markov predictions.

    This class contains no business logic.
    """

    @staticmethod
    def print_prediction(
        *,
        current_state: MarkovState,
        transition: TransitionProbability,
        status: PredictionStatus,
    ) -> None:
        """
        Print the current prediction status.
        """

        print()

        print("========== MARKOV ==========")

        print(f"Current state : {current_state}")

        print(
            f"Next state    : {transition.target}",
        )

        print(
            "Probability  : " f"{transition.probability.value:.4f}",
        )

        print(
            "Status       : " f"{status.name}",
        )

        print("============================")

        print()


__all__ = [
    "MarkovDebugPrinter",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# NO
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
