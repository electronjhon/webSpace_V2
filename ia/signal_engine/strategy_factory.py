"""
Space AI 2.0

Signal Engine

Strategy Factory.

Creates Signal Engine strategies from the configured
SignalStrategyType.

Sprint:
    7

Version:
    1.0.0
"""

from __future__ import annotations

# ============================================================================
# Space AI - Signal Engine
# ============================================================================
from ia.signal_engine.base import BaseSignalStrategy
from ia.signal_engine.enums import SignalStrategyType
from ia.signal_engine.exceptions import UnsupportedSignalStrategyError
from ia.signal_engine.strategies.rule_based_strategy import (
    RuleBasedSignalStrategy,
)


class StrategyFactory:
    """
    Factory responsible for creating Signal Engine strategies.
    """

    _STRATEGIES: dict[
        SignalStrategyType,
        type[BaseSignalStrategy],
    ] = {
        SignalStrategyType.RULE_BASED: RuleBasedSignalStrategy,
    }

    @classmethod
    def create(
        cls,
        strategy: SignalStrategyType,
    ) -> BaseSignalStrategy:
        """
        Create a Signal strategy.

        Parameters
        ----------
        strategy:
            Strategy to instantiate.

        Returns
        -------
        BaseSignalStrategy
            Strategy instance.

        Raises
        ------
        UnsupportedSignalStrategyError
            If the strategy is not registered.
        """

        strategy_class = cls._STRATEGIES.get(strategy)

        if strategy_class is None:
            raise UnsupportedSignalStrategyError(
                f"Unsupported Signal strategy: {strategy.value}"
            )

        return strategy_class()

    @classmethod
    def register(
        cls,
        strategy: SignalStrategyType,
        implementation: type[BaseSignalStrategy],
    ) -> None:
        """
        Register or replace a strategy implementation.

        This method is primarily intended for testing or
        controlled extensions of the Signal Engine.
        """

        cls._STRATEGIES[strategy] = implementation


__all__ = [
    "StrategyFactory",
]
