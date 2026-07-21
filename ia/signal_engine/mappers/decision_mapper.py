"""
Space AI 2.0

Signal Engine

Decision Mapper.

Transforms immutable Decision objects into immutable Signal
objects.

The mapper is responsible only for translating concepts
between the Decision Engine and the Signal Engine.

Sprint:
    7

Version:
    1.0.0
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from datetime import datetime

# ============================================================================
# Space AI - Decision Engine
# ============================================================================
from ia.decision_engine.decision import Decision
from ia.decision_engine.enums import DecisionAction

# ============================================================================
# Space AI - Signal Engine
# ============================================================================
from ia.signal_engine.enums import (
    SignalDirection,
    SignalSource,
    SignalType,
)
from ia.signal_engine.exceptions import InvalidSignalError
from ia.signal_engine.value_objects.signal import Signal


class DecisionMapper:
    """
    Maps Decision objects into Signal objects.

    This class centralizes every translation rule between
    the Decision Engine and the Signal Engine.
    """

    @classmethod
    def to_signal(
        cls,
        decision: Decision,
        timestamp: datetime,
    ) -> Signal:
        """
        Convert a Decision into a Signal.
        """

        return Signal(
            signal_type=cls._signal_type(decision.action),
            direction=cls._signal_direction(decision.action),
            confidence=decision.confidence,
            source=SignalSource.RULE_ENGINE,
            timestamp=timestamp,
        )

    @staticmethod
    def _signal_type(
        action: DecisionAction,
    ) -> SignalType:
        """
        Translate a DecisionAction into a SignalType.
        """

        match action:
            case DecisionAction.BUY:
                return SignalType.ENTRY

            case DecisionAction.SELL:
                return SignalType.ENTRY

            case DecisionAction.HOLD:
                return SignalType.HOLD

            case DecisionAction.EXIT:
                return SignalType.EXIT

        raise InvalidSignalError(f"Unsupported DecisionAction: {action!r}.")

    @staticmethod
    def _signal_direction(
        action: DecisionAction,
    ) -> SignalDirection:
        """
        Translate a DecisionAction into a SignalDirection.
        """

        match action:
            case DecisionAction.BUY:
                return SignalDirection.LONG

            case DecisionAction.SELL:
                return SignalDirection.SHORT

            case DecisionAction.HOLD:
                return SignalDirection.NEUTRAL

            case DecisionAction.EXIT:
                return SignalDirection.NEUTRAL

        raise InvalidSignalError(f"Unsupported DecisionAction: {action!r}.")


__all__ = [
    "DecisionMapper",
]
