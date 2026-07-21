"""
Space AI 2.0

Threshold Range

Immutable value object representing a normalized
classification threshold range.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

LabelT = TypeVar("LabelT")


@dataclass(frozen=True, slots=True)
class ThresholdRange:
    """
    Immutable threshold range.

    Thresholds divide a continuous normalized value into
    five semantic regions.

        very_low ─ low ─ moderate ─ high ─ very_high

    Expected domain:

        0.0 ---------------------------- 1.0

    Signed domains (e.g. trend slope) are also supported
    by providing negative threshold values.
    """

    very_low: float
    low: float
    moderate: float
    high: float
    very_high: float

    def classify(
        self,
        value: float,
        *,
        very_low: LabelT,
        low: LabelT,
        moderate: LabelT,
        high: LabelT,
        very_high: LabelT,
    ) -> LabelT:
        """
        Classifies a value according to this threshold range.

        Args:
            value:
                Continuous value to classify.

            very_low:
                Label for values <= very_low threshold.

            low:
                Label for values <= low threshold.

            moderate:
                Label for values <= moderate threshold.

            high:
                Label for values <= high threshold.

            very_high:
                Label for values > high threshold.

        Returns:
            Semantic label associated with the supplied value.
        """

        if value <= self.very_low:
            return very_low

        if value <= self.low:
            return low

        if value <= self.moderate:
            return moderate

        if value <= self.high:
            return high

        return very_high
