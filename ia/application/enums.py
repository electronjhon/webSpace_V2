"""
Space AI 2.0

Application Enums

Defines the application lifecycle states.
"""

from __future__ import annotations

from enum import StrEnum


class ApplicationState(StrEnum):
    """
    Represents the lifecycle state of the application.
    """

    CREATED = "created"
    INITIALIZED = "initialized"
    RUNNING = "running"
    STOPPED = "stopped"
