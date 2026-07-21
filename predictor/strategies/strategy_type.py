"""
Space AI 2.0

Strategy Type

Supported prediction strategies.
"""

from __future__ import annotations

from enum import StrEnum, unique


@unique
class StrategyType(StrEnum):
    """
    Supported prediction strategies.

    This enumeration identifies every prediction
    strategy officially supported by the
    Predictor Engine.
    """

    MARKOV = "markov"

    BAYESIAN = "bayesian"

    ENSEMBLE = "ensemble"


__all__ = [
    "StrategyType",
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
