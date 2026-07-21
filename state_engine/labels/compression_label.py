from __future__ import annotations

from enum import StrEnum


class CompressionLabel(StrEnum):
    """
    Represents the degree of compression of the analyzed sequence.

    Compression measures how concentrated or dispersed the recent
    outcomes are. Highly compressed sequences tend to exhibit low
    variability, whereas low compression indicates a more dispersed
    behavior.
    """

    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

    def __str__(self) -> str:
        return self.value
