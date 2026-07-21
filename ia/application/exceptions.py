"""
Space AI 2.0

Application Exceptions

Defines the exception hierarchy for the application layer.
"""

from __future__ import annotations


class ApplicationError(Exception):
    """
    Base exception for the application layer.
    """


class ApplicationInitializationError(ApplicationError):
    """
    Raised when the application cannot be initialized.
    """


class ApplicationRuntimeError(ApplicationError):
    """
    Raised when the application lifecycle is used incorrectly.
    """
