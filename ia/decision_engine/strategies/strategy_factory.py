"""
Space AI 2.0

Decision Strategy Factory

Factory responsible for creating Decision Strategy
instances from an immutable configuration.

The factory contains no business logic and only
instantiates strategy implementations.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Space AI - Same Package
# ============================================================================
from ..decision_strategy_configuration import (
    DecisionStrategyConfiguration,
)
from ..exceptions import StrategyNotFoundError
from .base_decision_strategy import BaseDecisionStrategy
from .rule_based_strategy import RuleBasedStrategy
from .strategy_type import DecisionStrategyType


class StrategyFactory:
    """
    Factory responsible for creating Decision Strategy
    implementations.
    """

    def create(
        self,
        configuration: DecisionStrategyConfiguration,
    ) -> BaseDecisionStrategy:
        """
        Create the configured Decision Strategy.

        Parameters
        ----------
        configuration:
            Immutable strategy configuration.

        Returns
        -------
        BaseDecisionStrategy
            Configured strategy implementation.

        Raises
        ------
        StrategyNotFoundError
            If the requested strategy is not supported.
        """

        match configuration.strategy_type:
            case DecisionStrategyType.RULE_BASED:
                return RuleBasedStrategy(configuration)

            case _:
                raise StrategyNotFoundError(
                    f"Unsupported Decision Strategy: {configuration.strategy_type!s}"
                )


__all__ = [
    "StrategyFactory",
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
