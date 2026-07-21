"""
Space AI 2.0 - Dashboard Exceptions

Define la jerarquía de excepciones específica del Dashboard.

El Dashboard constituye la capa de agregación y visualización del sistema,
por lo que dispone de excepciones propias para desacoplar el manejo de
errores del resto de los motores.

Principios:
- Bajo acoplamiento.
- Alta cohesión.
- Excepciones específicas por dominio.
"""

from __future__ import annotations


class DashboardError(Exception):
    """
    Excepción base del módulo Dashboard.

    Todas las excepciones específicas del Dashboard deben heredar de esta
    clase para permitir un manejo unificado de errores.
    """


class DashboardConfigurationError(DashboardError):
    """
    Error relacionado con la configuración del Dashboard.
    """


class DashboardRepositoryError(DashboardError):
    """
    Error producido durante la consulta de información mediante el
    DashboardRepository.
    """


class DashboardAggregationError(DashboardError):
    """
    Error producido durante la agregación de información proveniente de
    uno o varios motores del sistema.
    """


class DashboardSnapshotError(DashboardError):
    """
    Error producido durante la construcción o validación de un
    DashboardSnapshot.
    """
