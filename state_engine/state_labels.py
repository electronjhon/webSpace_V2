from __future__ import annotations

from dataclasses import dataclass

from state_engine.labels.balance_label import BalanceLabel
from state_engine.labels.compression_label import CompressionLabel
from state_engine.labels.entropy_label import EntropyLabel
from state_engine.labels.momentum_label import MomentumLabel
from state_engine.labels.trend_label import TrendLabel
from state_engine.labels.volatility_label import VolatilityLabel


@dataclass(frozen=True, slots=True)
class StateLabels:
    """
    Immutable value object that groups all classification dimensions
    describing a system state.

    Each dimension is independent and represents a different aspect of
    the analyzed sequence. Together they define the semantic meaning of
    a state within the StateEngine.
    """

    trend: TrendLabel
    momentum: MomentumLabel
    entropy: EntropyLabel
    compression: CompressionLabel
    balance: BalanceLabel
    volatility: VolatilityLabel
