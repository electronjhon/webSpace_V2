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

import re
from collections.abc import Iterator

from ia.integration.models.browser_event import BrowserEvent

from .constants import DEFAULT_EVENT_SOURCE


class RoundEventParser:
    """
    Analizador de resultados finales de una ronda.

    Un mensaje puede producir cero o un BrowserEvent.
    """

    _GAME_ID_PATTERN = re.compile(r'gId="(?P<game_id>\d+)"')

    _RESULT_PATTERN = re.compile(r'result="(?P<result>[0-9]+(?:\.[0-9]+)?)"')

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

        if "<gr" not in message:
            return

        game_id_match = self._GAME_ID_PATTERN.search(message)

        result_match = self._RESULT_PATTERN.search(message)

        if game_id_match is None or result_match is None:
            return

        try:

            game_id = int(game_id_match.group("game_id"))

            multiplier = float(result_match.group("result"))

        except (TypeError, ValueError):

            return

        if multiplier <= 0:

            return

        print(f"[RoundParser] " f"{game_id} -> {multiplier}")

        yield BrowserEvent.create(
            game_id=game_id,
            multiplier=multiplier,
            source=DEFAULT_EVENT_SOURCE,
            raw_message=message,
        )
