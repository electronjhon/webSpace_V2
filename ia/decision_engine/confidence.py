"""
Space AI 2.0

Decision Confidence Service

Domain service responsible for calculating the confidence
associated with a Decision.

The service evaluates the RuleResult objects produced by
the RuleEngine and returns a single immutable Confidence
instance.

Compatible with:
    - Python 3.13.5
    - Ruff
    - MyPy (strict)
"""

from __future__ import annotations

# ============================================================================
# Standard Library
# ============================================================================
from collections.abc import Iterable

# ============================================================================
# Space AI - Other Engines
# ============================================================================
from ia.core.value_objects import Confidence

# ============================================================================
# Space AI - Same Package
# ============================================================================
from .rule_result import RuleResult


class ConfidenceService:
    """
    Calculates the confidence of a Decision.
    """

    @staticmethod
    def calculate(
        results: Iterable[RuleResult],
    ) -> Confidence:
        """
        Calculate the confidence associated with a
        collection of RuleResult objects.

        Parameters
        ----------
        results:
            Rule results produced by the RuleEngine.

        Returns
        -------
        Confidence
            Final confidence associated with the Decision.
        """

        best_confidence = max(
            (result.confidence.value for result in results if result.passed),
            default=0.0,
        )

        return Confidence.of(best_confidence)


__all__ = [
    "ConfidenceService",
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
