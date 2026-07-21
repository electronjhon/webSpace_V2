"""
Space AI 2.0

Round Mapper

Convierte BrowserEvent en RoundObservation.

Este componente constituye la frontera entre la infraestructura de captura
y el dominio de la IA.

Autor: Space AI 2.0
"""

from __future__ import annotations

from ia.integration.models.browser_event import BrowserEvent
from ia.integration.models.round_observation import (
    ObservationSource,
    RoundObservation,
)


class RoundMapper:
    """
    Convierte BrowserEvent en RoundObservation.
    """

    def map(
        self,
        event: BrowserEvent,
    ) -> RoundObservation:
        """
        Convierte un BrowserEvent en una observación del dominio.

        Parameters
        ----------
        event:
            Evento capturado desde el navegador.

        Returns
        -------
        RoundObservation
            Observación normalizada lista para ser consumida por la IA.
        """

        return RoundObservation(
            round_id=event.game_id,
            multiplier=event.multiplier,
            observed_at=event.captured_at,
            source=self._map_source(event.source),
            confidence=1.0,
        )

    @staticmethod
    def _map_source(
        source: str,
    ) -> ObservationSource:
        """
        Convierte el origen textual del BrowserEvent en un
        ObservationSource.

        Parameters
        ----------
        source:
            Fuente registrada en el BrowserEvent.

        Returns
        -------
        ObservationSource
            Enumeración correspondiente.
        """

        try:
            return ObservationSource(source)
        except ValueError:
            return ObservationSource.UNKNOWN
