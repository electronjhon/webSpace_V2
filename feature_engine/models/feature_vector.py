"""
Space AI 2.0

Feature Vector

Main immutable contract exchanged between
the FeatureEngine and downstream engines.
"""

from __future__ import annotations

from dataclasses import dataclass

from .pattern_features import PatternFeatures
from .quality_features import QualityFeatures
from .statistics_features import StatisticsFeatures
from .transition_features import TransitionFeatures
from .trend_features import TrendFeatures


@dataclass(
    frozen=True,
    slots=True,
)
class FeatureVector:
    """
    Complete feature set extracted from a
    rolling window.

    This object is the official output of
    the FeatureEngine and the official input
    of all downstream engines.
    """

    window_size: int

    statistics: StatisticsFeatures

    trend: TrendFeatures

    pattern: PatternFeatures

    quality: QualityFeatures

    transition: TransitionFeatures | None = None
