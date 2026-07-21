from __future__ import annotations

from enum import StrEnum


class BalanceLabel(StrEnum):
    """
    Represents the balance between the competing outcomes of the
    analyzed sequence.

    A balanced sequence exhibits a similar distribution between
    outcomes, whereas an imbalanced sequence is dominated by one
    outcome over the others.
    """

    VERY_IMBALANCED = "very_imbalanced"
    IMBALANCED = "imbalanced"
    BALANCED = "balanced"
    WELL_BALANCED = "well_balanced"
    PERFECTLY_BALANCED = "perfectly_balanced"

    def __str__(self) -> str:
        return self.value
