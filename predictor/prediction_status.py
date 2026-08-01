"""
Space AI 2.0

Prediction Status

Represents the execution state of a prediction.
"""

from __future__ import annotations

from enum import StrEnum


class PredictionStatus(StrEnum):
    """
    Prediction lifecycle status.
    """

    READY = "ready"

    WARMUP = "warmup"

    UNAVAILABLE = "unavailable"


__all__ = [
    "PredictionStatus",
]
