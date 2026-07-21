"""
Space AI 2.0

Signal Engine

Main orchestrator of the Signal Engine.

The engine coordinates the signal generation workflow by
selecting the configured strategy and delegating the
generation process.

Sprint:
    7

Version:
    1.0.0
"""

from __future__ import annotations

# ============================================================================
# Space AI - Signal Engine
# ============================================================================
from ia.signal_engine.context import SignalContext
from ia.signal_engine.result import SignalResult
from ia.signal_engine.strategy_factory import StrategyFactory


class SignalEngine:
    """
    Main Signal Engine orchestrator.

    The engine is intentionally stateless. Every execution
    selects the appropriate strategy according to the supplied
    configuration.
    """

    def generate(
        self,
        context: SignalContext,
    ) -> SignalResult:
        """
        Generate a signal.

        Parameters
        ----------
        context:
            Immutable Signal Engine context.

        Returns
        -------
        SignalResult
            Result produced by the configured strategy.
        """

        strategy = StrategyFactory.create(
            context.configuration.strategy,
        )

        return strategy.generate(context)


__all__ = [
    "SignalEngine",
]
