"""
Space AI 2.0

Logger

Simple centralized logger for the application.
"""

from __future__ import annotations

from config.constants import LOG_LEVEL
from core.logging.log_level import LogLevel


class Logger:
    """
    Centralized application logger.

    Logging verbosity is controlled through
    Logger.level.
    """

    level: LogLevel = LOG_LEVEL

    @classmethod
    def debug(
        cls,
        message: str,
    ) -> None:
        if cls.level >= LogLevel.DEBUG:
            print(message)

    @classmethod
    def debug_block(
        cls,
        title: str,
        content: str,
    ) -> None:
        """
        Print a formatted debug block.
        """
        if cls.level < LogLevel.DEBUG:
            return

        print()
        print(f"========== {title} ==========")
        print(content)
        print("=" * (22 + len(title)))

    @classmethod
    def info(
        cls,
        message: str,
    ) -> None:
        if cls.level >= LogLevel.INFO:
            print(message)

    @classmethod
    def info_block(
        cls,
        title: str,
        content: str,
    ) -> None:
        """
        Print a formatted info block.
        """
        if cls.level < LogLevel.INFO:
            return

        print()
        print(f"========== {title} ==========")
        print(content)
        print("=" * (22 + len(title)))

    @classmethod
    def warning(
        cls,
        message: str,
    ) -> None:
        if cls.level >= LogLevel.WARNING:
            print(message)

    @classmethod
    def error(
        cls,
        message: str,
    ) -> None:
        if cls.level >= LogLevel.ERROR:
            print(message)


__all__ = [
    "Logger",
]

# ---------------------------------------------------------------------
# Estado:
# TERMINADO
#
# Congelado:
# NO
#
# Versión:
# 1.0.0
# ---------------------------------------------------------------------
