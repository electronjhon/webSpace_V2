"""
Space AI 2.0

Quality Extractor

Extracts quality-related metrics from a rolling window.
"""

from __future__ import annotations

from core.analytics import Analytics
from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.base_extractor import BaseExtractor
from feature_engine.models.quality_features import QualityFeatures


class QualityExtractor(
    BaseExtractor[QualityFeatures],
):
    """
    Extracts quality-related metrics from a rolling window.

    This extractor performs no analytical computations.

    Every metric is delegated to Analytics.
    """

    @classmethod
    def extract(
        cls,
        window: RollingWindow[Number],
    ) -> QualityFeatures:
        """
        Extracts quality-related features.

        Args:
            window:
                Source rolling window.

        Returns:
            Immutable QualityFeatures.
        """

        values = cls.values(window)

        confidence = Analytics.confidence(values)

        stability = Analytics.stability(values)

        noise = Analytics.noise_level(values)

        volatility = Analytics.coefficient_of_variation(
            values,
        )

        balance = 1.0 - volatility

        return QualityFeatures(
            confidence=confidence,
            stability=stability,
            noise=noise,
            balance=balance,
            volatility=volatility,
        )
