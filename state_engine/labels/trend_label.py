from __future__ import annotations

from enum import StrEnum


class TrendLabel(StrEnum):
    """
    Represents the directional trend of the analyzed sequence.

    The trend is intentionally independent from momentum,
    volatility and entropy so that each state dimension
    remains orthogonal within the StateEngine.
    """

    STRONG_DOWN = "strong_down"
    DOWN = "down"
    NEUTRAL = "neutral"
    UP = "up"
    STRONG_UP = "strong_up"

    def __str__(self) -> str:
        return self.value
