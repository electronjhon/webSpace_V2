"""
Space AI 2.0

Feature Engine

Coordinates every feature extractor and builds the
immutable FeatureVector consumed by the remaining
AI engines.
"""

from __future__ import annotations

from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.pattern_extractor import PatternExtractor
from feature_engine.extractors.quality_extractor import QualityExtractor
from feature_engine.extractors.statistics_extractor import StatisticsExtractor
from feature_engine.extractors.transition_extractor import TransitionExtractor
from feature_engine.extractors.trend_extractor import TrendExtractor
from feature_engine.models.feature_vector import FeatureVector


class FeatureEngine:
    """
    Coordinates feature extraction.

    This class contains no analytical algorithms.

    Every calculation is delegated to the
    specialized extractors.
    """

    @staticmethod
    def extract(
        window: RollingWindow[Number],
    ) -> FeatureVector:
        """
        Extracts every feature from the supplied
        rolling window.

        Args:
            window:
                Source rolling window.

        Returns:
            Immutable FeatureVector.
        """

        statistics = StatisticsExtractor.extract(window)

        trend = TrendExtractor.extract(window)

        pattern = PatternExtractor.extract(window)

        transition = TransitionExtractor.extract(window)

        quality = QualityExtractor.extract(window)

        return FeatureVector(
            window_size=len(window),
            statistics=statistics,
            trend=trend,
            pattern=pattern,
            transition=transition,
            quality=quality,
        )
