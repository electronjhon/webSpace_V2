"""
Space AI 2.0

Decision Strategy Type

Defines the supported strategy types for the
Decision Engine.

This enumeration is used by the Strategy Factory
to instantiate the appropriate decision strategy.
"""

from __future__ import annotations

from enum import StrEnum, auto


class DecisionStrategyType(StrEnum):
    """
    Supported Decision Engine strategies.
    """

    RULE_BASED = auto()

    CONSERVATIVE = auto()

    AGGRESSIVE = auto()

    CUSTOM = auto()


__all__ = [
    "DecisionStrategyType",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
