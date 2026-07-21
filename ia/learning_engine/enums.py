"""
Space AI 2.0

Learning Engine

Enums

Enumeraciones oficiales del dominio del Learning Engine.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from enum import StrEnum


class FeedbackOutcome(StrEnum):
    """
    Clasificación cualitativa del resultado obtenido por
    una predicción o señal evaluada.

    SUCCESS:
        El resultado fue completamente correcto.

    PARTIAL_SUCCESS:
        El resultado fue parcialmente correcto.

    FAILURE:
        El resultado fue incorrecto.
    """

    SUCCESS = "success"

    PARTIAL_SUCCESS = "partial_success"

    FAILURE = "failure"


__all__ = [
    "FeedbackOutcome",
]
