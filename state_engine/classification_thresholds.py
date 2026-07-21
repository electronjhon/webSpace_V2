"""
Space AI 2.0

Classification Thresholds

Official threshold definitions used throughout the StateEngine.

This module centralizes every threshold required by:

- RuleStateClassifier
- Analytics
- Predictor
- Dashboard
- Diagnostic tools

No magic numbers should exist outside this file.
"""

from __future__ import annotations

from state_engine.threshold_range import ThresholdRange


class ClassificationThresholds:
    """
    Official threshold repository.

    This class centralizes every semantic threshold used
    throughout Space AI.

    StateEngine consumes the State Classification section,
    while Analytics, Predictor and Dashboard may also use
    the Analytical Metrics section.
    """

    # ==========================================================
    # STATE CLASSIFICATION
    # ==========================================================

    TREND_SLOPE = ThresholdRange(
        very_low=-0.80,
        low=-0.30,
        moderate=0.00,
        high=0.30,
        very_high=0.80,
    )

    MOMENTUM = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    ENTROPY = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    COMPRESSION = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    BALANCE = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    VOLATILITY = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    # ==========================================================
    # ANALYTICAL METRICS
    # ==========================================================

    CONFIDENCE = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    STABILITY = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    NOISE = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    PATTERN_STRENGTH = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )

    TRANSITION_SCORE = ThresholdRange(
        very_low=0.20,
        low=0.40,
        moderate=0.60,
        high=0.80,
        very_high=1.00,
    )
