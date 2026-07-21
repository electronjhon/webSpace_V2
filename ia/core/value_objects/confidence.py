"""
Space AI 2.0

Core - Value Objects

Implementación del Value Object Confidence.

Representa un nivel de confianza del dominio con un rango
válido entre 0.0 y 1.0, utilizando Decimal como
representación interna para garantizar precisión.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ia.core.value_objects.numeric_value_object import NumericValueObject


@dataclass(frozen=True, slots=True, kw_only=True)
class Confidence(NumericValueObject):
    """
    Value Object que representa un nivel de confianza.

    Una instancia de Confidence siempre contiene un valor
    comprendido entre 0.0 y 1.0 (inclusive).
    """

    @classmethod
    def valid_range(cls) -> tuple[Decimal, Decimal]:
        """
        Devuelve el rango permitido para Confidence.
        """

        return (
            Decimal("0.0"),
            Decimal("1.0"),
        )

    @property
    def is_zero(self) -> bool:
        """
        Indica si la confianza es exactamente cero.
        """

        return self.value.is_zero()

    @property
    def is_full(self) -> bool:
        """
        Indica si la confianza representa certeza total.
        """

        return self.value == Decimal("1.0")

    @property
    def percentage(self) -> Decimal:
        """
        Devuelve la confianza expresada como porcentaje.
        """

        return self.value * Decimal("100")
