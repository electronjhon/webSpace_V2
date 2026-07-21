"""
Space AI 2.0

Browser Event Model

Representa un evento crudo proveniente del navegador (Playwright/WebSocket).

Este modelo pertenece exclusivamente a la capa de infraestructura y nunca
debe propagarse hacia el dominio de la IA.

Autor: Space AI 2.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Final

UNKNOWN_SOURCE: Final[str] = "unknown"


@dataclass(frozen=True, slots=True)
class BrowserEvent:
    """
    Evento capturado desde el navegador.

    Este objeto representa exactamente la información obtenida desde
    Playwright/WebSocket antes de cualquier transformación hacia los
    modelos del dominio.

    Attributes
    ----------
    game_id:
        Identificador único de la ronda.

    multiplier:
        Multiplicador final de la ronda.

    captured_at:
        Fecha y hora UTC en que el evento fue recibido.

    source:
        Origen del evento (websocket, dom, replay, etc.).

    raw_message:
        Mensaje original recibido desde el navegador.
        Se conserva únicamente para auditoría y depuración.
    """

    game_id: int

    multiplier: float

    captured_at: datetime

    source: str = UNKNOWN_SOURCE

    raw_message: str | None = None

    @classmethod
    def create(
        cls,
        *,
        game_id: int,
        multiplier: float,
        source: str = UNKNOWN_SOURCE,
        raw_message: str | None = None,
    ) -> BrowserEvent:
        """
        Construye un BrowserEvent utilizando la hora UTC actual.

        Parameters
        ----------
        game_id:
            Identificador de la ronda.

        multiplier:
            Multiplicador obtenido.

        source:
            Fuente del evento.

        raw_message:
            Mensaje original recibido.

        Returns
        -------
        BrowserEvent
        """
        return cls(
            game_id=game_id,
            multiplier=multiplier,
            captured_at=datetime.now(UTC),
            source=source,
            raw_message=raw_message,
        )
