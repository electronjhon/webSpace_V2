"""
Space AI 2.0

Decision Engine

Facade responsible for generating immutable Decision
objects from a DecisionContext.

The DecisionEngine coordinates the configured Decision
Strategy without containing business logic.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Space AI - Same Package
# ============================================================================
from .decision import Decision
from .decision_context import DecisionContext
from .decision_strategy_configuration import (
    DecisionStrategyConfiguration,
)
from .strategies.strategy_factory import StrategyFactory


class DecisionEngine:
    """
    Facade for the Decision Engine.
    """

    def __init__(
        self,
        configuration: DecisionStrategyConfiguration,
    ) -> None:
        """
        Initialize the Decision Engine.

        Parameters
        ----------
        configuration:
            Immutable strategy configuration.
        """

        self._strategy = StrategyFactory().create(
            configuration,
        )

    def decide(
        self,
        context: DecisionContext,
    ) -> Decision:
        """
        Produce a Decision.

        Parameters
        ----------
        context:
            Immutable DecisionContext.

        Returns
        -------
        Decision
            Final immutable decision.
        """

        return self._strategy.decide(context)


__all__ = [
    "DecisionEngine",
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
