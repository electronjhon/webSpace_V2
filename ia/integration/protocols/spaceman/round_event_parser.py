"""
Space AI 2.0

Round Event Parser

Convierte un mensaje correspondiente al resultado final de una ronda
de Spaceman en un BrowserEvent.

Este componente conoce únicamente el formato del mensaje <gr ...>
utilizado por el protocolo del juego.

Autor: Space AI 2.0
"""

from __future__ import annotations

from collections.abc import Iterator

from ia.integration.models.browser_event import BrowserEvent

from .constants import (
    DEFAULT_EVENT_SOURCE,
    ROUND_RESULT_PATTERN,
)


class RoundEventParser:
    """
    Analizador de resultados finales de una ronda.

    Un mensaje puede producir cero o un BrowserEvent.
    """

    def parse(
        self,
        message: str,
    ) -> Iterator[BrowserEvent]:
        """
        Analiza un mensaje correspondiente a una ronda finalizada.

        Parameters
        ----------
        message:
            Mensaje recibido desde el WebSocket.

        Yields
        ------
        BrowserEvent
            Evento correspondiente a la ronda.
        """

        match = ROUND_RESULT_PATTERN.search(message)

        if match is None:
            return

        try:
            game_id = int(match.group("game_id"))
            multiplier = float(match.group("result"))
        except (TypeError, ValueError):
            return

        if multiplier <= 0.0:
            return

        yield BrowserEvent.create(
            game_id=game_id,
            multiplier=multiplier,
            source=DEFAULT_EVENT_SOURCE,
            raw_message=message,
        )
