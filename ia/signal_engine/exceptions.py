"""
Space AI 2.0
Signal Engine

Jerarquía de excepciones oficial del Signal Engine.

Todas las excepciones específicas del motor deben heredar de
SignalEngineError para facilitar un manejo uniforme por parte
de los componentes superiores del sistema.

Sprint:
    Sprint 7

Versión:
    1.0.0
"""

from __future__ import annotations


class SignalEngineError(Exception):
    """
    Excepción base del Signal Engine.
    """

    pass


class SignalConfigurationError(SignalEngineError):
    """
    Error en la configuración del Signal Engine.
    """

    pass


class SignalContextError(SignalEngineError):
    """
    Error relacionado con la construcción o validación
    del SignalContext.
    """

    pass


class SignalValidationError(SignalEngineError):
    """
    Error producido durante la validación de una señal.
    """

    pass


class SignalGenerationError(SignalEngineError):
    """
    Error ocurrido durante la generación de una señal.
    """

    pass


class SignalStrategyError(SignalEngineError):
    """
    Error producido por una estrategia de generación
    de señales.
    """

    pass


class SignalFactoryError(SignalEngineError):
    """
    Error producido al crear una estrategia mediante
    la fábrica correspondiente.
    """

    pass


class UnsupportedSignalStrategyError(SignalFactoryError):
    """
    Se solicita una estrategia que no está registrada
    o no es compatible.
    """

    pass


class InvalidSignalError(SignalValidationError):
    """
    La señal generada no cumple las reglas de
    consistencia del dominio.
    """

    pass


class SignalExecutionError(SignalEngineError):
    """
    Error inesperado durante la ejecución del
    Signal Engine.
    """

    pass
