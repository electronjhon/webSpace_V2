from __future__ import annotations

from dataclasses import dataclass

from state_engine.state_labels import StateLabels


@dataclass(frozen=True, slots=True)
class ClassificationResult:
    """
    Immutable result produced by a state classifier.

    This value object encapsulates the semantic classification
    of a feature vector together with the confidence assigned
    to that classification.
    """

    labels: StateLabels

    confidence: float
