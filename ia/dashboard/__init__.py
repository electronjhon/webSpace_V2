"""
Space AI 2.0

Dashboard

Expone la API pública del Dashboard.

El Dashboard constituye la capa de presentación consolidada
del sistema de inteligencia artificial y proporciona una
única fachada pública para la construcción de snapshots del
estado global.

Sprint:
    9

Versión:
    1.0.0
"""

from .dashboard_engine import DashboardEngine

__all__ = [
    "DashboardEngine",
]
