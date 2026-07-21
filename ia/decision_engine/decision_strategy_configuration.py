"""
Space AI 2.0

Decision Strategy Configuration

Immutable Value Object containing the configuration
required to instantiate a Decision Strategy.

The configuration encapsulates every parameter needed by
the StrategyFactory while keeping the Decision Engine
independent from concrete strategy implementations.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from collections.abc import Sequence
from dataclasses import dataclass

# ============================================================================
# Space AI - Same Package
# ============================================================================
from .rules.base_rule import BaseRule
from .strategies.strategy_type import DecisionStrategyType


@dataclass(
    frozen=True,
    slots=True,
)
class DecisionStrategyConfiguration:
    """
    Immutable configuration used by the StrategyFactory.

    Attributes
    ----------
    strategy_type:
        Strategy implementation to instantiate.

    rules:
        Ordered collection of decision rules.
    """

    strategy_type: DecisionStrategyType

    rules: Sequence[BaseRule]

    def __post_init__(self) -> None:
        """
        Ensure the rule collection is immutable.
        """
        object.__setattr__(
            self,
            "rules",
            tuple(self.rules),
        )


__all__ = [
    "DecisionStrategyConfiguration",
]

# ---------------------------------------------------------------------
# Estado:
# APROBADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
