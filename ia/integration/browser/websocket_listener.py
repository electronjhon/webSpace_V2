"""
Space AI 2.0

WebSocket Listener

Escucha mensajes WebSocket provenientes del navegador y los expone como
una secuencia continua de mensajes crudos.

No interpreta el protocolo del juego ni conoce la estructura de los
mensajes intercambiados.

Autor: Space AI 2.0
"""

from __future__ import annotations

from collections.abc import Iterator
from queue import Empty, Queue
from threading import Event

from playwright.sync_api import Page, WebSocket


class WebSocketListener:
    """
    Captura mensajes WebSocket emitidos por una página.

    La clase únicamente almacena mensajes de texto recibidos.
    Toda interpretación corresponde al ProtocolParser.
    """

    def __init__(
        self,
        page: Page,
        messages: Queue[str] | None = None,
    ) -> None:
        """
        Inicializa el listener.

        Parameters
        ----------
        page:
            Página que será observada.

        messages:
            Cola compartida opcional. Si no se proporciona,
            el listener crea una cola privada, preservando el
            comportamiento existente.
        """
        self._page = page
        self._messages: Queue[str] = messages if messages is not None else Queue()

        self._running = Event()
        self._registered = False

    def start(self) -> None:
        """
        Comienza a escuchar mensajes WebSocket.
        """
        if self._registered:
            return

        self._page.on(
            "websocket",
            self._on_websocket,
        )

        self._running.set()
        self._registered = True

    def stop(self) -> None:
        """
        Detiene la escucha de nuevos mensajes.
        """
        self._running.clear()

    def messages(self) -> Iterator[str]:
        """
        Produce continuamente los mensajes recibidos.

        Yields
        ------
        str
            Mensaje recibido desde el WebSocket.
        """
        while self._running.is_set():
            self._page.wait_for_timeout(50)

            try:
                yield self._messages.get_nowait()
            except Empty:
                continue

    def _on_websocket(
        self,
        websocket: WebSocket,
    ) -> None:
        """
        Registra los callbacks para un WebSocket recién creado.

        Parameters
        ----------
        websocket:
            WebSocket proporcionado por Playwright.
        """
        print(f"[WebSocketListener] WebSocket detected: {websocket.url}")

        if "/game" not in websocket.url:
            print("[WebSocketListener] Ignored.")
            return

        print("[WebSocketListener] GAME WebSocket registered.")

        websocket.on(
            "framereceived",
            self._on_frame_received,
        )

    def _on_frame_received(
        self,
        payload: bytes | str,
    ) -> None:
        """
        Almacena un mensaje recibido.

        Parameters
        ----------
        payload:
            Contenido del frame recibido.
        """
        if isinstance(payload, bytes):
            print(f"[Frame] bytes={len(payload)}")
        else:
            preview = payload[:200].replace("\n", "\\n")

            print()
            print("========== FRAME ==========")
            print(preview)
            print("===========================")

        if isinstance(payload, bytes):
            payload = payload.decode(
                "utf-8",
                errors="replace",
            )

        self._messages.put(payload)
