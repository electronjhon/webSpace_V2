"""
Space AI 2.0

Log Level

Defines the available logging levels for the
application.
"""

from __future__ import annotations

from enum import IntEnum


class LogLevel(IntEnum):
    """
    Logging verbosity levels.

    Higher values include lower-severity messages.
    """

    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


__all__ = [
    "LogLevel",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# SÍ
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
