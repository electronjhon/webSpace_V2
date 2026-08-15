"""
Space AI 2.0

Learning Engine

Prediction Metrics

Métricas acumuladas de evaluación predictiva.

Sprint:
    15
Versión:
    1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(
    frozen=True,
    slots=True,
)
class PredictionMetrics:
    """
    Métricas acumuladas del rendimiento del Predictor.

    Las métricas se mantienen inmutables. Cada evaluación
    produce una nueva instancia con los valores actualizados.
    """

    total: int = 0

    correct: int = 0

    partial: int = 0

    incorrect: int = 0

    total_score: Decimal = Decimal("0")

    @property
    def accuracy(self) -> float:
        """
        Porcentaje de predicciones completamente correctas.

        Devuelve un valor entre 0.0 y 1.0.
        """

        if self.total == 0:
            return 0.0

        return self.correct / self.total

    @property
    def average_score(self) -> float:
        """
        Score promedio de las predicciones evaluadas.

        Devuelve un valor entre 0.0 y 1.0 cuando el
        LearningScore pertenece a ese rango.
        """

        if self.total == 0:
            return 0.0

        return float(self.total_score / Decimal(self.total))

    def add(
        self,
        outcome: str,
        score: Decimal,
    ) -> PredictionMetrics:
        """
        Devuelve nuevas métricas incorporando una evaluación.

        Parameters
        ----------
        outcome:
            Resultado de la evaluación.

        score:
            Score obtenido por la predicción.
        """

        normalized_outcome = outcome.upper()

        return PredictionMetrics(
            total=self.total + 1,
            correct=self.correct + int(normalized_outcome == "CORRECT"),
            partial=self.partial + int(normalized_outcome == "PARTIAL"),
            incorrect=self.incorrect + int(normalized_outcome == "INCORRECT"),
            total_score=self.total_score + score,
        )


__all__ = [
    "PredictionMetrics",
]
