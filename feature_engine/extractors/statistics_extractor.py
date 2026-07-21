"""
Space AI 2.0

Statistics Extractor
"""

from __future__ import annotations

from core.statistics import Statistics
from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.base_extractor import BaseExtractor
from feature_engine.models.statistics_features import StatisticsFeatures


class StatisticsExtractor(
    BaseExtractor[StatisticsFeatures],
):
    """
    Extracts descriptive statistical metrics.
    """

    @staticmethod
    def extract(
        window: RollingWindow[Number],
    ) -> StatisticsFeatures:
        """
        Extracts descriptive statistics from a
        rolling window.

        Args:
            window:
                Source rolling window.

        Returns:
            StatisticsFeatures.
        """

        values = BaseExtractor.values(window)

        return StatisticsFeatures(
            minimum=Statistics.minimum(values),
            maximum=Statistics.maximum(values),
            range_value=Statistics.value_range(values),
            mean=Statistics.mean(values),
            median=Statistics.median(values),
            variance=Statistics.variance(values),
            standard_deviation=Statistics.standard_deviation(values),
            mad=Statistics.mad(values),
            coefficient_of_variation=Statistics.coefficient_of_variation(values),
            root_mean_square=Statistics.root_mean_square(values),
        )
