"""
Space AI 2.0

Signal Engine

Abstract base class for all Signal Engine strategies.

Every Signal strategy receives an immutable SignalContext
and produces an immutable SignalResult.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from abc import ABC, abstractmethod

# ============================================================================
# Space AI - Same Package
# ============================================================================
from ia.signal_engine.context import SignalContext
from ia.signal_engine.result import SignalResult


class BaseSignalStrategy(ABC):
    """
    Base class for all Signal Engine strategies.

    Concrete implementations are responsible for transforming
    a SignalContext into a SignalResult.
    """

    @abstractmethod
    def generate(
        self,
        context: SignalContext,
    ) -> SignalResult:
        """
        Generate a trading signal.

        Parameters
        ----------
        context:
            Immutable Signal Engine context.

        Returns
        -------
        SignalResult
            Immutable result produced by the strategy.
        """
        raise NotImplementedError


__all__ = [
    "BaseSignalStrategy",
]
