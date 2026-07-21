"""
Space AI 2.0

Rule-based State Classifier
"""

from __future__ import annotations

from feature_engine.models.feature_vector import FeatureVector
from state_engine.classification_thresholds import ClassificationThresholds
from state_engine.classifiers.base_classifier import BaseStateClassifier
from state_engine.labels.balance_label import BalanceLabel
from state_engine.labels.compression_label import CompressionLabel
from state_engine.labels.entropy_label import EntropyLabel
from state_engine.labels.momentum_label import MomentumLabel
from state_engine.labels.trend_label import TrendLabel
from state_engine.labels.volatility_label import VolatilityLabel
from state_engine.models.classification_result import ClassificationResult
from state_engine.state_labels import StateLabels


class RuleStateClassifier(BaseStateClassifier):
    """
    Default deterministic implementation of the StateEngine.

    Converts a FeatureVector into semantic labels using the
    official threshold repository.
    """

    def classify(
        self,
        features: FeatureVector,
    ) -> ClassificationResult:

        labels = StateLabels(
            trend=self._trend(features),
            momentum=self._momentum(features),
            entropy=self._entropy(features),
            compression=self._compression(features),
            balance=self._balance(features),
            volatility=self._volatility(features),
        )

        return ClassificationResult(
            labels=labels,
            confidence=features.quality.confidence,
        )

    # ---------------------------------------------------------
    # Trend
    # ---------------------------------------------------------

    def _trend(
        self,
        features: FeatureVector,
    ) -> TrendLabel:

        return ClassificationThresholds.TREND_SLOPE.classify(
            value=features.trend.slope,
            very_low=TrendLabel.STRONG_DOWN,
            low=TrendLabel.DOWN,
            moderate=TrendLabel.NEUTRAL,
            high=TrendLabel.UP,
            very_high=TrendLabel.STRONG_UP,
        )

    # ---------------------------------------------------------
    # Momentum
    # ---------------------------------------------------------

    def _momentum(
        self,
        features: FeatureVector,
    ) -> MomentumLabel:

        return ClassificationThresholds.MOMENTUM.classify(
            value=features.trend.momentum,
            very_low=MomentumLabel.VERY_WEAK,
            low=MomentumLabel.WEAK,
            moderate=MomentumLabel.MODERATE,
            high=MomentumLabel.STRONG,
            very_high=MomentumLabel.VERY_STRONG,
        )

    # ---------------------------------------------------------
    # Entropy
    # ---------------------------------------------------------

    def _entropy(
        self,
        features: FeatureVector,
    ) -> EntropyLabel:

        return ClassificationThresholds.ENTROPY.classify(
            value=features.pattern.entropy,
            very_low=EntropyLabel.VERY_LOW,
            low=EntropyLabel.LOW,
            moderate=EntropyLabel.MODERATE,
            high=EntropyLabel.HIGH,
            very_high=EntropyLabel.VERY_HIGH,
        )

    # ---------------------------------------------------------
    # Compression
    # ---------------------------------------------------------

    def _compression(
        self,
        features: FeatureVector,
    ) -> CompressionLabel:

        return ClassificationThresholds.COMPRESSION.classify(
            value=features.pattern.compression,
            very_low=CompressionLabel.VERY_LOW,
            low=CompressionLabel.LOW,
            moderate=CompressionLabel.MODERATE,
            high=CompressionLabel.HIGH,
            very_high=CompressionLabel.VERY_HIGH,
        )

    # ---------------------------------------------------------
    # Balance
    # ---------------------------------------------------------

    def _balance(
        self,
        features: FeatureVector,
    ) -> BalanceLabel:

        return ClassificationThresholds.BALANCE.classify(
            value=features.quality.balance,
            very_low=BalanceLabel.VERY_IMBALANCED,
            low=BalanceLabel.IMBALANCED,
            moderate=BalanceLabel.BALANCED,
            high=BalanceLabel.WELL_BALANCED,
            very_high=BalanceLabel.PERFECTLY_BALANCED,
        )

    # ---------------------------------------------------------
    # Volatility
    # ---------------------------------------------------------

    def _volatility(
        self,
        features: FeatureVector,
    ) -> VolatilityLabel:

        return ClassificationThresholds.VOLATILITY.classify(
            value=features.quality.volatility,
            very_low=VolatilityLabel.VERY_STABLE,
            low=VolatilityLabel.STABLE,
            moderate=VolatilityLabel.MODERATE,
            high=VolatilityLabel.VOLATILE,
            very_high=VolatilityLabel.HIGHLY_VOLATILE,
        )
