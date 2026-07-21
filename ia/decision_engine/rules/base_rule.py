"""
Space AI 2.0

Base Rule

Defines the abstract contract implemented by every
Decision Rule.

A rule evaluates a DecisionContext and produces a
RuleResult.

Rules never create Decisions directly.

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
from ..decision_context import DecisionContext
from ..rule_result import RuleResult


class BaseRule(ABC):
    """
    Abstract base class for every Decision Rule.
    """

    @abstractmethod
    def evaluate(
        self,
        context: DecisionContext,
    ) -> RuleResult:
        """
        Evaluate a DecisionContext.

        Parameters
        ----------
        context:
            Immutable decision context.

        Returns
        -------
        RuleResult
            Result produced by the rule.
        """
        ...


__all__ = [
    "BaseRule",
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
