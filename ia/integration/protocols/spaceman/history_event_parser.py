"""
Space AI 2.0

History Event Parser

Convierte el historial inicial de Spaceman en una secuencia de
BrowserEvent.

Este componente conoce únicamente el formato del mensaje
SpaceManStatisticHistory y no interpreta ningún otro tipo de evento
del protocolo.

Autor: Space AI 2.0
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from json import JSONDecodeError

from ia.integration.models.browser_event import BrowserEvent

from .constants import (
    DEFAULT_EVENT_SOURCE,
    GAME_ID_KEY,
    GAME_RESULT_KEY,
    HISTORY_KEY,
    STATISTIC_HISTORY_EVENT,
)


class HistoryEventParser:
    """
    Analizador del historial inicial de Spaceman.

    Un único mensaje del protocolo puede producir cero, uno o múltiples
    BrowserEvent.
    """

    def parse(
        self,
        message: str,
    ) -> Iterator[BrowserEvent]:
        """
        Analiza un mensaje de historial.

        Parameters
        ----------
        message:
            Mensaje WebSocket recibido.

        Yields
        ------
        BrowserEvent
            Eventos obtenidos del historial.
        """

        if STATISTIC_HISTORY_EVENT not in message or f'"{HISTORY_KEY}"' not in message:
            return

        payload = self._extract_json(message)

        if payload is None:
            return

        history = payload.get(HISTORY_KEY)

        if not isinstance(history, list):
            return

        for item in reversed(history):

            if not isinstance(item, dict):
                continue

            game_id = item.get(GAME_ID_KEY)
            multiplier = item.get(GAME_RESULT_KEY)

            if not isinstance(game_id, (int, str)):
                continue

            if not isinstance(multiplier, (int, float)):
                continue

            multiplier = float(multiplier)

            if multiplier <= 0.0:
                continue

            print(f"[HistoryParser] " f"{game_id} -> {multiplier}")

            yield BrowserEvent.create(
                game_id=int(game_id),
                multiplier=multiplier,
                source=DEFAULT_EVENT_SOURCE,
                raw_message=message,
            )

    @staticmethod
    def _extract_json(
        message: str,
    ) -> dict[str, object] | None:
        """
        Extrae el objeto JSON contenido en el mensaje.

        Parameters
        ----------
        message:
            Mensaje recibido desde el WebSocket.

        Returns
        -------
        dict[str, object] | None
            Objeto JSON extraído o None si no pudo obtenerse.
        """

        try:
            json_payload = message.split(">", 1)[1].rsplit("<", 1)[0]
        except IndexError:
            return None

        try:
            data = json.loads(json_payload)
        except JSONDecodeError:
            return None

        if not isinstance(data, dict):
            return None

        return data
