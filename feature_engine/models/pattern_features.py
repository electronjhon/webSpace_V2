"""
Space AI 2.0

Pattern Features Model

Immutable data transfer object containing the
pattern-related features extracted from a rolling window.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class PatternFeatures:
    """
    Pattern-related metrics extracted from
    a rolling window.

    All values are computed by the
    PatternExtractor.
    """

    entropy: float

    compression: float

    spike_score: float

    pattern_strength: float
