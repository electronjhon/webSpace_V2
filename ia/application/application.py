"""
Space AI 2.0

Application Lifecycle

Coordinates the lifecycle of the Space AI application.

The application layer contains no business logic.
Its only responsibility is coordinating initialization,
execution and shutdown using an immutable
ApplicationContext.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ia.application.enums import ApplicationState
from ia.application.exceptions import (
    ApplicationInitializationError,
    ApplicationRuntimeError,
)
from ia.application.models.application_context import (
    ApplicationContext,
)


@dataclass(slots=True)
class SpaceAIApplication:
    """
    Coordinates the application lifecycle.

    The application never creates dependencies.
    Every required service is provided through an
    immutable ApplicationContext.
    """

    context: ApplicationContext

    _state: ApplicationState = field(
        default=ApplicationState.CREATED,
        init=False,
        repr=False,
    )

    @property
    def state(self) -> ApplicationState:
        """
        Returns the current lifecycle state.
        """
        return self._state

    @property
    def is_initialized(self) -> bool:
        """
        Indicates whether the application has been
        initialized.
        """
        return self._state is not ApplicationState.CREATED

    def initialize(self) -> None:
        """
        Initializes the application.
        """
        if self._state is not ApplicationState.CREATED:
            raise ApplicationInitializationError(
                "The application has already been initialized.",
            )

        self.context.collector.connect()

        self._state = ApplicationState.INITIALIZED

    def run(self) -> None:
        """
        Starts the application lifecycle.
        """
        if self._state is not ApplicationState.INITIALIZED:
            raise ApplicationRuntimeError(
                "The application must be initialized before execution.",
            )

        self._state = ApplicationState.RUNNING

        for window in self.context.rolling_window_builder.build(
            self.context.collector.observations(),
        ):
            #
            # Delegate the complete AI processing to
            # the pipeline.
            #
            self.context.pipeline.process(
                window,
            )

    def shutdown(self) -> None:
        """
        Gracefully shuts down the application.
        """

        if self.context.collector.is_connected():
            self.context.collector.disconnect()

        self._state = ApplicationState.STOPPED
