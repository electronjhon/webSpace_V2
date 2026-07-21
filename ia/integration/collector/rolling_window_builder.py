"""
Space AI 2.0

Rolling Window Builder

Transforms a stream of RoundObservation objects into
fixed-size RollingWindow instances consumed by the
Feature Engine.

This component belongs to the integration layer and
contains no analytical or business logic.

Author: Space AI 2.0
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from core.types import Number
from core.windows import RollingWindow
from ia.integration.models.round_observation import (
    RoundObservation,
)


@dataclass(slots=True)
class RollingWindowBuilder:
    """
    Builds immutable rolling windows from incoming
    observations.

    The builder maintains an internal fixed-size buffer
    containing only the numeric multiplier extracted from
    each RoundObservation.

    Once the configured window size is reached, a new
    immutable RollingWindow is produced for every incoming
    observation.
    """

    window_size: int

    _window: RollingWindow[Number] = field(
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        """
        Initialize the internal rolling window.
        """

        if self.window_size <= 0:
            raise ValueError(
                "window_size must be greater than zero.",
            )

        self._window = RollingWindow[Number](
            self.window_size,
        )

    def append(
        self,
        observation: RoundObservation,
    ) -> RollingWindow[Number] | None:
        """
        Add a new observation.
        """

        self._window.append(
            observation.multiplier,
        )

        if not self._window.is_full():
            return None

        return self._window.copy()

    def build(
        self,
        observations: Iterator[RoundObservation],
    ) -> Iterator[RollingWindow[Number]]:
        """
        Transform an observation stream into rolling
        windows.

        Parameters
        ----------
        observations:
            Source observation iterator.

        Yields
        ------
        RollingWindow[Number]
            Immutable rolling windows.
        """

        for observation in observations:

            window = self.append(
                observation,
            )

            if window is not None:
                yield window
