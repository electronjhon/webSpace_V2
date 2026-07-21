"""
Space AI 2.0

Transition Matrix Builder

Builds immutable transition matrices from
state histories.
"""

from __future__ import annotations

from collections import Counter

from predictor.models.transition_matrix import TransitionMatrix
from predictor.models.transition_probability import TransitionProbability
from predictor.probability import Probability
from state_engine.state import State
from state_engine.state_history import StateHistory


class TransitionMatrixBuilder:
    """
    Factory responsible for constructing immutable
    transition matrices from a StateHistory.
    """

    @staticmethod
    def build(history: StateHistory) -> TransitionMatrix:
        """
        Build a transition matrix from a state history.

        Parameters
        ----------
        history:
            Historical sequence of states.

        Returns
        -------
        TransitionMatrix
            Immutable transition matrix.
        """

        if len(history.transitions) == 0:
            return TransitionMatrix()

        transition_counts: Counter[tuple[State, State]] = Counter()
        outgoing_counts: Counter[State] = Counter()

        for transition in history.transitions:
            transition_counts[(transition.from_state, transition.to_state)] += 1

            outgoing_counts[transition.from_state] += 1

        probabilities: list[TransitionProbability] = []

        for (source, target), count in transition_counts.items():
            total = outgoing_counts[source]

            probabilities.append(
                TransitionProbability(
                    source=source,
                    target=target,
                    probability=Probability(
                        value=count / total,
                    ),
                ),
            )

        return TransitionMatrix(
            transitions=tuple(probabilities),
        )


__all__ = [
    "TransitionMatrixBuilder",
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
