"""
Space AI 2.0

Decision Engine Exceptions

Custom exception hierarchy used throughout the Decision
Engine.

Every exception defined by this module inherits from
DecisionEngineError.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations


class DecisionEngineError(Exception):
    """
    Base exception for the Decision Engine.
    """


class StrategyNotFoundError(DecisionEngineError):
    """
    Raised when the requested Decision Strategy
    is not supported.
    """


class RuleEvaluationError(DecisionEngineError):
    """
    Raised when a decision rule cannot be evaluated.
    """


class InvalidDecisionContextError(DecisionEngineError):
    """
    Raised when an invalid DecisionContext is supplied.
    """


__all__ = [
    "DecisionEngineError",
    "InvalidDecisionContextError",
    "RuleEvaluationError",
    "StrategyNotFoundError",
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
