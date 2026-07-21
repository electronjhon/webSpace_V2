"""
Space AI 2.0

Core Statistics Library

Biblioteca estadística oficial del proyecto.

Responsabilidades:

- Estadística descriptiva
- Tendencias
- Dispersión
- Normalización
- Percentiles
- Medias móviles
- Regresión lineal

Este módulo es completamente independiente del dominio del juego
y puede ser reutilizado por cualquier motor del sistema.

Python 3.12
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite, sqrt
from statistics import (
    mean,
    median,
    multimode,
    pstdev,
    pvariance,
)

from core.exceptions import ValidationError

Number = int | float


class Statistics:
    """
    Biblioteca de utilidades estadísticas.

    Todas las funciones son estáticas para evitar mantener estado
    y facilitar su reutilización desde cualquier componente
    del sistema.
    """

    @staticmethod
    def _validate(values: Sequence[Number]) -> None:
        """
        Valida una secuencia numérica.

        Reglas:

        - La secuencia no puede estar vacía.
        - No se permiten valores booleanos.
        - No se permiten NaN.
        - No se permiten infinitos.

        Args:
            values:
                Secuencia de valores.

        Raises:
            ValidationError:
                Si la secuencia no cumple las reglas.
        """
        if len(values) == 0:
            raise ValidationError("The sequence cannot be empty.")

        for value in values:
            if isinstance(value, bool):
                raise ValidationError("Boolean values are not valid numeric values.")

            if not isfinite(float(value)):
                raise ValidationError("All values must be finite.")

    @staticmethod
    def count(values: Sequence[Number]) -> int:
        """
        Retorna la cantidad de elementos.

        Args:
            values:
                Datos.

        Returns:
            Número de elementos.
        """
        Statistics._validate(values)
        return len(values)

    @staticmethod
    def total(values: Sequence[Number]) -> float:
        """
        Retorna la suma total.

        Args:
            values:
                Datos.

        Returns:
            Suma.
        """
        Statistics._validate(values)
        return float(sum(values))

    @staticmethod
    def minimum(values: Sequence[Number]) -> float:
        """
        Retorna el valor mínimo.

        Args:
            values:
                Datos.

        Returns:
            Valor mínimo.
        """
        Statistics._validate(values)
        return float(min(values))

    @staticmethod
    def maximum(values: Sequence[Number]) -> float:
        """
        Retorna el valor máximo.

        Args:
            values:
                Datos.

        Returns:
            Valor máximo.
        """
        Statistics._validate(values)
        return float(max(values))

    @staticmethod
    def value_range(values: Sequence[Number]) -> float:
        """
        Calcula el rango estadístico.

        Args:
            values:
                Datos.

        Returns:
            Diferencia entre el máximo y el mínimo.
        """
        Statistics._validate(values)

        minimum = float(values[0])
        maximum = float(values[0])

        for value in values[1:]:
            numeric = float(value)

            if numeric < minimum:
                minimum = numeric

            if numeric > maximum:
                maximum = numeric

        return maximum - minimum

    @staticmethod
    def mean(values: Sequence[Number]) -> float:
        """
        Calcula la media aritmética.

        Args:
            values:
                Datos.

        Returns:
            Media.
        """
        Statistics._validate(values)
        return float(mean(values))

    @staticmethod
    def median(values: Sequence[Number]) -> float:
        """
        Calcula la mediana.

        Args:
            values:
                Datos.

        Returns:
            Mediana.
        """
        Statistics._validate(values)
        return float(median(values))

    @staticmethod
    def mode(values: Sequence[Number]) -> float:
        """
        Calcula la moda.

        Si existen múltiples modas,
        retorna la primera.

        Args:
            values:
                Datos.

        Returns:
            Moda.
        """
        Statistics._validate(values)

        modes = multimode(values)

        if len(modes) == 0:
            raise ValidationError("Unable to determine mode.")

        return float(modes[0])

    @staticmethod
    def variance(values: Sequence[Number]) -> float:
        """
        Calcula la varianza poblacional.

        Args:
            values:
                Datos.

        Returns:
            Varianza.
        """
        Statistics._validate(values)
        return float(pvariance(values))

    @staticmethod
    def standard_deviation(values: Sequence[Number]) -> float:
        """
        Calcula la desviación estándar poblacional.

        Args:
            values:
                Datos.

        Returns:
            Desviación estándar.
        """
        Statistics._validate(values)
        return float(pstdev(values))

    @staticmethod
    def mad(
        values: Sequence[Number],
    ) -> float:
        """
        Median Absolute Deviation.

        Args:
            values:
                Datos.

        Returns:
            MAD.
        """
        Statistics._validate(values)

        ordered = sorted(float(v) for v in values)

        size = len(ordered)
        middle = size // 2

        if size % 2 == 0:
            med = (ordered[middle - 1] + ordered[middle]) / 2.0
        else:
            med = ordered[middle]

        deviations = [abs(float(value) - med) for value in values]

        deviations.sort()

        size = len(deviations)
        middle = size // 2

        if size % 2 == 0:
            return (deviations[middle - 1] + deviations[middle]) / 2.0

        return deviations[middle]

    @staticmethod
    def min_max(
        values: Sequence[Number],
    ) -> list[float]:
        """
        Normaliza una secuencia utilizando
        Min-Max Scaling.

        Args:
            values:
                Datos.

        Returns:
            Serie normalizada.
        """
        Statistics._validate(values)

        minimum = float(values[0])
        maximum = float(values[0])

        for value in values[1:]:
            numeric = float(value)

            if numeric < minimum:
                minimum = numeric

            if numeric > maximum:
                maximum = numeric

        delta = maximum - minimum

        if delta == 0.0:
            return [0.0] * len(values)

        return [(float(value) - minimum) / delta for value in values]

    @staticmethod
    def z_score(
        values: Sequence[Number],
    ) -> list[float]:
        """
        Calcula el Z-Score de una serie.

        Args:
            values:
                Datos.

        Returns:
            Serie normalizada.
        """
        Statistics._validate(values)

        avg = float(mean(values))
        deviation = float(pstdev(values))

        if deviation == 0.0:
            return [0.0] * len(values)

        return [(float(value) - avg) / deviation for value in values]

    @staticmethod
    def percentile(
        values: Sequence[Number],
        percentile: float,
    ) -> float:
        """
        Calcula un percentil utilizando interpolación lineal.

        Args:
            values:
                Datos.

            percentile:
                Valor entre 0 y 100.

        Returns:
            Percentil solicitado.

        Raises:
            ValueError:
                Si el percentil está fuera de rango.
        """
        Statistics._validate(values)

        if percentile < 0 or percentile > 100:
            raise ValidationError("Percentile must be between 0 and 100.")

        ordered = sorted(float(v) for v in values)

        if len(ordered) == 1:
            return ordered[0]

        position = (len(ordered) - 1) * (percentile / 100)

        lower = int(position)
        upper = min(lower + 1, len(ordered) - 1)

        if lower == upper:
            return ordered[lower]

        fraction = position - lower

        return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction

    @staticmethod
    def sma(
        values: Sequence[Number],
        period: int,
    ) -> list[float]:
        """
        Calcula la Serie de la Media Móvil Simple (SMA).

        Cada posición representa la media de los últimos
        'period' elementos disponibles.

        Para los primeros elementos se utiliza la ventana
        parcial disponible.

        Args:
            values:
                Serie temporal.

            period:
                Tamaño de la ventana.

        Returns:
            Serie SMA.

        Raises:
            ValueError:
                Si el período es menor que uno.
        """
        Statistics._validate(values)

        if period < 1:
            raise ValidationError("Period must be greater than zero.")

        result: list[float] = []

        window_sum = 0.0

        for index, value in enumerate(values):
            window_sum += float(value)

            if index >= period:
                window_sum -= float(values[index - period])

            current_size = min(index + 1, period)

            result.append(window_sum / current_size)

        return result

    @staticmethod
    def ema(
        values: Sequence[Number],
        period: int,
    ) -> list[float]:
        """
        Calcula la Serie de la Media Móvil Exponencial (EMA).

        La EMA asigna un mayor peso a las observaciones más
        recientes, permitiendo responder con mayor rapidez
        a cambios en la serie temporal.

        Fórmula:

            α = 2 / (period + 1)

            EMA₀ = primer valor

            EMAₙ = α·valor + (1-α)·EMAₙ₋₁

        Args:
            values:
                Serie temporal.

            period:
                Período de suavizado.

        Returns:
            Serie EMA.

        Raises:
            ValueError:
                Si el período es menor que uno.
        """
        Statistics._validate(values)

        if period < 1:
            raise ValidationError("Period must be greater than zero.")

        alpha = 2.0 / (period + 1.0)

        result: list[float] = []

        ema_value = float(values[0])

        result.append(ema_value)

        for value in values[1:]:
            ema_value = alpha * float(value) + (1.0 - alpha) * ema_value

            result.append(ema_value)

        return result

    @staticmethod
    def slope(values: Sequence[Number]) -> float:
        """
        Calcula la pendiente de la regresión lineal
        utilizando mínimos cuadrados.

        La pendiente representa la tendencia general
        de la serie.

        Valores positivos:
            Tendencia ascendente.

        Valores negativos:
            Tendencia descendente.

        Valor cercano a cero:
            Tendencia lateral.

        Args:
            values:
                Serie temporal.

        Returns:
            Pendiente de la recta.
        """
        Statistics._validate(values)

        if len(values) == 1:
            return 0.0

        n = len(values)

        mean_x = (n - 1) / 2.0

        mean_y = Statistics.mean(values)

        numerator = 0.0
        denominator = 0.0

        for index, value in enumerate(values):
            dx = index - mean_x
            dy = float(value) - mean_y

            numerator += dx * dy
            denominator += dx * dx

        if denominator == 0.0:
            return 0.0

        return numerator / denominator

    @staticmethod
    def momentum(
        values: Sequence[Number],
    ) -> float:
        """
        Calculates the momentum of a sequence.

        Momentum is defined as the difference
        between the most recent value and the
        oldest value in the sequence.

        Args:
            values:
                Numeric sequence.

        Returns:
            Momentum value.
        """

        Statistics._validate(values)

        return float(values[-1]) - float(values[0])

    @staticmethod
    def coefficient_of_variation(
        values: Sequence[Number],
    ) -> float:
        """
        Calcula el coeficiente de variación.

        Args:
            values:
                Datos.

        Returns:
            CV.
        """
        Statistics._validate(values)

        avg = float(mean(values))

        if avg == 0.0:
            raise ValidationError(
                "Coefficient of variation is undefined when the mean equals zero."
            )

        deviation = float(pstdev(values))

        return deviation / abs(avg)

    @staticmethod
    def root_mean_square(
        values: Sequence[Number],
    ) -> float:
        """
        Calcula el Root Mean Square (RMS).

        Fórmula:

            sqrt(sum(x²) / n)

        Args:
            values:
                Datos.

        Returns:
            RMS.
        """
        Statistics._validate(values)

        squared_sum = 0.0

        for value in values:
            numeric = float(value)
            squared_sum += numeric * numeric

        return sqrt(squared_sum / len(values))

    @staticmethod
    def mean_absolute_error(
        expected: Sequence[Number],
        predicted: Sequence[Number],
    ) -> float:
        """
        Calcula el Error Absoluto Medio (MAE).

        Args:
            expected:
                Valores reales.

            predicted:
                Valores estimados.

        Returns:
            MAE.

        Raises:
            ValueError:
                Si las secuencias tienen tamaños distintos.
        """
        Statistics._validate(expected)
        Statistics._validate(predicted)

        if len(expected) != len(predicted):
            raise ValidationError("Sequences must have the same length.")

        total_error = 0.0

        for real, estimate in zip(expected, predicted, strict=True):
            total_error += abs(float(real) - float(estimate))

        return total_error / len(expected)

    @staticmethod
    def root_mean_square_error(
        expected: Sequence[Number],
        predicted: Sequence[Number],
    ) -> float:
        """
        Calcula el Root Mean Square Error (RMSE).

        Args:
            expected:
                Valores reales.

            predicted:
                Valores estimados.

        Returns:
            RMSE.

        Raises:
            ValueError:
                Si las secuencias tienen tamaños distintos.
        """
        Statistics._validate(expected)
        Statistics._validate(predicted)

        if len(expected) != len(predicted):
            raise ValidationError("Sequences must have the same length.")

        squared_error = 0.0

        for real, estimate in zip(expected, predicted, strict=True):
            difference = float(real) - float(estimate)

            squared_error += difference * difference

        return sqrt(squared_error / len(expected))
