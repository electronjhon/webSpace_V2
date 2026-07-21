from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from ia.decision_engine.decision_engine import DecisionEngine
from ia.integration.browser.browser_adapter import BrowserAdapter
from ia.integration.collector.collector import Collector
from ia.integration.collector.rolling_window_builder import (
    RollingWindowBuilder,
)
from ia.learning_engine.learning_engine import LearningEngine
from ia.signal_engine.signal_engine import SignalEngine
from predictor.predictor_engine import PredictorEngine
from state_engine.state_engine import StateEngine

if TYPE_CHECKING:
    from ia.pipeline.pipeline import AIPipeline


@dataclass(
    frozen=True,
    slots=True,
    kw_only=True,
)
class ApplicationContext:
    """
    Immutable runtime context.

    Holds every application service with lifecycle or state.

    Static façade classes (FeatureEngine and DashboardEngine)
    are intentionally excluded because they do not require
    instantiation.
    """

    browser_adapter: BrowserAdapter

    collector: Collector

    rolling_window_builder: RollingWindowBuilder

    pipeline: AIPipeline

    state_engine: StateEngine

    predictor_engine: PredictorEngine

    decision_engine: DecisionEngine

    signal_engine: SignalEngine

    learning_engine: LearningEngine
