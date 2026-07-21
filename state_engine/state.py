from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from state_engine.state_id import StateId
from state_engine.state_labels import StateLabels


@dataclass(frozen=True, slots=True)
class State:
    """
    Immutable domain entity representing the classification of the system
    at a specific point in time.

    A State contains no business logic. It is a snapshot produced by the
    StateClassifier and consumed by the StateMachine, Analytics and
    Predictor components.
    """

    id: StateId
    index: int
    timestamp: datetime
    labels: StateLabels
