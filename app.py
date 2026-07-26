"""
Space AI 2.0

Application Entry Point
"""

from config.constants import SHORT_WINDOW
from ia.application.bootstrap import ApplicationBootstrap
from ia.application.composition import create_application
from ia.application.models.application_configuration import (
    ApplicationConfiguration,
)
from ia.decision_engine.decision_strategy_configuration import (
    DecisionStrategyConfiguration,
)
from ia.decision_engine.strategies.strategy_type import (
    DecisionStrategyType,
)
from ia.learning_engine.history.result_history import ResultHistory
from ia.learning_engine.repository.learning_repository import (
    LearningRepository,
)

CDP_URL = "http://127.0.0.1:9222"


def _build_application_configuration() -> ApplicationConfiguration:
    """
    Build the application runtime configuration.
    """

    return ApplicationConfiguration(
        cdp_url=CDP_URL,
        rolling_window_size=SHORT_WINDOW,
    )


def _build_decision_configuration() -> DecisionStrategyConfiguration:
    """
    Build the default decision strategy configuration.
    """

    return DecisionStrategyConfiguration(
        strategy_type=DecisionStrategyType.RULE_BASED,
        rules=(),
    )


def _build_learning_repository() -> LearningRepository:
    """
    Build the initial in-memory learning repository.
    """

    return LearningRepository(
        history=ResultHistory(),
    )


def _build_bootstrap() -> ApplicationBootstrap:
    """
    Build the application bootstrap dependencies.
    """

    return ApplicationBootstrap(
        application_configuration=_build_application_configuration(),
        decision_configuration=_build_decision_configuration(),
        learning_repository=_build_learning_repository(),
    )


def main() -> None:
    """
    Create and run the Space AI application.
    """

    application = create_application(
        _build_bootstrap(),
    )

    try:
        application.initialize()
        application.run()
    finally:
        application.shutdown()


if __name__ == "__main__":
    main()
