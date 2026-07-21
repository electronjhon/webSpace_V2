from __future__ import annotations

from enum import StrEnum


class VolatilityLabel(StrEnum):
    """
    Represents the magnitude of variation within the analyzed sequence.

    Volatility measures how rapidly the sequence changes over time,
    independently of its direction, entropy or compression.
    """

    VERY_STABLE = "very_stable"
    STABLE = "stable"
    MODERATE = "moderate"
    VOLATILE = "volatile"
    HIGHLY_VOLATILE = "highly_volatile"

    def __str__(self) -> str:
        return self.value
