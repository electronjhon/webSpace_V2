"""
Space AI 2.0

Signal Engine

Configuración oficial del Signal Engine.

Define los parámetros de configuración utilizados por el
motor y por las distintas estrategias de generación de
señales.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass

from ia.core.value_objects import Confidence
from ia.signal_engine.enums import SignalStrategyType


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class SignalConfiguration:
    """
    Configuración del Signal Engine.

    Attributes
    ----------
    strategy:
        Estrategia utilizada por el motor.

    minimum_confidence:
        Confianza mínima requerida para generar una señal.

    allow_hold_signals:
        Permite generar señales HOLD.

    allow_none_signals:
        Permite generar señales NONE.
    """

    strategy: SignalStrategyType = SignalStrategyType.RULE_BASED

    minimum_confidence: Confidence = Confidence.of(0.50)

    allow_hold_signals: bool = True

    allow_none_signals: bool = False
