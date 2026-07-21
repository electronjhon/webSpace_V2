from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from state_engine.state import State


@dataclass(frozen=True, slots=True)
class StateTransition:
    """
    Immutable domain event representing the transition from one state
    to another.

    A transition captures the evolution of the system between two
    consecutive states without embedding any business logic.
    """

    from_state: State
    to_state: State
    transition_index: int
    timestamp: datetime
