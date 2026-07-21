"""
Space AI 2.0

Application Configuration

Immutable configuration for the application runtime.

This object centralizes every configurable parameter
required during application initialization.
"""

from __future__ import annotations

from dataclasses import dataclass

from predictor.strategies.strategy_type import StrategyType


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class ApplicationConfiguration:
    """
    Immutable application configuration.

    Attributes
    ----------
    cdp_url:
        Chrome DevTools Protocol endpoint.

    rolling_window_size:
        Number of observations used to build the
        rolling window.

    prediction_strategy:
        Default prediction strategy used by the
        Predictor Engine during application execution.
    """

    cdp_url: str

    rolling_window_size: int

    prediction_strategy: StrategyType = StrategyType.MARKOV


__all__ = [
    "ApplicationConfiguration",
]
