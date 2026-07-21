"""
Space AI 2.0

Transition Matrix

Immutable transition matrix used by Markov-based
prediction strategies.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.models.transition_probability import TransitionProbability
from state_engine.state import State


@dataclass(
    frozen=True,
    slots=True,
)
class TransitionMatrix:
    """
    Immutable transition matrix.

    Represents the complete set of transition
    probabilities inferred from a StateHistory.

    This object contains no business logic.

    Matrix construction is the responsibility of
    TransitionMatrixBuilder.
    """

    transitions: tuple[TransitionProbability, ...] = ()

    def outgoing(
        self,
        state: State,
    ) -> tuple[TransitionProbability, ...]:
        """
        Return every outgoing transition from a state.

        Parameters
        ----------
        state:
            Source state.

        Returns
        -------
        tuple[TransitionProbability, ...]
            Outgoing transitions.
        """

        return tuple(
            transition for transition in self.transitions if transition.source == state
        )

    def most_probable(
        self,
        state: State,
    ) -> TransitionProbability | None:
        """
        Return the most probable outgoing transition.

        Parameters
        ----------
        state:
            Source state.

        Returns
        -------
        TransitionProbability | None
            Transition with the highest probability,
            or None if no outgoing transition exists.
        """

        outgoing = self.outgoing(state)

        if not outgoing:
            return None

        return max(
            outgoing,
            key=lambda transition: transition.probability.value,
        )

    def is_empty(self) -> bool:
        """
        Determine whether the transition matrix is empty.

        Returns
        -------
        bool
            True if the matrix contains no transitions.
        """

        return len(self.transitions) == 0


__all__ = [
    "TransitionMatrix",
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
