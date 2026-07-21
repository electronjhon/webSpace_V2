"""
Space AI 2.0

State History

Immutable history of the state evolution.

The history acts as the aggregate root for all
State and StateTransition instances created by
the StateEngine.
"""

from __future__ import annotations

from dataclasses import dataclass

from state_engine.state import State
from state_engine.state_transition import StateTransition


@dataclass(
    frozen=True,
    slots=True,
)
class StateHistory:
    """
    Immutable aggregate containing every generated
    State and StateTransition.

    This object contains no business logic.

    New histories are always produced by the
    StateMachine.
    """

    states: tuple[State, ...] = ()

    transitions: tuple[StateTransition, ...] = ()

    def is_empty(self) -> bool:
        """
        Determine whether the history contains states.

        Returns
        -------
        bool
            True when the history is empty.
        """

        return not self.states

    def last(self) -> State | None:
        """
        Return the most recent state.

        Returns
        -------
        State | None
            Last generated state or None if the
            history is empty.
        """

        if self.is_empty():
            return None

        return self.states[-1]

    def last_transition(self) -> StateTransition | None:
        """
        Return the most recent transition.

        Returns
        -------
        StateTransition | None
            Last generated transition or None if
            no transitions exist.
        """

        if not self.transitions:
            return None

        return self.transitions[-1]


__all__ = [
    "StateHistory",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.1.0
# ---------------------------------------------------------------------
