from __future__ import annotations

from dataclasses import dataclass

from state_engine.state_labels import StateLabels


@dataclass(frozen=True, slots=True)
class MarkovState:
    """
    Representación lógica de un estado para el modelo de Markov.

    La equivalencia entre estados está determinada exclusivamente por
    StateLabels.
    """

    labels: StateLabels

    @property
    def key(self) -> StateLabels:
        return self.labels

    def __str__(self) -> str:
        return (
            f"{self.labels.trend.name}|"
            f"{self.labels.momentum.name}|"
            f"{self.labels.entropy.name}|"
            f"{self.labels.compression.name}|"
            f"{self.labels.balance.name}|"
            f"{self.labels.volatility.name}"
        )
