"""
Space AI 2.0

Application Composition

Composition Root of the application.

Responsible for composing the complete object graph of the
application.

No business logic is allowed in this module.
"""

from __future__ import annotations

from ia.application.application import SpaceAIApplication
from ia.application.bootstrap import ApplicationBootstrap


def create_application(
    bootstrap: ApplicationBootstrap,
) -> SpaceAIApplication:
    """
    Create a fully configured Space AI application.

    Parameters
    ----------
    bootstrap:
        Initialized application bootstrap.

    Returns
    -------
    SpaceAIApplication
        Ready-to-run application.
    """

    bootstrap.initialize()

    return SpaceAIApplication(
        context=bootstrap.context,
    )


__all__ = [
    "create_application",
]
