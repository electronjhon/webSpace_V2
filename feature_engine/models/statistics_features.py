"""
Space AI 2.0

Statistics Features Model

Immutable data transfer object containing the
descriptive statistical features extracted from
a rolling window.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class StatisticsFeatures:
    """
    Descriptive statistical metrics extracted
    from a rolling window.

    All values are computed by the
    StatisticsExtractor.
    """

    minimum: float

    maximum: float

    range_value: float

    mean: float

    median: float

    variance: float

    standard_deviation: float

    mad: float

    coefficient_of_variation: float

    root_mean_square: float
