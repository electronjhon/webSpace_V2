"""
Space AI 2.0

State Machine

Stateless domain service responsible for creating immutable
state histories.
"""

from __future__ import annotations

from datetime import datetime

from state_engine.state import State
from state_engine.state_history import StateHistory
from state_engine.state_id import StateId
from state_engine.state_labels import StateLabels
from state_engine.state_transition import StateTransition


class StateMachine:
    """
    Stateless domain service responsible for creating immutable
    state histories.

    The StateMachine owns the lifecycle of State entities and
    StateTransition events while remaining completely unaware
    of how the state labels were obtained.
    """

    @classmethod
    def build(
        cls,
        history: StateHistory,
        labels: StateLabels,
        timestamp: datetime,
    ) -> StateHistory:
        """
        Builds a new immutable StateHistory.
        """

        current_state = cls._create_state(
            history=history,
            labels=labels,
            timestamp=timestamp,
        )

        states = history.states + (current_state,)
        transitions = history.transitions

        previous_state = cls._last_state(history)

        if previous_state is not None:
            transition = cls._create_transition(
                previous=previous_state,
                current=current_state,
                history=history,
                timestamp=timestamp,
            )

            transitions += (transition,)

        return StateHistory(
            states=states,
            transitions=transitions,
        )

    @classmethod
    def _create_state(
        cls,
        history: StateHistory,
        labels: StateLabels,
        timestamp: datetime,
    ) -> State:

        return State(
            id=StateId.generate(),
            index=cls._next_state_index(history),
            timestamp=timestamp,
            labels=labels,
        )

    @classmethod
    def _create_transition(
        cls,
        previous: State,
        current: State,
        history: StateHistory,
        timestamp: datetime,
    ) -> StateTransition:

        return StateTransition(
            from_state=previous,
            to_state=current,
            transition_index=cls._next_transition_index(history),
            timestamp=timestamp,
        )

    @staticmethod
    def _last_state(
        history: StateHistory,
    ) -> State | None:

        if not history.states:
            return None

        return history.states[-1]

    @staticmethod
    def _last_transition(
        history: StateHistory,
    ) -> StateTransition | None:

        if not history.transitions:
            return None

        return history.transitions[-1]

    @classmethod
    def _next_state_index(
        cls,
        history: StateHistory,
    ) -> int:

        last = cls._last_state(history)

        return 0 if last is None else last.index + 1

    @classmethod
    def _next_transition_index(
        cls,
        history: StateHistory,
    ) -> int:

        last = cls._last_transition(history)

        return 0 if last is None else last.transition_index + 1
