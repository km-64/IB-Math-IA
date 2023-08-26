import numpy as np
from functools import lru_cache
import sampling

p = sampling.p


@lru_cache(maxsize=10000)
def P(r: int, x: int) -> float:
    if r == 1:
        if x > 12: return 0
        else: return p[x]
    else:
        if x == 0:
            return P(r - 1, 0) + p[0] * sum(
                [P(r - 1, i) for i in range(4 * (r - 1), 12 * (r - 1))]
            )
        else:
            return sum(
                [p[x - i] * P(r - 1, i) for i in range(max(x - 12, 4), x - 4 + 1)]
            )

def E(r: int) -> float:
    return sum([i * P(r, i) for i in range(4 * r, 12 * r + 1)])

@lru_cache(maxsize=10000)
def Ps(r: int, x: int, s: int) -> float:
    if r == 1:
        if x > 12: return 0
        else: return p[x]
    else:
        if x == 0:
            return Ps(r - 1, 0, s) + p[0] * sum(
                [Ps(r - 1, i, s) for i in range(4 * (r - 1), 12 * (r - 1))]
            )
        if x < s:
            return sum(
                [Ps(r - 1, i, s) * p[x - i] for i in range(max(x - 12, 4), x - 4 + 1)]
            )
        else:
            return Ps(r - 1, x, s) + sum(
                [
                    p[x - i] * Ps(r - 1, i, s)
                    for i in range(max(x - 12, 4), min(x - 4, s - 1) + 1)
                ]
            )


def Es(s: int) -> float:
    r = np.ceil(s / 4)
    return sum([i * Ps(r, i, s) for i in range(s, s + 12 + 1)])
