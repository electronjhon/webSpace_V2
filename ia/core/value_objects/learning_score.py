"""
Space AI 2.0

Core - Value Objects

Implementación del Value Object LearningScore.

Representa la calidad obtenida por el sistema durante el
proceso de aprendizaje.

Un LearningScore siempre se encuentra comprendido entre
0.0 y 1.0 (inclusive), donde:

    0.0 -> Resultado completamente incorrecto.
    1.0 -> Resultado perfecto.

Internamente utiliza Decimal para garantizar precisión y
consistencia con el resto del dominio.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from ia.core.value_objects.numeric_value_object import (
    NumericValueObject,
)


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class LearningScore(NumericValueObject):
    """
    Value Object que representa una puntuación de aprendizaje.

    Este objeto encapsula la calidad obtenida por una
    predicción o decisión evaluada por el Learning Engine.
    """

    @classmethod
    def valid_range(cls) -> tuple[Decimal, Decimal]:
        """
        Devuelve el rango permitido para LearningScore.
        """

        return (
            Decimal("0.0"),
            Decimal("1.0"),
        )

    @property
    def is_zero(self) -> bool:
        """
        Indica si la puntuación es exactamente cero.
        """

        return self.value.is_zero()

    @property
    def is_perfect(self) -> bool:
        """
        Indica si la puntuación representa un resultado
        perfecto.
        """

        return self.value == Decimal("1.0")

    @property
    def percentage(self) -> Decimal:
        """
        Devuelve la puntuación expresada como porcentaje.
        """

        return self.value * Decimal("100")


__all__ = [
    "LearningScore",
]
