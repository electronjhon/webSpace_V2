from __future__ import annotations

from abc import ABC, abstractmethod

from feature_engine.models.feature_vector import FeatureVector
from state_engine.models.classification_result import ClassificationResult


class BaseStateClassifier(ABC):
    """
    Base contract for all state classifiers.

    A classifier is responsible for transforming a FeatureVector into
    a semantic ClassificationResult. Implementations may rely on
    deterministic rules, machine learning models or hybrid approaches.

    Classifiers are intentionally stateless.
    """

    @abstractmethod
    def classify(
        self,
        features: FeatureVector,
    ) -> ClassificationResult:
        """
        Classifies a feature vector.

        Args:
            features:
                Complete feature vector produced by the FeatureEngine.

        Returns:
            ClassificationResult describing the semantic state.
        """
        raise NotImplementedError
