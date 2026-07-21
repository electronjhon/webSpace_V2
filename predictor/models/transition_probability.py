"""
Space AI 2.0

Transition Probability

Immutable transition probability between two states.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.probability import Probability
from state_engine.state import State


@dataclass(
    frozen=True,
    slots=True,
)
class TransitionProbability:
    """
    Immutable transition probability.

    Represents the probability of transitioning
    from one state to another.

    This object contains no business logic.
    """

    source: State

    target: State

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
# 1.0.0
# ---------------------------------------------------------------------
