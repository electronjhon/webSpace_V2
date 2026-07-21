"""
Space AI 2.0

Browser Adapter Contract

Define el contrato que debe implementar cualquier adaptador capaz de
obtener eventos desde una fuente externa (Playwright, Selenium,
simuladores, APIs, etc.).

Esta interfaz constituye el límite entre la infraestructura externa
y el Collector.

Autor: Space AI 2.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator

from ia.integration.models.browser_event import BrowserEvent


class BrowserAdapter(ABC):
    """
    Contrato para adaptadores de captura.

    Un BrowserAdapter es responsable únicamente de obtener eventos
    provenientes de una fuente externa y entregarlos como objetos
    BrowserEvent.

    No debe contener lógica de negocio ni conocer componentes del
    dominio como FeatureEngine, StateEngine o Predictor.
    """

    @abstractmethod
    def connect(self) -> None:
        """
        Establece la conexión con la fuente de datos.

        Raises
        ------
        ConnectionError
            Si no es posible establecer la conexión.
        """

    @abstractmethod
    def disconnect(self) -> None:
        """
        Finaliza la conexión liberando todos los recursos utilizados.
        """

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Indica si el adaptador mantiene una conexión activa.

        Returns
        -------
        bool
            True si existe una conexión activa.
        """

    @abstractmethod
    def events(self) -> Iterator[BrowserEvent]:
        """
        Produce eventos capturados desde la fuente de datos.

        Returns
        -------
        Iterator[BrowserEvent]
            Flujo continuo de eventos.

        Notes
        -----
        La implementación puede ser infinita mientras la conexión
        permanezca activa.
        """
