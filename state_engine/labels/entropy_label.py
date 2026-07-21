from __future__ import annotations

from enum import StrEnum


class EntropyLabel(StrEnum):
    """
    Represents the degree of uncertainty or randomness of the sequence.

    Lower entropy indicates a more predictable and structured behavior,
    while higher entropy indicates greater randomness and less
    predictability.
    """

    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

    def __str__(self) -> str:
        return self.value
