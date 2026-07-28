from __future__ import annotations

from playwright.sync_api import (
    BrowserContext,
    Page,
    WebSocket,
    sync_playwright,
)

CDP_URL = "http://127.0.0.1:9222"


def on_ws(ws: WebSocket) -> None:
    print("\nWEBSOCKET")
    print(ws.url)


def on_page(page: Page) -> None:
    print("\nNEW PAGE")
    print(page.url)

    page.on("websocket", on_ws)


with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp(CDP_URL)

    print(f"Contexts: {len(browser.contexts)}")

    for context in browser.contexts:

        context: BrowserContext

        context.on("page", on_page)

        print("\nCONTEXT")

        for page in context.pages:

            print(page.url)

            page.on("websocket", on_ws)

    print("\nListening...")

    while True:
        browser.contexts[0].pages[0].wait_for_timeout(1000)
