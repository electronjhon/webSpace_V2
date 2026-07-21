"""
Space AI 2.0

Core Exceptions

Jerarquía oficial de excepciones del proyecto.

Todas las excepciones de Space AI deben heredar de SpaceAIError.
Esto permite capturar cualquier error propio del sistema mediante
una única excepción base.
"""

from __future__ import annotations


class SpaceAIError(Exception):
    """
    Excepción base de Space AI.

    Todas las excepciones específicas del proyecto deben heredar
    de esta clase.
    """


class ValidationError(SpaceAIError):
    """
    Error producido cuando una validación falla.
    """


class ConfigurationError(SpaceAIError):
    """
    Error de configuración del sistema.
    """


class DatabaseError(SpaceAIError):
    """
    Error relacionado con la base de datos.
    """


class CollectorError(SpaceAIError):
    """
    Error producido durante la captura de datos.
    """


class FeatureEngineError(SpaceAIError):
    """
    Error producido dentro del FeatureEngine.
    """


class StateEngineError(SpaceAIError):
    """
    Error producido dentro del StateEngine.
    """


class LearningEngineError(SpaceAIError):
    """
    Error producido dentro del LearningEngine.
    """


class DecisionEngineError(SpaceAIError):
    """
    Error producido dentro del DecisionEngine.
    """


class DashboardError(SpaceAIError):
    """
    Error producido dentro del Dashboard.
    """
