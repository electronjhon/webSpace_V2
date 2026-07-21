"""
Space AI 2.0

Trend Extractor

Extracts trend-related features from a
rolling window.
"""

from __future__ import annotations

from core.statistics import Statistics
from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.base_extractor import BaseExtractor
from feature_engine.models.trend_features import TrendFeatures


class TrendExtractor:
    """
    Extracts trend-related metrics from
    a rolling window.
    """

    @staticmethod
    def extract(
        window: RollingWindow[Number],
    ) -> TrendFeatures:
        """
        Extract trend features.

        Args:
            window:
                Source rolling window.

        Returns:
            TrendFeatures.
        """

        values = BaseExtractor.values(window)

        return TrendFeatures(
            slope=Statistics.slope(values),
            momentum=Statistics.momentum(values),
        )
