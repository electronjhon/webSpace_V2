"""
Space AI 2.0

Analytics

Advanced analytical algorithms for sequence analysis.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from math import log2

from core.statistics import Statistics
from core.types import Number
from core.validator import Validator


class Analytics:
    """
    Advanced sequence analysis algorithms.
    """

    @staticmethod
    def entropy(
        values: Sequence[Number],
    ) -> float:
        """
        Calculates the Shannon entropy.
        """

        Validator.validate_numeric_sequence(values)

        total = len(values)

        frequencies = Counter(values)

        entropy = 0.0

        for count in frequencies.values():
            probability = count / total

            entropy -= probability * log2(probability)

        return entropy

    @staticmethod
    def compression(
        values: Sequence[Number],
    ) -> float:
        """
        Calculates the compression ratio.
        """

        Validator.validate_numeric_sequence(values)

        total = len(values)

        if total == 1:
            return 1.0

        unique = len(set(values))

        return 1.0 - ((unique - 1) / (total - 1))

    @staticmethod
    def spike_score(
        values: Sequence[Number],
    ) -> float:
        """
        Calculates the largest normalized jump.
        """

        Validator.validate_numeric_sequence(values)

        if len(values) < 2:
            return 0.0

        maximum_jump = max(
            abs(float(values[i]) - float(values[i - 1])) for i in range(1, len(values))
        )

        deviation = Statistics.standard_deviation(values)

        if deviation == 0.0:
            return 0.0

        return maximum_jump / deviation

    @staticmethod
    def coefficient_of_variation(
        values: Sequence[Number],
    ) -> float:
        """
        Calculates the coefficient of variation.

        Returns:
            Standard deviation divided by the
            absolute mean.

        If the mean is zero, returns 0.0.
        """

        Validator.validate_numeric_sequence(values)

        mean = abs(
            Statistics.mean(values),
        )

        if mean == 0.0:
            return 0.0

        return Statistics.standard_deviation(values) / mean

    @staticmethod
    def pattern_strength(
        values: Sequence[Number],
    ) -> float:
        """
        Combines entropy, compression and spike
        activity into a normalized score.
        """

        Validator.validate_numeric_sequence(values)

        entropy = Analytics.entropy(values)

        compression = Analytics.compression(values)

        spike = Analytics.spike_score(values)

        maximum_entropy = log2(len(set(values)))

        if maximum_entropy == 0.0:
            entropy_factor = 1.0
        else:
            entropy_factor = 1.0 - entropy / maximum_entropy

        spike_factor = 1.0 / (1.0 + spike)

        strength = (entropy_factor + compression + spike_factor) / 3.0

        return max(
            0.0,
            min(1.0, strength),
        )

    @staticmethod
    def confidence(
        values: Sequence[Number],
    ) -> float:
        """
        Estimates the confidence of the sequence.

        High confidence is associated with
        strong patterns.
        """

        Validator.validate_numeric_sequence(values)

        return Analytics.pattern_strength(values)

    @staticmethod
    def stability(
        values: Sequence[Number],
    ) -> float:
        """
        Estimates temporal stability.

        Stable sequences exhibit
        low variance.
        """

        Validator.validate_numeric_sequence(values)

        coefficient = Analytics.coefficient_of_variation(
            values,
        )

        return 1.0 / (1.0 + coefficient)

    @staticmethod
    def noise_level(
        values: Sequence[Number],
    ) -> float:
        """
        Estimates sequence noise.

        Noise is considered the inverse
        of temporal stability.

        Returns:
            Value normalized to [0,1].
        """

        Validator.validate_numeric_sequence(values)

        return 1.0 - Analytics.stability(values)
