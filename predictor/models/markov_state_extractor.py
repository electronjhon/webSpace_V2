from __future__ import annotations

from predictor.models.markov_state import MarkovState
from state_engine.state import State


class MarkovStateExtractor:
    """
    Convierte un State del dominio en un MarkovState.
    """

    @staticmethod
    def extract(state: State) -> MarkovState:
        return MarkovState(
            labels=state.labels,
        )
