"""
Space AI 2.0

Core - Value Objects

Define el contrato base para todos los Value Objects del dominio.

Un Value Object representa un concepto definido únicamente por
sus valores, es inmutable y no posee identidad propia.

Los Value Objects concretos son responsables de definir su
estructura mediante dataclasses inmutables y de implementar
las invariantes propias de su dominio.

Sprint:
    7

Versión:
    1.0.0
"""

from __future__ import annotations


class ValueObject:
    """
    Contrato base para todos los Value Objects del dominio.

    Esta clase actúa como marcador arquitectónico para identificar
    objetos que representan conceptos del dominio definidos por
    sus valores y no por una identidad.

    Responsabilidades
    -----------------
    - Servir como raíz común de los Value Objects.
    - Proporcionar una abstracción explícita del dominio.
    - Facilitar la extensibilidad futura del Core.

    Notas
    -----
    - No define atributos.
    - No implementa comportamiento.
    - Las clases derivadas son responsables de utilizar
      ``@dataclass(frozen=True, slots=True, kw_only=True)``
      cuando corresponda.
    """

    __slots__: tuple[str, ...] = ()
