"""
Space AI 2.0

Rolling Window

Implementación oficial de ventanas deslizantes del proyecto.

Responsabilidades:

- Administrar una ventana deslizante.
- Mantener una capacidad máxima.
- Exponer acceso seguro a los datos.
- Proporcionar una API Pythonic.

Esta clase no realiza cálculos estadísticos.
Toda la lógica matemática pertenece a Statistics.

Python 3.12
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

from core.validator import Validator

T = TypeVar("T")


class RollingWindow(Generic[T]):
    """
    Ventana deslizante genérica.

    Mantiene los últimos N elementos insertados.

    Cuando la capacidad máxima es alcanzada,
    el elemento más antiguo es descartado automáticamente.
    """

    def __init__(
        self,
        capacity: int,
    ) -> None:
        """
        Inicializa una nueva ventana.

        Args:
            capacity:
                Capacidad máxima de la ventana.

        Raises:
            ValidationError:
                Si la capacidad es inválida.
        """

        Validator.validate_integer(capacity)
        Validator.validate_positive(capacity)

        self._capacity: int = capacity

        self._data: deque[T] = deque(maxlen=capacity)

    @property
    def capacity(self) -> int:
        """
        Retorna la capacidad máxima.

        Returns:
            Capacidad.
        """

        return self._capacity

    @property
    def size(self) -> int:
        """
        Retorna el número de elementos
        almacenados actualmente.

        Returns:
            Cantidad de elementos.
        """

        return len(self)

    def is_empty(self) -> bool:
        """
        Indica si la ventana está vacía.

        Returns:
            True si está vacía.
        """

        return len(self._data) == 0

    def is_full(self) -> bool:
        """
        Indica si la ventana alcanzó
        su capacidad máxima.

        Returns:
            True si está llena.
        """

        return len(self._data) == self._capacity

    def clear(self) -> None:
        """
        Elimina todos los elementos
        de la ventana.
        """

        self._data.clear()

    def __len__(self) -> int:
        """
        Retorna la cantidad de elementos.

        Permite utilizar:

            len(window)
        """

        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """
        Retorna un iterador sobre la ventana.

        Permite:

            for value in window
        """

        return iter(self._data)

    def __contains__(
        self,
        item: object,
    ) -> bool:
        """
        Permite:

            value in window
        """

        return item in self._data

    def __getitem__(
        self,
        index: int,
    ) -> T:
        """
        Acceso mediante índices.

        Soporta índices negativos.

        Args:
            index:
                Posición solicitada.

        Returns:
            Elemento correspondiente.

        Raises:
            ValidationError:
                Si el índice es inválido.
        """

        Validator.validate_integer(index)

        if self.is_empty():
            Validator.validate_not_empty(self._data)

        try:
            return self._data[index]

        except IndexError as exc:
            raise IndexError(f"Index {index} is out of range.") from exc

    def __repr__(self) -> str:
        """
        Representación informal.
        """

        return (
            f"{self.__class__.__name__}"
            f"(capacity={self._capacity}, "
            f"size={len(self)}, "
            f"values={tuple(self._data)})"
        )

    def append(
        self,
        value: T,
    ) -> None:
        """
        Inserta un nuevo elemento.

        Si la ventana está llena,
        el elemento más antiguo será
        descartado automáticamente.

        Args:
            value:
                Elemento a insertar.
        """

        Validator.validate_not_none(value)

        self._data.append(value)

    def extend(
        self,
        values: Iterable[T],
    ) -> None:
        """
        Inserta múltiples elementos.

        Args:
            values:
                Colección de elementos.
        """

        for value in values:
            Validator.validate_not_none(value)

            self._data.append(value)

    def first(self) -> T:
        """
        Retorna el primer elemento.

        Returns:
            Primer elemento.

        Raises:
            ValidationError:
                Si la ventana está vacía.
        """

        Validator.validate_not_empty(self._data)

        return self._data[0]

    def latest(self) -> T:
        """
        Retorna el elemento más reciente.

        Returns:
            Último elemento.

        Raises:
            ValidationError:
                Si la ventana está vacía.
        """

        Validator.validate_not_empty(self._data)

        return self._data[-1]

    def at(
        self,
        index: int,
    ) -> T:
        """
        Retorna el elemento ubicado
        en una posición específica.

        Args:
            index:
                Posición.

        Returns:
            Elemento solicitado.
        """

        return self[index]

    def last(
        self,
        count: int,
    ) -> tuple[T, ...]:
        """
        Retorna los últimos N elementos.

        Args:
            count:
                Cantidad solicitada.

        Returns:
            Tupla con los elementos.

        Raises:
            ValidationError:
                Si count es inválido.
        """

        Validator.validate_integer(count)
        Validator.validate_positive(count)

        if count > len(self):
            count = len(self)

        return tuple(self._data)[-count:]

    def copy(self) -> RollingWindow[T]:
        """
        Crea una copia independiente de la ventana.

        Returns:
            Nueva instancia con los mismos datos.
        """

        window = RollingWindow[T](self._capacity)

        window.extend(self._data)

        return window

    def to_tuple(self) -> tuple[T, ...]:
        """
        Retorna una copia inmutable.

        Returns:
            Tupla.
        """

        return tuple(self._data)

    def __eq__(
        self,
        other: object,
    ) -> bool:
        """
        Compara dos ventanas.

        Returns:
            True si poseen la misma capacidad
            y los mismos elementos.
        """

        if not isinstance(other, RollingWindow):
            return False

        return self._capacity == other._capacity and tuple(self._data) == tuple(
            other._data
        )

    def __bool__(self) -> bool:
        """
        Permite:

            if window:
                ...

        Returns:
            True si contiene elementos.
        """

        return not self.is_empty()

    @property
    def remaining_capacity(self) -> int:
        """
        Espacio restante.

        Returns:
            Capacidad disponible.
        """

        return self._capacity - len(self)

    def __str__(self) -> str:
        """
        Representación amigable.

        Returns:
            Cadena.
        """

        return str(tuple(self._data))
