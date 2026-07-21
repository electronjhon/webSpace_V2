"""
Space AI 2.0

Spaceman Protocol Parser

Implementación del contrato ProtocolParser para el juego Spaceman.

Coordina los distintos analizadores del protocolo y transforma un
mensaje WebSocket en cero, uno o múltiples BrowserEvent.

Autor: Space AI 2.0
"""

from __future__ import annotations

from collections.abc import Iterator

from ia.integration.browser.protocol_parser import ProtocolParser
from ia.integration.models.browser_event import BrowserEvent

from .history_event_parser import HistoryEventParser
from .round_event_parser import RoundEventParser


class SpacemanProtocolParser(ProtocolParser):
    """
    Parser principal del protocolo Spaceman.

    Este componente coordina los analizadores especializados para cada
    tipo de mensaje soportado por el protocolo.
    """

    def __init__(self) -> None:
        self._history_parser = HistoryEventParser()
        self._round_parser = RoundEventParser()

    def parse(
        self,
        message: str,
    ) -> Iterator[BrowserEvent]:
        """
        Analiza un mensaje del protocolo.

        Parameters
        ----------
        message:
            Mensaje recibido desde el WebSocket.

        Yields
        ------
        BrowserEvent
            Eventos generados a partir del mensaje.
        """

        yield from self._history_parser.parse(message)

        yield from self._round_parser.parse(message)
