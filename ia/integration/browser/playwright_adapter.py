"""
Space AI 2.0

Playwright Adapter

Implementación del BrowserAdapter basada en Playwright.

Este componente coordina la sesión del navegador, la captura de mensajes
WebSocket y el parser del protocolo, produciendo BrowserEvent para el
resto del sistema.

No contiene lógica de negocio ni interpreta el protocolo del juego.

Autor: Space AI 2.0
"""

from __future__ import annotations

from collections.abc import Iterator

from ia.integration.models.browser_event import BrowserEvent
from ia.integration.protocols.spaceman.parser import (
    SpacemanProtocolParser,
)

from .browser_adapter import BrowserAdapter
from .browser_session import BrowserSession
from .websocket_listener import WebSocketListener


class PlaywrightAdapter(BrowserAdapter):
    """
    Adaptador basado en Playwright.

    Coordina los componentes necesarios para transformar los mensajes
    capturados desde el navegador en BrowserEvent.
    """

    def __init__(
        self,
        session: BrowserSession,
    ) -> None:
        """
        Inicializa el adaptador.

        Parameters
        ----------
        session:
            Sesión activa del navegador.
        """
        self._session = session
        self._listener: WebSocketListener | None = None
        self._parser = SpacemanProtocolParser()

    def connect(self) -> None:

        print("[Adapter] connect()")

        self._session.connect()
        print("[Adapter] BrowserSession connected")

        self._listener = WebSocketListener(
            self._session.page,
        )
        print("[Adapter] Listener created")

        self._listener.start()
        print("[Adapter] Listener started")

    def disconnect(self) -> None:
        """
        Finaliza la captura de eventos y libera los recursos asociados.
        """
        if self._listener is not None:
            self._listener.stop()

        self._session.disconnect()

        self._listener = None

    def is_connected(self) -> bool:
        """
        Indica si existe una conexión activa.

        Returns
        -------
        bool
            True si el adaptador mantiene una conexión activa.
        """
        return self._session.is_connected() and self._listener is not None

    def events(self) -> Iterator[BrowserEvent]:
        """
        Produce continuamente BrowserEvent obtenidos desde Playwright.

        Yields
        ------
        BrowserEvent
            Eventos generados por el parser del protocolo.

        Raises
        ------
        RuntimeError
            Si el adaptador aún no ha sido conectado.
        """
        if self._listener is None:
            raise RuntimeError(
                "PlaywrightAdapter is not connected.",
            )

        for message in self._listener.messages():

            for event in self._parser.parse(message):

                print(
                    "[Adapter] BrowserEvent -> "
                    f"game_id={event.game_id}, "
                    f"multiplier={event.multiplier}"
                )

                yield event
