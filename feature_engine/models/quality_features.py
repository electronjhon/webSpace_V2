"""
Space AI 2.0

Quality Features Model

Immutable data transfer object describing
the quality of the extracted feature set.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class QualityFeatures:
    """
    Quality-related features describing the reliability and
    stability of the analyzed sequence.
    """

    confidence: float

    stability: float

    noise: float

    balance: float

    volatility: float
