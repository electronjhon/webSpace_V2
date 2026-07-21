from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class StateId:
    """
    Immutable identifier for a State entity.

    This value object encapsulates the UUID used to uniquely identify
    a state within the StateEngine.
    """

    value: UUID

    @classmethod
    def generate(cls) -> StateId:
        """
        Generates a new unique StateId.

        Returns:
            A new immutable StateId instance.
        """
        return cls(value=uuid4())

    @classmethod
    def from_uuid(cls, value: UUID) -> StateId:
        """
        Creates a StateId from an existing UUID.

        Args:
            value:
                UUID to encapsulate.

        Returns:
            A StateId instance.
        """
        return cls(value=value)

    @classmethod
    def from_string(cls, value: str) -> StateId:
        """
        Creates a StateId from its string representation.

        Args:
            value:
                UUID string.

        Returns:
            A StateId instance.

        Raises:
            ValueError:
                If the string is not a valid UUID.
        """
        return cls(value=UUID(value))

    def __str__(self) -> str:
        return str(self.value)
