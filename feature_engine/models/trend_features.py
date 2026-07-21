"""
Space AI 2.0

Trend Features Model

Immutable data transfer object containing the
trend-related features extracted from a rolling window.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class TrendFeatures:
    """
    Trend-related metrics extracted from
    a rolling window.

    All values are computed by the
    TrendExtractor.
    """

    slope: float

    momentum: float
