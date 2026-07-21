"""
Space AI 2.0

Learning Engine

Exceptions

Define las excepciones específicas del dominio del
Learning Engine.

Sprint:
    8

Versión:
    1.0.0
"""

from __future__ import annotations


class LearningEngineError(Exception):
    """
    Excepción base del Learning Engine.
    """


class InvalidObservedOutcomeError(LearningEngineError):
    """
    Se produce cuando un ObservedOutcome viola
    una invariante del dominio.
    """


class InvalidFeedbackError(LearningEngineError):
    """
    Se produce cuando un Feedback contiene
    información inconsistente.
    """


class InvalidLearningRecordError(LearningEngineError):
    """
    Se produce cuando un LearningRecord no
    cumple las reglas del dominio.
    """


class InvalidLearningSnapshotError(LearningEngineError):
    """
    Se produce cuando un LearningSnapshot
    contiene un estado inválido.
    """


__all__ = [
    "LearningEngineError",
    "InvalidObservedOutcomeError",
    "InvalidFeedbackError",
    "InvalidLearningRecordError",
    "InvalidLearningSnapshotError",
]
