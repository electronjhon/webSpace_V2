"""
Space AI 2.0

Prediction Result

Immutable result produced by the Predictor Engine.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.prediction import Prediction
from predictor.prediction_status import PredictionStatus


@dataclass(
    frozen=True,
    slots=True,
)
class PredictionResult:
    """
    Immutable result produced by the Predictor Engine.

    This object represents the complete outcome of a
    prediction attempt, including successful predictions
    and warm-up situations.
    """

    status: PredictionStatus

    prediction: Prediction | None = None

    reason: str | None = None


__all__ = [
    "PredictionResult",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# NO
#
# Versión:
# 2.0.0
# ---------------------------------------------------------------------
