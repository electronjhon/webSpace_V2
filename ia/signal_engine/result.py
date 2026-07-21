"""
Space AI 2.0

Signal Engine

Immutable result produced by the Signal Engine.

A SignalResult represents the outcome of the signal generation
process. It may contain a generated Signal or indicate why no
signal was accepted.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from dataclasses import dataclass

# ============================================================================
# Space AI - Same Package
# ============================================================================
from ia.signal_engine.value_objects.signal import Signal


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class SignalResult:
    """
    Immutable result produced by the Signal Engine.

    Parameters
    ----------
    signal:
        Generated signal. None when no signal is produced.

    accepted:
        Indicates whether the signal has been accepted.

    reason:
        Human-readable explanation describing the result.
    """

    signal: Signal | None

    accepted: bool

    reason: str


__all__ = [
    "SignalResult",
]
