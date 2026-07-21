"""
Space AI 2.0
------------

Decision Engine - Enumerations

Define todas las enumeraciones utilizadas por el Decision Engine.

Principios de diseño
--------------------
- Uso de StrEnum para facilitar serialización y logging.
- Compatible con Python 3.13.5.
- Sin dependencias del resto del módulo.
- Archivo estable (no debe modificarse salvo decisión arquitectónica).
"""

from __future__ import annotations

from enum import StrEnum, auto


class DecisionAction(StrEnum):
    """
    Acción final generada por el Decision Engine.
    """

    BUY = auto()
    SELL = auto()
    HOLD = auto()
    EXIT = auto()


class ConfidenceLevel(StrEnum):
    """
    Clasificación cualitativa de la confianza de una decisión.

    La conversión desde un valor numérico se realizará en confidence.py.
    """

    VERY_LOW = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    VERY_HIGH = auto()


class DecisionSource(StrEnum):
    """
    Origen de la decisión generada.
    """

    RULE_ENGINE = auto()
    ENSEMBLE = auto()
    HYBRID = auto()
    MANUAL = auto()


class EnsembleMethod(StrEnum):
    """
    Estrategias soportadas para combinar múltiples predicciones.
    """

    MAJORITY_VOTE = auto()
    WEIGHTED_VOTE = auto()
    SOFT_VOTING = auto()
    HARD_VOTING = auto()
    STACKING = auto()


class MarketBias(StrEnum):
    """
    Dirección predominante estimada por el mercado.
    """

    BULLISH = auto()
    BEARISH = auto()
    SIDEWAYS = auto()
    UNKNOWN = auto()


class RiskLevel(StrEnum):
    """
    Nivel de riesgo asociado a una decisión.
    """

    VERY_LOW = auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    VERY_HIGH = auto()


class SignalStrength(StrEnum):
    """
    Intensidad de la señal generada.
    """

    VERY_WEAK = auto()
    WEAK = auto()
    MODERATE = auto()
    STRONG = auto()
    VERY_STRONG = auto()


class RuleEvaluation(StrEnum):
    """
    Resultado de evaluar una regla individual.
    """

    PASSED = auto()
    FAILED = auto()
    SKIPPED = auto()


class DecisionStatus(StrEnum):
    """
    Estado interno del proceso de decisión.
    """

    PENDING = auto()
    GENERATED = auto()
    REJECTED = auto()
    INVALID = auto()


class DecisionPriority(StrEnum):
    """
    Prioridad utilizada cuando múltiples reglas generan decisiones
    simultáneamente.
    """

    LOW = auto()
    NORMAL = auto()
    HIGH = auto()
    CRITICAL = auto()


class ConfidenceSource(StrEnum):
    """
    Componentes que participan en el cálculo de confianza.
    """

    PREDICTOR = auto()
    ENSEMBLE = auto()
    MARKET_STATE = auto()
    FEATURE_QUALITY = auto()
    VOLATILITY = auto()
    LIQUIDITY = auto()


__all__ = [
    "ConfidenceLevel",
    "ConfidenceSource",
    "DecisionAction",
    "DecisionPriority",
    "DecisionSource",
    "DecisionStatus",
    "EnsembleMethod",
    "MarketBias",
    "RiskLevel",
    "RuleEvaluation",
    "SignalStrength",
]
