"""
Space AI 2.0

Transition Extractor

Extracts transition-related metrics from a rolling window.
"""

from __future__ import annotations

from core.types import Number
from core.windows import RollingWindow
from feature_engine.extractors.base_extractor import BaseExtractor
from feature_engine.models.transition_features import TransitionFeatures


class TransitionExtractor(
    BaseExtractor[TransitionFeatures],
):
    """
    Extracts transition-related features from a rolling window.

    All returned metrics are normalized to the range [0.0, 1.0].
    """

    @classmethod
    def extract(
        cls,
        window: RollingWindow[Number],
    ) -> TransitionFeatures:
        """
        Extracts transition-related metrics.

        Args:
            window:
                Source rolling window.

        Returns:
            TransitionFeatures.
        """

        values = cls.values(window)

        transition_count = cls._transition_count(values)
        total_transitions = max(len(values) - 1, 1)

        transition_score = transition_count / total_transitions
        repeat_probability = 1.0 - transition_score
        alternation_probability = transition_score

        return TransitionFeatures(
            transition_score=transition_score,
            repeat_probability=repeat_probability,
            alternation_probability=alternation_probability,
        )

    @staticmethod
    def _transition_count(
        values: tuple[Number, ...],
    ) -> int:
        """
        Counts value transitions between consecutive samples.

        Args:
            values:
                Immutable window snapshot.

        Returns:
            Number of detected transitions.
        """

        if len(values) < 2:
            return 0

        transitions = 0

        previous = values[0]

        for current in values[1:]:
            if current != previous:
                transitions += 1

            previous = current

        return transitions
