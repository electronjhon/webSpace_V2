"""
Space AI 2.0

Learning Engine

Feedback History

Gestiona el historial inmutable de Feedback generados
por el Learning Engine.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from ia.learning_engine.models.feedback import Feedback


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class FeedbackHistory:
    """
    Historial inmutable de Feedback.
    """

    feedbacks: tuple[Feedback, ...] = field(
        default_factory=tuple,
    )

    @property
    def size(self) -> int:
        """
        Número de elementos almacenados.
        """

        return len(self.feedbacks)

    @property
    def is_empty(self) -> bool:
        """
        Indica si el historial está vacío.
        """

        return not self.feedbacks

    def append(
        self,
        feedback: Feedback,
    ) -> FeedbackHistory:
        """
        Devuelve un nuevo historial con el Feedback agregado.
        """

        return FeedbackHistory(
            feedbacks=(
                *self.feedbacks,
                feedback,
            ),
        )

    def __iter__(self) -> Iterator[Feedback]:
        """
        Iterador sobre los elementos del historial.
        """

        return iter(self.feedbacks)

    def __len__(self) -> int:
        """
        Número de elementos almacenados.
        """

        return self.size


__all__ = [
    "FeedbackHistory",
]
