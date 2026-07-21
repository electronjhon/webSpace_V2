"""
Space AI 2.0

Core - Value Objects

Clase base para todos los Value Objects numéricos del dominio.

Responsabilidades
-----------------
- Garantizar la inmutabilidad.
- Validar el rango permitido.
- Implementar comparaciones.
- Proporcionar conversiones controladas.
- Evitar duplicación entre Confidence, Probability,
  Percentage, Score, Weight y futuros Value Objects.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from functools import total_ordering
from typing import Self

from ia.core.exceptions import ValueObjectValidationError
from ia.core.value_objects.value_object import ValueObject

type NumericInput = Decimal | int | float | str


@total_ordering
@dataclass(frozen=True, slots=True, kw_only=True)
class NumericValueObject(ValueObject):
    """
    Clase base para todos los Value Objects numéricos.

    Las clases derivadas únicamente deben definir el rango
    permitido mediante ``valid_range()``.
    """

    value: Decimal

    @classmethod
    def of(cls, value: NumericInput) -> Self:
        """
        Construye un Value Object a partir de un valor numérico.

        El valor recibido es normalizado a Decimal antes de
        crear la instancia.
        """

        try:
            decimal_value = value if isinstance(value, Decimal) else Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise ValueObjectValidationError(
                f"Valor numérico inválido: {value!r}."
            ) from exc

        return cls(value=decimal_value)

    def __post_init__(self) -> None:
        """
        Valida las invariantes comunes del dominio.

        El método oficial de construcción es ``of()``. Por tanto,
        se asume que ``value`` ya ha sido normalizado a ``Decimal``.
        """

        self._validate()

    def _validate(self) -> None:
        """
        Valida las invariantes comunes del dominio.
        """

        minimum, maximum = self.valid_range()

        if not minimum <= self.value <= maximum:
            raise ValueObjectValidationError(
                f"{type(self).__name__} debe estar "
                f"entre {minimum} y {maximum}. "
                f"Valor recibido: {self.value}."
            )

    @classmethod
    @abstractmethod
    def valid_range(cls) -> tuple[Decimal, Decimal]:
        """
        Devuelve el rango permitido para el Value Object.
        """

    def __eq__(self, other: object) -> bool:
        """
        Compara igualdad entre objetos del mismo tipo.
        """

        if type(self) is not type(other):
            return NotImplemented

        return self.value == other.value

    def __lt__(self, other: object) -> bool:
        """
        Compara dos objetos del mismo tipo.
        """

        if type(self) is not type(other):
            return NotImplemented

        return self.value < other.value

    def __float__(self) -> float:
        """
        Convierte el Value Object a float.
        """

        return float(self.value)

    def __int__(self) -> int:
        """
        Convierte el Value Object a int.
        """

        return int(self.value)

    def __str__(self) -> str:
        """
        Representación legible.
        """

        return str(self.value.normalize())

    def __repr__(self) -> str:
        """
        Representación para depuración.
        """

        return f"{type(self).__name__}({self})"
