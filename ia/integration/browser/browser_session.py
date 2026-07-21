"""
Space AI 2.0

Browser Session

Administra el ciclo de vida de la conexión con un navegador Chromium
utilizando Chrome DevTools Protocol (CDP).

Esta clase encapsula exclusivamente la infraestructura necesaria para
establecer y liberar la sesión del navegador.

No interpreta información del juego ni genera eventos del dominio.

Autor: Space AI 2.0
"""

from __future__ import annotations

from dataclasses import dataclass

from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


@dataclass(slots=True)
class BrowserSession:
    """
    Administra una sesión de navegador mediante Playwright.

    Parameters
    ----------
    cdp_url:
        Dirección del endpoint CDP del navegador.
    """

    cdp_url: str

    _playwright: Playwright | None = None
    _browser: Browser | None = None
    _context: BrowserContext | None = None
    _page: Page | None = None

    def connect(self) -> None:
        """
        Establece una conexión utilizando Chrome DevTools Protocol.

        Raises
        ------
        RuntimeError
            Si no existe ningún contexto o página disponible.
        """

        if self.is_connected():
            return

        self._playwright = sync_playwright().start()

        self._browser = self._playwright.chromium.connect_over_cdp(
            self.cdp_url,
        )

        if not self._browser.contexts:
            raise RuntimeError("The connected browser does not expose any context.")

        self._context = self._browser.contexts[0]

        if not self._context.pages:
            raise RuntimeError("The browser context does not contain any open page.")

        self._page = self._context.pages[0]

    def disconnect(self) -> None:
        """
        Libera todos los recursos asociados a la sesión.
        """

        if self._browser is not None:
            self._browser.close()

        if self._playwright is not None:
            self._playwright.stop()

        self._page = None
        self._context = None
        self._browser = None
        self._playwright = None

    def is_connected(self) -> bool:
        """
        Indica si existe una sesión activa.

        Returns
        -------
        bool
        """
        return (
            self._playwright is not None
            and self._browser is not None
            and self._context is not None
            and self._page is not None
        )

    @property
    def browser(self) -> Browser:
        """
        Devuelve el navegador conectado.

        Raises
        ------
        RuntimeError
            Si la sesión aún no ha sido inicializada.
        """

        if self._browser is None:
            raise RuntimeError("Browser session is not connected.")

        return self._browser

    @property
    def context(self) -> BrowserContext:
        """
        Devuelve el contexto activo.
        """

        if self._context is None:
            raise RuntimeError("Browser context is not available.")

        return self._context

    @property
    def page(self) -> Page:
        """
        Devuelve la página activa.
        """

        if self._page is None:
            raise RuntimeError("Browser page is not available.")

        return self._page
