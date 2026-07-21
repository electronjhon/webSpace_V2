"""
Space AI 2.0

Signal Engine

Enumeraciones oficiales del dominio del Signal Engine.

Las enumeraciones definen los valores permitidos para la generación
de señales, evitando el uso de cadenas de texto distribuidas por
todo el proyecto y proporcionando tipado fuerte.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations

from enum import StrEnum


class SignalType(StrEnum):
    """
    Tipo general de señal generada por el Signal Engine.

    ENTRY:
        Apertura de una nueva posición.

    EXIT:
        Cierre de una posición existente.

    HOLD:
        Mantener la posición actual.
    """

    ENTRY = "ENTRY"
    EXIT = "EXIT"
    HOLD = "HOLD"


class SignalDirection(StrEnum):
    """
    Dirección operacional de la señal.
    """

    LONG = "LONG"
    SHORT = "SHORT"
    NEUTRAL = "NEUTRAL"


class SignalStatus(StrEnum):
    """
    Estado de validez de una señal.
    """

    VALID = "VALID"
    INVALID = "INVALID"
    FILTERED = "FILTERED"


class SignalSource(StrEnum):
    """
    Origen de la señal.

    Permite identificar qué componente produjo la señal.
    """

    RULE_ENGINE = "RULE_ENGINE"
    MANUAL = "MANUAL"
    UNKNOWN = "UNKNOWN"


class SignalStrategyType(StrEnum):
    """
    Estrategias soportadas por el Signal Engine.
    """

    RULE_BASED = "RULE_BASED"
    BAYESIAN = "BAYESIAN"
    MACHINE_LEARNING = "MACHINE_LEARNING"
    HYBRID = "HYBRID"
    ENSEMBLE = "ENSEMBLE"


__all__ = [
    "SignalDirection",
    "SignalSource",
    "SignalStatus",
    "SignalStrategyType",
    "SignalType",
]
