"""
Space AI 2.0

Signal Engine

Default Rule-Based implementation of the Signal Engine.

Responsibilities
----------------
- Orchestrate the signal generation workflow.
- Delegate Decision → Signal conversion.
- Delegate signal validation.
- Produce an immutable SignalResult.

Sprint:
    7

Version:
    1.0.0
"""

from __future__ import annotations

# ============================================================================
# Space AI - Signal Engine
# ============================================================================
from ia.signal_engine.base import BaseSignalStrategy
from ia.signal_engine.context import SignalContext
from ia.signal_engine.mappers.decision_mapper import DecisionMapper
from ia.signal_engine.result import SignalResult
from ia.signal_engine.validators.signal_validator import SignalValidator


class RuleBasedSignalStrategy(BaseSignalStrategy):
    """
    Default implementation of the Signal Engine strategy.
    """

    def __init__(self) -> None:
        self._mapper = DecisionMapper()
        self._validator = SignalValidator()

    def generate(
        self,
        context: SignalContext,
    ) -> SignalResult:
        """
        Generate a SignalResult from the supplied context.
        """

        signal = self._mapper.to_signal(
            decision=context.decision,
            timestamp=context.timestamp,
        )

        validation = self._validator.validate(
            signal=signal,
            configuration=context.configuration,
        )

        return SignalResult(
            signal=signal if validation.accepted else None,
            accepted=validation.accepted,
            reason=validation.reason,
        )


__all__ = [
    "RuleBasedSignalStrategy",
]
