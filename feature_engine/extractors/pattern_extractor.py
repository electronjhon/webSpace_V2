"""
Space AI 2.0

Pattern Extractor

Extracts pattern-related features from a rolling window.
"""

from __future__ import annotations

from core.analytics import Analytics
from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.base_extractor import BaseExtractor
from feature_engine.models.pattern_features import PatternFeatures


class PatternExtractor:
    """
    Extracts pattern-related metrics from
    a rolling window.
    """

    @staticmethod
    def extract(
        window: RollingWindow[Number],
    ) -> PatternFeatures:
        """
        Extract pattern features.

        Args:
            window:
                Source rolling window.

        Returns:
            PatternFeatures.
        """

        values = BaseExtractor.values(window)

        return PatternFeatures(
            entropy=Analytics.entropy(values),
            compression=Analytics.compression(values),
            spike_score=Analytics.spike_score(values),
            pattern_strength=Analytics.pattern_strength(values),
        )
