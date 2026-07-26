"""
Space AI 2.0

Collector

Coordina la captura de observaciones provenientes de la infraestructura
de integración.

El Collector constituye la frontera entre la capa de integración
(browser, replay, API, etc.) y el núcleo de Space AI.

Autor: Space AI 2.0
"""

from __future__ import annotations

import logging
from collections.abc import Iterator

from ia.integration.browser.browser_adapter import BrowserAdapter
from ia.integration.models.round_observation import RoundObservation

from .duplicate_detector import DuplicateDetector
from .round_mapper import RoundMapper

logger = logging.getLogger(__name__)


class Collector:
    """
    Coordina la captura de observaciones.

    Responsabilidades
    -----------------
    - administrar el ciclo de vida del BrowserAdapter;
    - convertir BrowserEvent en RoundObservation;
    - eliminar observaciones duplicadas;
    - producir únicamente observaciones válidas.
    """

    def __init__(
        self,
        adapter: BrowserAdapter,
    ) -> None:
        """
        Inicializa el Collector.

        Parameters
        ----------
        adapter:
            Adaptador responsable de producir BrowserEvent.
        """
        self._adapter = adapter
        self._mapper = RoundMapper()
        self._duplicates = DuplicateDetector()

    def connect(self) -> None:
        """
        Establece la conexión con la fuente de datos.
        """
        self._adapter.connect()

    def disconnect(self) -> None:
        """
        Finaliza la captura liberando todos los recursos.
        """
        self._adapter.disconnect()

    def is_connected(self) -> bool:
        """
        Indica si el Collector mantiene una conexión activa.

        Returns
        -------
        bool
        """
        return self._adapter.is_connected()

    def observations(
        self,
    ) -> Iterator[RoundObservation]:
        """
        Produce observaciones normalizadas.

        Yields
        ------
        RoundObservation
            Observaciones listas para ser consumidas por el núcleo
            de Space AI.
        """

        for event in self._adapter.events():

            logger.debug(
                "[Collector] Received event: game_id=%d, multiplier=%s, "
                "source=%s, captured_at=%s",
                event.game_id,
                event.multiplier,
                event.source,
                event.captured_at,
            )

            observation = self._mapper.map(event)

            logger.debug(
                "[Collector] Normalized observation: round_id=%d, "
                "multiplier=%s, source=%s, observed_at=%s",
                observation.round_id,
                observation.multiplier,
                observation.source,
                observation.observed_at,
            )

            if self._duplicates.is_duplicate(observation):
                logger.debug(
                    "[Collector] Duplicate observation discarded: round_id=%d",
                    observation.round_id,
                )
                continue

            self._duplicates.register(observation)

            yield observation
