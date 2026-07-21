"""
Space AI 2.0

Signal Engine

Signal Validator.

Validates generated signals against the configured business
rules of the Signal Engine.

Sprint:
    7

Version:
    1.0.0
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from dataclasses import dataclass

# ============================================================================
# Space AI - Signal Engine
# ============================================================================
from ia.signal_engine.configuration import SignalConfiguration
from ia.signal_engine.enums import SignalType
from ia.signal_engine.value_objects.signal import Signal


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class ValidationResult:
    """
    Immutable validation result.
    """

    accepted: bool

    reason: str


class SignalValidator:
    """
    Validates Signal objects according to the configured
    Signal Engine rules.
    """

    @staticmethod
    def validate(
        signal: Signal,
        configuration: SignalConfiguration,
    ) -> ValidationResult:
        """
        Validate a generated signal.
        """

        if signal.confidence < configuration.minimum_confidence:
            return ValidationResult(
                accepted=False,
                reason="Confidence below configured threshold.",
            )

        if (
            signal.signal_type is SignalType.HOLD
            and not configuration.allow_hold_signals
        ):
            return ValidationResult(
                accepted=False,
                reason="HOLD signals are disabled.",
            )

        return ValidationResult(
            accepted=True,
            reason="Signal accepted.",
        )


__all__ = [
    "SignalValidator",
    "ValidationResult",
]
