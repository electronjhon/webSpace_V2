"""
Space AI 2.0

Transition Matrix Builder

Builds immutable transition matrices from
state histories.
"""

from __future__ import annotations

from collections import Counter

from predictor.models.markov_state import MarkovState
from predictor.models.markov_state_extractor import MarkovStateExtractor
from predictor.models.transition_matrix import TransitionMatrix
from predictor.models.transition_probability import TransitionProbability
from predictor.probability import Probability
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

        transition_counts: Counter[tuple[MarkovState, MarkovState]] = Counter()

        outgoing_counts: Counter[MarkovState] = Counter()

        for transition in history.transitions:
            source = MarkovStateExtractor.extract(
                transition.from_state,
            )

            target = MarkovStateExtractor.extract(
                transition.to_state,
            )

            transition_counts[(source, target)] += 1

            outgoing_counts[source] += 1

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
# 1.1.0
# ---------------------------------------------------------------------
