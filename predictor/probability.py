"""
Space AI 2.0

Probability

Immutable probability value object used by the
Predictor Engine.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class Probability:
    """
    Immutable probability value.

    Represents the probability assigned to a predicted
    state by a prediction strategy.

    The value is expected to be normalized in the
    [0.0, 1.0] interval.
    """

    value: float


__all__ = [
    "Probability",
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
