"""
Space AI 2.0

Rule Based Strategy

Default implementation of the Decision Engine.

This strategy evaluates the configured rules using the
RuleEngine, calculates the overall confidence through the
ConfidenceService and produces the final immutable Decision.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from collections.abc import Collection

# ============================================================================
# Space AI - Same Package
# ============================================================================
from ..confidence import ConfidenceService
from ..decision import Decision
from ..decision_context import DecisionContext
from ..decision_strategy_configuration import (
    DecisionStrategyConfiguration,
)
from ..enums import DecisionAction
from ..rule_engine import RuleEngine
from ..rule_result import RuleResult
from .base_decision_strategy import BaseDecisionStrategy


class RuleBasedStrategy(BaseDecisionStrategy):
    """
    Default rule-based implementation of the Decision Engine.
    """

    def __init__(
        self,
        configuration: DecisionStrategyConfiguration,
    ) -> None:
        """
        Initialize the strategy.
        """

        self._rule_engine = RuleEngine(
            configuration.rules,
        )

        self._confidence_service = ConfidenceService()

    def decide(
        self,
        context: DecisionContext,
    ) -> Decision:
        """
        Produce a Decision from the supplied DecisionContext.
        """

        results = self._rule_engine.evaluate(context)

        confidence = self._confidence_service.calculate(results)

        best_result = self._select_best_result(results)

        if best_result is None:
            return Decision(
                action=DecisionAction.HOLD,
                confidence=confidence,
                reason="No decision rule was satisfied.",
            )

        return Decision(
            action=best_result.action,
            confidence=confidence,
            reason=best_result.reason,
        )

    @staticmethod
    def _select_best_result(
        results: Collection[RuleResult],
    ) -> RuleResult | None:
        """
        Select the successful rule with the highest
        confidence.

        Returns
        -------
        RuleResult | None
            Best successful rule or None if no rule passed.
        """

        valid_results = (result for result in results if result.passed)

        return max(
            valid_results,
            key=lambda result: result.confidence.value,
            default=None,
        )


__all__ = [
    "RuleBasedStrategy",
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
