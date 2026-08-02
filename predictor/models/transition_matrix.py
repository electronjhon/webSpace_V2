"""
Space AI 2.0

Transition Matrix

Immutable transition matrix used by Markov-based
prediction strategies.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.models.markov_state import MarkovState
from predictor.models.transition_probability import TransitionProbability


@dataclass(
    frozen=True,
    slots=True,
)
class TransitionMatrix:
    """
    Immutable transition matrix.
    """

    transitions: tuple[TransitionProbability, ...] = ()

    def outgoing(
        self,
        state: MarkovState,
    ) -> tuple[TransitionProbability, ...]:
        return tuple(
            transition for transition in self.transitions if transition.source == state
        )

    def most_probable(
        self,
        state: MarkovState,
    ) -> TransitionProbability | None:
        outgoing = self.outgoing(state)

        if not outgoing:
            return None

        return max(
            outgoing,
            key=lambda transition: transition.probability.value,
        )

    def is_empty(self) -> bool:
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
# 1.1.0
# ---------------------------------------------------------------------
