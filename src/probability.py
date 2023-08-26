import numpy as np
from numba import njit, prange
import rolls

@njit(parallel=True)
def p_losing_turn(target_rolls: int, trials: int = 100_000) -> float:
    total: int = 0
    for t in prange(trials):
        total += 0 if rolls.roll_turn_tr(target_rolls) > 0 else 1
    return total / trials
