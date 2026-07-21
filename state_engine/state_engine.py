"""
Space AI 2.0

State Engine

Facade responsible for transforming FeatureVectors into
immutable state histories.
"""

from __future__ import annotations

from datetime import datetime

from feature_engine.models.feature_vector import FeatureVector
from state_engine.classifiers.base_classifier import BaseStateClassifier
from state_engine.classifiers.rule_classifier import RuleStateClassifier
from state_engine.models.state_engine_result import StateEngineResult
from state_engine.state_history import StateHistory
from state_engine.state_machine import StateMachine


class StateEngine:
    """
    Facade for the State Engine.

    Coordinates the classifier and the StateMachine while
    remaining completely free of business logic.
    """

    def __init__(
        self,
        classifier: BaseStateClassifier | None = None,
        state_machine: StateMachine | None = None,
    ) -> None:
        self._classifier = RuleStateClassifier() if classifier is None else classifier

        self._state_machine = StateMachine() if state_machine is None else state_machine

    def process(
        self,
        history: StateHistory,
        features: FeatureVector,
        timestamp: datetime | None = None,
    ) -> StateEngineResult:
        """
        Processes a FeatureVector.

        Returns
        -------
        StateEngineResult
            Immutable object containing the generated
            ClassificationResult and the updated
            StateHistory.
        """

        classification = self._classifier.classify(
            features,
        )

        updated_history = self._state_machine.build(
            history=history,
            labels=classification.labels,
            timestamp=self._resolve_timestamp(
                timestamp,
            ),
        )

        return StateEngineResult(
            classification=classification,
            history=updated_history,
        )

    @staticmethod
    def _resolve_timestamp(
        timestamp: datetime | None,
    ) -> datetime:
        """
        Resolve the timestamp used by the StateMachine.
        """

        return datetime.now() if timestamp is None else timestamp


__all__ = [
    "StateEngine",
]
