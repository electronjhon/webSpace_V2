"""
Space AI 2.0

Transition Probability

Immutable transition probability between two states.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.models.markov_state import MarkovState
from predictor.probability import Probability


@dataclass(
    frozen=True,
    slots=True,
)
class TransitionProbability:
    """
    Immutable transition probability.

    Represents the probability of transitioning
    from one Markov state to another.

    This object contains no business logic.
    """

    source: MarkovState

    target: MarkovState

    probability: Probability


__all__ = [
    "TransitionProbability",
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
