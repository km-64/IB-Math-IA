from numba import njit, prange
import numpy as np
import sampling

@njit
def game_turns_tr(target_rolls: int, early_stop: bool) -> int:
    turns: int = 0
    total: int = 0
    while total < 100:
        turn_total: int = 0
        for r in range(target_rolls):
            dice = sampling.roll_dice()
            if np.array_equal(dice, np.ones_like(dice)):
                turn_total = 0
                total = 0
                break
            elif np.any(dice[:] == 1):
                turn_total = 0
                break
            else:
                turn_total += dice.sum()
                if early_stop and turn_total >= 100 - total: break
        turns += 1
        total += turn_total
    return turns


@njit
def game_turns_ts(target_score: int, early_stop: bool) -> int:
    turns: int = 0
    total: int = 0
    while total < 100:
        turn_total: int = 0
        while turn_total < target_score:
            dice = sampling.roll_dice()
            if np.array_equal(dice, np.ones_like(dice)):
                turn_total = 0
                total = 0
                break
            elif np.any(dice[:] == 1):
                turn_total = 0
                break
            else:
                turn_total += dice.sum()
                if early_stop and turn_total >= 100 - total: break
        turns += 1
        total += turn_total
    return turns
