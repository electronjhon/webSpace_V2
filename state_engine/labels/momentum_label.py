from __future__ import annotations

from enum import StrEnum


class MomentumLabel(StrEnum):
    """
    Represents the strength of movement independently of direction.

    Momentum measures how strongly the sequence is evolving,
    regardless of whether the trend is upward or downward.
    """

    VERY_WEAK = "very_weak"
    WEAK = "weak"
    MODERATE = "moderate"
    STRONG = "strong"
    VERY_STRONG = "very_strong"

    def __str__(self) -> str:
        return self.value
