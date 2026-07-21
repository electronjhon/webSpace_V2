"""
Space AI 2.0

Round Observation Model

Representa una observación normalizada del dominio obtenida desde cualquier
fuente de datos.

Este modelo constituye la frontera entre la infraestructura y el núcleo
de la IA. Ningún motor interno debe depender de BrowserEvent, Playwright
ni del protocolo del navegador.

Autor: Space AI 2.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class ObservationSource(StrEnum):
    """
    Fuente desde la cual fue obtenida la observación.
    """

    BROWSER = "browser"
    REPLAY = "replay"
    SIMULATION = "simulation"
    API = "api"
    UNKNOWN = "unknown"


@dataclass(frozen=True, slots=True)
class RoundObservation:
    """
    Observación de una ronda perteneciente al dominio.

    Esta clase representa una ronda completamente normalizada,
    independiente del mecanismo mediante el cual fue obtenida.

    Attributes
    ----------
    round_id:
        Identificador único de la ronda.

    multiplier:
        Multiplicador final de la ronda.

    observed_at:
        Instante UTC en que la observación fue registrada.

    source:
        Fuente lógica de la observación.

    confidence:
        Nivel de confianza asociado a la captura.

        Normalmente será 1.0 para capturas provenientes del
        navegador en tiempo real.
    """

    round_id: int

    multiplier: float

    observed_at: datetime

    source: ObservationSource

    confidence: float = 1.0
