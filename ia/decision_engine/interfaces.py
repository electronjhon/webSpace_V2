"""
Space AI 2.0

Decision Engine Interfaces

Public protocols used throughout the Decision Engine.

Protocols define behavioural contracts while concrete
implementations are provided by abstract base classes
and services.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from typing import Protocol

# ============================================================================
# Space AI - Same Package
# ============================================================================
from .decision import Decision
from .decision_context import DecisionContext
from .rule_result import RuleResult


class DecisionStrategy(Protocol):
    """
    Protocol implemented by every Decision Strategy.
    """

    def decide(
        self,
        context: DecisionContext,
    ) -> Decision:
        """
        Produce an immutable Decision.
        """
        ...


class DecisionRule(Protocol):
    """
    Protocol implemented by every decision rule.
    """

    def evaluate(
        self,
        context: DecisionContext,
    ) -> RuleResult:
        """
        Evaluate a DecisionContext.
        """
        ...


__all__ = [
    "DecisionRule",
    "DecisionStrategy",
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
