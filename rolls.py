import numpy as np
from numba import njit
import sampling

@njit
def roll_turn_tr(target_rolls: int) -> int:
    total: int = 0
    for r in range(target_rolls):
        dice = sampling.roll_dice()
        if np.any(dice[:] == 1): return 0
        total += dice.sum()
    return total

@njit
def roll_turn_ts(target_score: int) -> int:
    total: int = 0
    while total < target_score:
        dice = sampling.roll_dice()
        if np.any(dice[:] == 1): return 0
        total += dice.sum()
    return total
