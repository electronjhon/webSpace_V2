"""
Space AI 2.0

Core

Jerarquía oficial de excepciones compartidas por todos los
componentes del sistema.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations


class CoreError(Exception):
    """
    Excepción base del Core.
    """


class ValueObjectValidationError(CoreError):
    """
    Error producido durante la validación de un Value Object.
    """


class ConfigurationError(CoreError):
    """
    Error de configuración de un componente del Core.
    """


class FactoryError(CoreError):
    """
    Error producido por una fábrica del Core.
    """


class StrategyError(CoreError):
    """
    Error producido por una estrategia del Core.
    """
