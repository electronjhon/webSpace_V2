"""
Space AI 2.0

State Engine Result

Immutable result produced by the State Engine.

This object groups the generated ClassificationResult
together with the updated StateHistory.

Compatible with:
    - Python 3.13.5
    - Ruff
    - Black
    - isort
    - MyPy (strict)
"""

from __future__ import annotations

from dataclasses import dataclass

from state_engine.models.classification_result import (
    ClassificationResult,
)
from state_engine.state_history import StateHistory


@dataclass(
    frozen=True,
    slots=True,
)
class StateEngineResult:
    """
    Immutable result returned by the State Engine.

    Attributes
    ----------
    classification:
        Semantic classification produced from the current
        FeatureVector.

    history:
        Updated immutable StateHistory.
    """

    classification: ClassificationResult

    history: StateHistory


__all__ = [
    "StateEngineResult",
]
