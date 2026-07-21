"""
Space AI 2.0

Signal Engine

Immutable context consumed by Signal strategies.

The SignalContext encapsulates every dependency required
by a SignalStrategy in order to generate a Signal.

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
from datetime import datetime

# ============================================================================
# Space AI - Decision Engine
# ============================================================================
from ia.decision_engine.decision import Decision

# ============================================================================
# Space AI - Same Package
# ============================================================================
from ia.signal_engine.configuration import SignalConfiguration
from ia.signal_engine.exceptions import SignalContextError


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class SignalContext:
    """
    Immutable input consumed by Signal strategies.

    Parameters
    ----------
    decision:
        Final decision produced by the Decision Engine.

    configuration:
        Immutable Signal Engine configuration.

    timestamp:
        Evaluation timestamp.

    Notes
    -----
    The timestamp must always be timezone-aware.
    """

    decision: Decision

    configuration: SignalConfiguration

    timestamp: datetime

    def __post_init__(self) -> None:
        """
        Validate the context invariants.
        """

        self._validate_timestamp()

    def _validate_timestamp(self) -> None:
        """
        Ensure the timestamp is timezone-aware.
        """

        if self.timestamp.tzinfo is None:
            raise SignalContextError("The timestamp must be timezone-aware.")


__all__ = [
    "SignalContext",
]
