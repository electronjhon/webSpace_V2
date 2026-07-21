"""
Space AI 2.0

Rule Engine

Domain service responsible for executing decision rules.

The RuleEngine evaluates every configured rule against
a DecisionContext and returns an immutable collection of
RuleResult objects.

The RuleEngine never interprets rule results nor builds
Decision objects.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from collections.abc import Sequence

# ============================================================================
# Space AI - Same Package
# ============================================================================
from .decision_context import DecisionContext
from .rule_result import RuleResult
from .rules.base_rule import BaseRule


class RuleEngine:
    """
    Executes a collection of decision rules.
    """

    def __init__(
        self,
        rules: Sequence[BaseRule],
    ) -> None:
        """
        Initialize the Rule Engine.

        Parameters
        ----------
        rules:
            Ordered collection of decision rules.
        """

        self._rules: tuple[BaseRule, ...] = tuple(rules)

    def evaluate(
        self,
        context: DecisionContext,
    ) -> tuple[RuleResult, ...]:
        """
        Evaluate every configured rule.

        Parameters
        ----------
        context:
            Immutable DecisionContext.

        Returns
        -------
        tuple[RuleResult, ...]
            Immutable collection of rule results.
        """

        return tuple(rule.evaluate(context) for rule in self._rules)


__all__ = [
    "RuleEngine",
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
