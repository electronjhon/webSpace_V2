"""
Space AI 2.0

Signal Engine

Value Object que representa una señal del dominio.

Una Signal encapsula el resultado normalizado generado por el
Signal Engine. Está compuesta exclusivamente por Value Objects
y tipos propios del dominio.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from ia.core.value_objects import Confidence
from ia.signal_engine.enums import (
    SignalDirection,
    SignalSource,
    SignalType,
)
from ia.signal_engine.exceptions import InvalidSignalError


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class Signal:
    """
    Value Object que representa una señal del dominio.
    """

    signal_type: SignalType

    direction: SignalDirection

    confidence: Confidence

    source: SignalSource

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def __post_init__(self) -> None:
        """
        Valida las invariantes del dominio.
        """

        self._validate_timestamp()
        self._validate_signal_consistency()

    def _validate_timestamp(self) -> None:
        """
        Garantiza que el timestamp sea timezone-aware.
        """

        if self.timestamp.tzinfo is None:
            raise InvalidSignalError(
                "timestamp debe contener información de zona horaria."
            )

    def _validate_signal_consistency(self) -> None:
        """
        Valida las reglas del dominio.
        """

        if (
            self.signal_type is SignalType.HOLD
            and self.direction is not SignalDirection.NEUTRAL
        ):
            raise InvalidSignalError(
                "Una señal HOLD únicamente admite " "SignalDirection.NEUTRAL."
            )

        if (
            self.signal_type is SignalType.EXIT
            and self.direction is not SignalDirection.NEUTRAL
        ):
            raise InvalidSignalError(
                "Una señal EXIT únicamente admite " "SignalDirection.NEUTRAL."
            )


__all__ = [
    "Signal",
]
