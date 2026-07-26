"""
Space AI 2.0

Application Bootstrap

Responsible for constructing the application runtime
context.

The bootstrap owns the creation of every service with
lifecycle while keeping the application completely
decoupled from dependency construction.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ia.application.models.application_configuration import (
    ApplicationConfiguration,
)
from ia.application.models.application_context import (
    ApplicationContext,
)
from ia.decision_engine.decision_engine import DecisionEngine
from ia.decision_engine.decision_strategy_configuration import (
    DecisionStrategyConfiguration,
)
from ia.integration.browser.browser_adapter import BrowserAdapter
from ia.integration.browser.browser_session import BrowserSession
from ia.integration.browser.playwright_adapter import (
    PlaywrightAdapter,
)
from ia.integration.collector.collector import Collector
from ia.integration.collector.rolling_window_builder import (
    RollingWindowBuilder,
)
from ia.learning_engine.learning_engine import LearningEngine
from ia.learning_engine.repository.learning_repository import (
    LearningRepository,
)
from ia.pipeline.pipeline import AIPipeline
from ia.signal_engine.signal_engine import SignalEngine
from predictor.predictor_engine import PredictorEngine
from state_engine.state_engine import StateEngine


@dataclass(slots=True)
class ApplicationBootstrap:
    """
    Builds the application runtime context.

    This class is responsible only for dependency
    construction.
    """

    application_configuration: ApplicationConfiguration

    decision_configuration: DecisionStrategyConfiguration

    learning_repository: LearningRepository

    _context: ApplicationContext | None = field(
        default=None,
        init=False,
        repr=False,
    )

    @property
    def context(self) -> ApplicationContext:
        """
        Returns the initialized application context.
        """
        if self._context is None:
            raise RuntimeError(
                "Application context has not been initialized.",
            )

        return self._context

    def initialize(self) -> None:
        """
        Builds every application service.
        """

        browser_adapter = self._build_browser_adapter()

        collector = self._build_collector(
            browser_adapter,
        )

        rolling_window_builder = self._build_rolling_window_builder()

        state_engine = self._build_state_engine()

        predictor_engine = self._build_predictor_engine()

        decision_engine = self._build_decision_engine()

        signal_engine = self._build_signal_engine()

        learning_engine = self._build_learning_engine()

        pipeline = self._build_pipeline(
            state_engine=state_engine,
            predictor_engine=predictor_engine,
            decision_engine=decision_engine,
            signal_engine=signal_engine,
            learning_engine=learning_engine,
        )

        self._context = ApplicationContext(
            browser_adapter=browser_adapter,
            collector=collector,
            rolling_window_builder=rolling_window_builder,
            pipeline=pipeline,
            state_engine=state_engine,
            predictor_engine=predictor_engine,
            decision_engine=decision_engine,
            signal_engine=signal_engine,
            learning_engine=learning_engine,
        )

    def _build_browser_session(
        self,
    ) -> BrowserSession:
        """
        Build the Browser Session.
        """

        return BrowserSession(
            cdp_url=self.application_configuration.cdp_url,
        )

    def _build_browser_adapter(
        self,
    ) -> BrowserAdapter:
        """
        Build the Browser Adapter.
        """

        return PlaywrightAdapter(
            session=self._build_browser_session(),
        )

    def _build_collector(
        self,
        adapter: BrowserAdapter,
    ) -> Collector:
        """
        Build the Collector.
        """

        return Collector(
            adapter=adapter,
        )

    def _build_state_engine(
        self,
    ) -> StateEngine:
        """
        Build the State Engine.
        """

        return StateEngine()

    def _build_predictor_engine(
        self,
    ) -> PredictorEngine:
        """
        Build the Predictor Engine.
        """

        return PredictorEngine()

    def _build_decision_engine(
        self,
    ) -> DecisionEngine:
        """
        Build the Decision Engine.
        """

        return DecisionEngine(
            configuration=self.decision_configuration,
        )

    def _build_signal_engine(
        self,
    ) -> SignalEngine:
        """
        Build the Signal Engine.
        """

        return SignalEngine()

    def _build_learning_engine(
        self,
    ) -> LearningEngine:
        """
        Build the Learning Engine.
        """

        return LearningEngine(
            repository=self.learning_repository,
        )

    def _build_pipeline(
        self,
        *,
        state_engine: StateEngine,
        predictor_engine: PredictorEngine,
        decision_engine: DecisionEngine,
        signal_engine: SignalEngine,
        learning_engine: LearningEngine,
    ) -> AIPipeline:
        """
        Build the AI Pipeline.
        """

        return AIPipeline(
            state_engine=state_engine,
            predictor_engine=predictor_engine,
            decision_engine=decision_engine,
            signal_engine=signal_engine,
            learning_engine=learning_engine,
            prediction_strategy=(self.application_configuration.prediction_strategy),
        )

    def _build_rolling_window_builder(
        self,
    ) -> RollingWindowBuilder:
        """
        Build the Rolling Window Builder.
        """

        return RollingWindowBuilder(
            window_size=self.application_configuration.rolling_window_size,
        )
