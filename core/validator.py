"""
Space AI 2.0

Core Validation Library

Biblioteca centralizada de validaciones reutilizable por todos los
componentes del sistema.

Responsabilidades:

- Validación de secuencias
- Validación de tipos
- Validación de rangos
- Validación de probabilidades
- Validación de porcentajes
- Validación de índices
- Validación de ventanas

Este módulo nunca modifica datos.

Únicamente valida y lanza excepciones cuando una condición
no es satisfecha.

Python 3.12
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite

from core.exceptions import ValidationError

Number = int | float


class Validator:
    """
    Biblioteca de validaciones.

    Todos los métodos son estáticos para evitar mantener estado y
    facilitar su reutilización desde cualquier módulo del sistema.
    """

    """----------Sequence Validation----------"""

    @staticmethod
    def validate_not_empty(
        sequence: Sequence[object],
    ) -> None:
        """
        Valida que una secuencia no esté vacía.

        Args:
            sequence:
                Secuencia.

        Raises:
            ValidationError:
                Si está vacía.
        """

        if len(sequence) == 0:
            raise ValidationError("Sequence cannot be empty.")

    @staticmethod
    def validate_numeric_sequence(
        values: Sequence[Number],
    ) -> None:
        """
        Validates a numeric sequence.

        Ensures that the sequence:

        - is not empty;
        - contains only numeric values;
        - does not contain booleans;
        - does not contain NaN values;
        - does not contain infinite values.

        Args:
            values:
                Sequence to validate.

        Raises:
            ValidationError:
                If the sequence is invalid.
        """

        Validator.validate_not_empty(values)

        for value in values:
            Validator.validate_numeric(value)

            Validator.validate_finite(value)

    @staticmethod
    def validate_length(
        sequence: Sequence[object],
        expected_length: int,
    ) -> None:
        """
        Valida una longitud exacta.
        """
        Validator.validate_not_empty(sequence)
        Validator.validate_integer(expected_length)

        if expected_length < 0:
            raise ValidationError("Expected length cannot be negative.")

        if len(sequence) != expected_length:
            raise ValidationError(
                f"Expected length {expected_length}, received {len(sequence)}."
            )

    @staticmethod
    def validate_min_length(
        sequence: Sequence[object],
        minimum_length: int,
    ) -> None:
        """
        Valida una longitud mínima.
        """
        Validator.validate_not_empty(sequence)
        Validator.validate_integer(minimum_length)

        if minimum_length < 0:
            raise ValidationError("Minimum length cannot be negative.")

        if len(sequence) < minimum_length:
            raise ValidationError(
                f"Minimum length is {minimum_length}, received {len(sequence)}."
            )

    @staticmethod
    def validate_max_length(
        sequence: Sequence[object],
        maximum_length: int,
    ) -> None:
        """
        Valida una longitud máxima.
        """
        Validator.validate_not_empty(sequence)
        Validator.validate_integer(maximum_length)

        if maximum_length < 1:
            raise ValidationError("Maximum length must be greater than zero.")

        if len(sequence) > maximum_length:
            raise ValidationError(
                f"Maximum length is {maximum_length}, received {len(sequence)}."
            )

    @staticmethod
    def validate_same_length(
        first: Sequence[object],
        second: Sequence[object],
    ) -> None:
        """
        Valida que dos secuencias tengan
        exactamente la misma longitud.

        Args:
            first:
                Primera secuencia.

            second:
                Segunda secuencia.

        Raises:
            ValidationError:
                Si las longitudes son distintas.
        """
        Validator.validate_not_empty(first)
        Validator.validate_not_empty(second)

        if len(first) != len(second):
            raise ValidationError("Sequences must have the same length.")

    """----------Type Validation----------"""

    @staticmethod
    def validate_not_none(
        value: object,
    ) -> None:
        """
        Valida que un valor no sea None.

        Args:
            value:
                Valor a validar.

        Raises:
            ValidationError:
                Si el valor es None.
        """

        if value is None:
            raise ValidationError("Value cannot be None.")

    @staticmethod
    def validate_numeric(
        value: object,
    ) -> None:
        """
        Valida que el valor sea numérico.

        Los valores booleanos no son considerados
        números válidos dentro de Space AI.

        Args:
            value:
                Valor.

        Raises:
            ValidationError:
                Si el valor no es numérico.
        """
        if isinstance(value, bool):
            raise ValidationError("Boolean values are not valid numeric values.")

        if not isinstance(value, (int, float)):
            raise ValidationError("Value must be numeric.")

    @staticmethod
    def validate_integer(
        value: object,
    ) -> None:
        """
        Valida que el valor sea un entero.

        Los valores booleanos no son considerados
        enteros válidos.

        Args:
            value:
                Valor.

        Raises:
            ValidationError:
                Si el valor no es un entero.
        """
        if isinstance(value, bool):
            raise ValidationError("Boolean values are not valid integers.")

        if not isinstance(value, int):
            raise ValidationError("Value must be an integer.")

    """----------Numeric Validation----------"""

    @staticmethod
    def validate_finite(
        value: Number,
    ) -> None:
        """
        Valida que un número sea finito.

        Rechaza:

        - NaN
        - +Infinity
        - -Infinity

        Args:
            value:
                Valor.

        Raises:
            ValidationError:
                Si el valor no es finito.
        """
        Validator.validate_numeric(value)

        if not isfinite(float(value)):
            raise ValidationError("Value must be finite.")

    @staticmethod
    def validate_positive(
        value: Number,
    ) -> None:
        """
        Valida que un número sea estrictamente positivo.
        """
        Validator.validate_numeric(value)
        Validator.validate_finite(value)

        if value <= 0:
            raise ValidationError("Value must be greater than zero.")

    @staticmethod
    def validate_non_negative(
        value: Number,
    ) -> None:
        """
        Valida que un número no sea negativo.
        """
        Validator.validate_numeric(value)
        Validator.validate_finite(value)

        if value < 0:
            raise ValidationError("Value cannot be negative.")

    """----------Range Validation----------"""

    @staticmethod
    def validate_probability(
        value: Number,
    ) -> None:
        """
        Valida una probabilidad.

        Debe pertenecer al intervalo [0.0, 1.0].

        Args:
            value:
                Probabilidad.

        Raises:
            ValidationError:
                Si el valor no representa
                una probabilidad válida.
        """
        Validator.validate_numeric(value)
        Validator.validate_finite(value)

        if value < 0.0 or value > 1.0:
            raise ValidationError("Probability must be between 0.0 and 1.0.")

    @staticmethod
    def validate_percentage(
        value: Number,
    ) -> None:
        """
        Valida un porcentaje.

        Debe pertenecer al intervalo [0, 100].

        Args:
            value:
                Porcentaje.

        Raises:
            ValidationError:
                Si el porcentaje es inválido.
        """
        Validator.validate_numeric(value)
        Validator.validate_finite(value)

        if value < 0.0 or value > 100.0:
            raise ValidationError("Percentage must be between 0 and 100.")

    @staticmethod
    def validate_range(
        value: Number,
        minimum: Number,
        maximum: Number,
    ) -> None:
        """
        Valida que un valor pertenezca a un rango inclusivo.

        Args:
            value:
                Valor.

            minimum:
                Límite inferior.

            maximum:
                Límite superior.

        Raises:
            ValidationError:
                Si el valor está fuera del rango.
        """
        Validator.validate_numeric(value)
        Validator.validate_numeric(minimum)
        Validator.validate_numeric(maximum)

        Validator.validate_finite(value)
        Validator.validate_finite(minimum)
        Validator.validate_finite(maximum)

        if minimum > maximum:
            raise ValidationError("Minimum value cannot be greater than maximum.")

        if not (minimum <= value <= maximum):
            raise ValidationError(f"Value must be between {minimum} and {maximum}.")

    @staticmethod
    def validate_between(
        value: Number,
        minimum: Number,
        maximum: Number,
    ) -> None:
        """
        Alias semántico de validate_range().

        Mejora la legibilidad en motores
        donde la validación expresa
        pertenencia a un intervalo.

        Args:
            value:
                Valor.

            minimum:
                Límite inferior.

            maximum:
                Límite superior.
        """
        Validator.validate_range(
            value=value,
            minimum=minimum,
            maximum=maximum,
        )

    @staticmethod
    def validate_greater_than(
        value: Number,
        threshold: Number,
    ) -> None:
        """
        Valida que un valor sea mayor que un umbral.
        """
        Validator.validate_numeric(value)
        Validator.validate_numeric(threshold)

        Validator.validate_finite(value)
        Validator.validate_finite(threshold)

        if value <= threshold:
            raise ValidationError(f"Value must be greater than {threshold}.")

    @staticmethod
    def validate_less_than(
        value: Number,
        threshold: Number,
    ) -> None:
        """
        Valida que un valor sea menor que un umbral.
        """
        Validator.validate_numeric(value)
        Validator.validate_numeric(threshold)

        Validator.validate_finite(value)
        Validator.validate_finite(threshold)

        if value >= threshold:
            raise ValidationError(f"Value must be less than {threshold}.")

    """----------Window Validation----------"""

    @staticmethod
    def validate_window(
        window_size: int,
    ) -> None:
        """
        Valida el tamaño de una ventana deslizante.

        Args:
            window_size:
                Tamaño de la ventana.

        Raises:
            ValidationError:
                Si el tamaño es inválido.
        """
        Validator.validate_integer(window_size)

        if window_size < 1:
            raise ValidationError("Window size must be greater than zero.")

    @staticmethod
    def validate_period(
        period: int,
    ) -> None:
        """
        Valida un período utilizado por algoritmos
        estadísticos o de aprendizaje.

        Args:
            period:
                Período.

        Raises:
            ValidationError:
                Si el período es inválido.
        """
        Validator.validate_integer(period)

        if period < 1:
            raise ValidationError("Period must be greater than zero.")

    """----------Collection Validation----------"""

    @staticmethod
    def validate_unique(
        sequence: Sequence[object],
    ) -> None:
        """
        Valida que todos los elementos de una secuencia
        sean únicos.

        La implementación no depende de que los elementos
        sean hashables.

        Args:
            sequence:
                Secuencia.

        Raises:
            ValidationError:
                Si existen elementos duplicados.
        """
        Validator.validate_not_empty(sequence)

        size = len(sequence)

        for i in range(size - 1):
            current = sequence[i]

            for j in range(i + 1, size):
                if current == sequence[j]:
                    raise ValidationError("Sequence contains duplicated values.")

    @staticmethod
    def validate_sorted(
        sequence: Sequence[Number],
        *,
        ascending: bool = True,
    ) -> None:
        """
        Valida que una secuencia esté ordenada.

        Args:
            sequence:
                Secuencia.

            ascending:
                True para orden ascendente.
                False para orden descendente.

        Raises:
            ValidationError:
                Si la secuencia no está ordenada.
        """
        Validator.validate_not_empty(sequence)

        for index in range(1, len(sequence)):
            previous = sequence[index - 1]
            current = sequence[index]

            if ascending:
                if previous > current:
                    raise ValidationError("Sequence is not sorted in ascending order.")

            else:
                if previous < current:
                    raise ValidationError("Sequence is not sorted in descending order.")

    """----------Index Validation----------"""

    @staticmethod
    def validate_index(
        index: int,
        sequence: Sequence[object],
    ) -> None:
        """
        Valida que un índice exista dentro de una
        secuencia.

        Args:
            index:
                Índice.

            sequence:
                Secuencia.

        Raises:
            ValidationError:
                Si el índice está fuera de rango.
        """
        Validator.validate_integer(index)
        Validator.validate_not_empty(sequence)

        if index < 0 or index >= len(sequence):
            raise ValidationError(f"Index {index} is out of range.")
