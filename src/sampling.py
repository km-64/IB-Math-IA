import numpy as np
from numba import njit


# Unbiased die
p_d1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
p_d2 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]

# Lower-biased die
#p_d1 = [i/21 for i in reversed(range(1,6+1))]
#p_d2 = [i/21 for i in reversed(range(1,6+1))]

# Center-biased die
#p_d1 = [i/12 for i in (1,2,3,3,2,1)]
#p_d2 = [i/12 for i in (1,2,3,3,2,1)]

# Upper-biased die
#p_d1 = [i / 21 for i in range(1, 6 + 1)]
#p_d2 = [i / 21 for i in range(1, 6 + 1)]


assert len(p_d1) == len(p_d2)

p_grid = np.array([[p_d1[i] * p_d2[j] for j in range(6)] for i in range(6)])
p = (
    [p_grid[0][0] + p_grid[:, 0][1:].sum() + p_grid[0, :][1:].sum()]
    + [0] * 3
    + [
        np.trace(np.flip(p_grid[1:, 1:], axis=1), offset=o)
        for o in reversed(range(-4, 4 + 1))
    ]
)

cd_d1 = np.cumsum([0] + p_d1) / np.cumsum([0] + p_d1)[-1]
cd_d2 = np.cumsum([0] + p_d2) / np.cumsum([0] + p_d2)[-1]

cd_d1 = np.cumsum([0] + p_d1) / np.cumsum([0] + p_d1)[-1]
cd_d2 = np.cumsum([0] + p_d2) / np.cumsum([0] + p_d2)[-1]

@njit
def roll_dice() -> np.array:
    u1, u2 = np.random.rand(1), np.random.rand(1)
    idx_1 = np.searchsorted(cd_d1, u1, side="right")
    idx_2 = np.searchsorted(cd_d1, u2, side="right")
    return np.concatenate((idx_1, idx_2))
