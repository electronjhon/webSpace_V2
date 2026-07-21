"""
Space AI 2.0

Base Extractor

Abstract generic contract shared by every
FeatureEngine extractor.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from core.types import Number
from core.validator import Validator
from core.windows import RollingWindow

FeatureT = TypeVar("FeatureT")


class BaseExtractor(
    ABC,
    Generic[FeatureT],
):
    """
    Abstract generic base class for every
    FeatureEngine extractor.
    """

    @classmethod
    @abstractmethod
    def extract(
        cls,
        window: RollingWindow[Number],
    ) -> FeatureT:
        """
        Extracts a feature model from the
        supplied rolling window.
        """
        raise NotImplementedError

    @staticmethod
    def values(
        window: RollingWindow[Number],
    ) -> tuple[Number, ...]:
        """
        Returns an immutable snapshot of
        the rolling window.
        """

        Validator.validate_not_none(window)

        values = window.to_tuple()

        Validator.validate_not_empty(values)

        return values

    @staticmethod
    def window_size(
        window: RollingWindow[Number],
    ) -> int:
        """
        Returns the current window size.
        """

        Validator.validate_not_none(window)

        return len(window)
