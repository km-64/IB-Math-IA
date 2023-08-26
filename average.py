import numpy as np
from numba import njit, prange

import rolls, game

@njit(parallel=True)
def avg_roll_tr(target_rolls: int, trials: int = 100_000) -> float:
    running_total: int = 0
    for t in prange(trials):
        running_total += rolls.roll_turn_tr(target_rolls)
    return running_total / trials

@njit(parallel=True)
def avg_roll_ts(target_score: int, trials: int = 100_000) -> float:
    running_total: int = 0
    for t in prange(trials):
        running_total += rolls.roll_turn_ts(target_score)
    return running_total / trials


# Average number of rolls, target rolls
@njit(parallel=True)
def avg_turns_tr(target_rolls: int, early_stop: bool = True, trials: int = 100_000):
    running_total: int = 0
    for t in prange(trials):
        running_total += game.game_turns_tr(target_rolls, early_stop)
    return running_total / trials


@njit(parallel=True)
def avg_turns_ts(target_score: int, early_stop: bool = True, trials: int = 100_000):
    running_total: int = 0
    for t in prange(trials):
        running_total += game.game_turns_ts(target_score, early_stop)
    return running_total / trials