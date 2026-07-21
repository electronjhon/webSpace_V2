"""
Space AI 2.0

Transition Features Model

Immutable data transfer object containing the
transition-related features extracted from a rolling window.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class TransitionFeatures:
    """
    Transition-related metrics extracted from
    a rolling window.

    All values are computed by the
    TransitionExtractor.
    """

    transition_score: float

    repeat_probability: float

    alternation_probability: float
