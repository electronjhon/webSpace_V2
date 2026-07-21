"""
Space AI 2.0

Strategy Factory

Factory responsible for creating prediction
strategy instances.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from predictor.strategies.base_strategy import BaseStrategy
from predictor.strategies.bayesian_strategy import BayesianStrategy
from predictor.strategies.ensemble_strategy import EnsembleStrategy
from predictor.strategies.markov_strategy import MarkovStrategy
from predictor.strategies.strategy_type import StrategyType


class StrategyFactory:
    """
    Factory responsible for creating prediction
    strategy instances.

    The factory provides a single entry point for
    obtaining prediction strategies without exposing
    their concrete implementations to the
    PredictorEngine.
    """

    _STRATEGIES: Final[
        Mapping[
            StrategyType,
            type[BaseStrategy],
        ]
    ] = MappingProxyType(
        {
            StrategyType.MARKOV: MarkovStrategy,
            StrategyType.BAYESIAN: BayesianStrategy,
            StrategyType.ENSEMBLE: EnsembleStrategy,
        }
    )

    @classmethod
    def create(
        cls,
        strategy_type: StrategyType,
    ) -> BaseStrategy:
        """
        Create a prediction strategy.

        Parameters
        ----------
        strategy_type:
            Requested prediction strategy.

        Returns
        -------
        BaseStrategy
            Instantiated prediction strategy.

        Raises
        ------
        ValueError
            If the requested strategy is not supported.
        """

        strategy_class = cls._STRATEGIES.get(strategy_type)

        if strategy_class is None:
            raise ValueError(f"Unsupported strategy: {strategy_type.value}")

        return strategy_class()


__all__ = [
    "StrategyFactory",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.1.0
# ---------------------------------------------------------------------
