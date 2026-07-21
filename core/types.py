"""
Space AI 2.0

Core Types

Shared type aliases used throughout the project.

Keeping common aliases in a single module ensures
consistent typing across all engines.
"""

from collections.abc import Sequence

type Number = int | float

type NumericSequence = Sequence[Number]
