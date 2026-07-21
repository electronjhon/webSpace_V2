"""
Space AI 2.0

Duplicate Detector

Detecta observaciones duplicadas provenientes de la infraestructura de
captura.

Su responsabilidad consiste únicamente en determinar si una observación
ya fue procesada anteriormente.

Autor: Space AI 2.0
"""

from __future__ import annotations

from collections import deque

from ia.integration.models.round_observation import RoundObservation


class DuplicateDetector:
    """
    Detector de observaciones duplicadas.

    Mantiene una ventana deslizante con los identificadores de las últimas
    rondas procesadas para evitar reprocesar eventos repetidos.
    """

    def __init__(
        self,
        capacity: int = 100,
    ) -> None:
        """
        Inicializa el detector.

        Parameters
        ----------
        capacity:
            Número máximo de identificadores conservados.
        """
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero.")

        self._capacity = capacity
        self._history: deque[int] = deque(maxlen=capacity)

    def is_duplicate(
        self,
        observation: RoundObservation,
    ) -> bool:
        """
        Indica si una observación ya fue procesada.

        Parameters
        ----------
        observation:
            Observación a evaluar.

        Returns
        -------
        bool
            True si la observación ya fue registrada.
        """
        return observation.round_id in self._history

    def register(
        self,
        observation: RoundObservation,
    ) -> None:
        """
        Registra una observación como procesada.

        Parameters
        ----------
        observation:
            Observación procesada.
        """
        self._history.append(observation.round_id)

    def clear(self) -> None:
        """
        Elimina el historial de observaciones registradas.
        """
        self._history.clear()

    @property
    def capacity(self) -> int:
        """
        Capacidad máxima del detector.
        """
        return self._capacity

    def __len__(self) -> int:
        """
        Número de identificadores almacenados.
        """
        return len(self._history)
