"""
Space AI 2.0

Protocol Parser

Define el contrato para todos los analizadores de protocolos de captura.

Un ProtocolParser transforma mensajes crudos provenientes de una fuente
externa (WebSocket, replay, API, etc.) en una secuencia de BrowserEvent.

Este contrato constituye el límite entre el protocolo específico de una
fuente de datos y el resto de la infraestructura de integración.

Autor: Space AI 2.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator

from ia.integration.models.browser_event import BrowserEvent


class ProtocolParser(ABC):
    """
    Contrato base para analizadores de protocolos.

    Las implementaciones concretas son responsables de interpretar los
    mensajes recibidos desde una fuente externa y producir cero, uno o
    varios BrowserEvent.

    El parser nunca debe lanzar excepciones debido a mensajes inválidos.
    Los mensajes no reconocidos simplemente no producirán eventos.
    """

    @abstractmethod
    def parse(
        self,
        message: str,
    ) -> Iterator[BrowserEvent]:
        """
        Analiza un mensaje recibido desde una fuente externa.

        Parameters
        ----------
        message:
            Mensaje crudo recibido desde el protocolo de comunicación.

        Yields
        ------
        BrowserEvent
            Eventos válidos obtenidos del mensaje.

        Notes
        -----
        Dependiendo del tipo de mensaje recibido, la implementación puede:

        - no producir eventos;
        - producir un único evento;
        - producir múltiples eventos.

        Esto permite utilizar el mismo contrato tanto para el historial
        inicial del juego como para las rondas recibidas en tiempo real.
        """
        raise NotImplementedError
