import pandas as pd
import numpy as np
import os, sys

import average, probability, sampling
import recursion
from tqdm.auto import tqdm, trange

save_path = ''

def save_df(data: dict, name: str):
    df = pd.DataFrame(data)
    os.makedirs(save_path, exist_ok=True)
    df.to_csv(os.path.join(save_path, f"{name}.csv"), index=False)
    
    return df

def table_1() -> pd.DataFrame:
    print("Generating Table 1")
    data = {"x": [x for x in range(12 + 1)], "P(X1=x)": sampling.p}
    df = save_df(data, "Table_1")
    print(df)
    return df

def table_2(max_r: int = 25, sim_mag=[3, 4, 6]) -> pd.DataFrame:
    print("Generating Table 2")
    data = {
        "r": [r for r in range(1, max_r + 1)],
        "E(Xr)": [
            recursion.E(1) * r * (1 - sampling.p[0]) ** (r - 1)
            for r in range(1, max_r + 1)
        ],
    }

    for mag in tqdm(sim_mag, desc="Table 2"):
        sim = [average.avg_roll_tr(r, 10**mag) for r in range(1, max_r + 1)]
        data[f"Simulation (10e{mag})"] = sim

    df = save_df(data, "Table_2")
    print(df)
    return df

def table_3(max_r: int = 15) -> pd.DataFrame:
    print("Generating Table 3")
    data = {
        "r": [r for r in range(1, max_r + 1)],
        "Estimated Turns": [100 / recursion.E(r) for r in range(1, max_r + 1)],
        "Sim Avg (10e3)": [
            average.avg_turns_tr(tr, early_stop=True, trials=10**3)
            for tr in trange(1, max_r + 1)
        ],
        "Sim Avg (10e5)": [
            average.avg_turns_tr(tr, early_stop=True, trials=10**5)
            for tr in trange(1, max_r + 1)
        ],
    }

    df = save_df(data, "Table_3")
    print(df)
    return df

def table_4(max_r: int = 25, sim_mag=[2, 4, 6]) -> pd.DataFrame:
    print("Generating Table 4")
    data = {
        "r": [r for r in range(1, max_r + 1)],
        "Markov": [recursion.P(r, 0) for r in range(1, max_r + 1)],
        "Geometric": [1 - (1 - sampling.p[0]) ** r for r in range(1, max_r + 1)],
    }

    for mag in tqdm(sim_mag, desc="Table 4"):
        sim = [
            probability.p_losing_turn(r, trials=10**mag) for r in range(1, max_r + 1)
        ]
        data[f"Sim (10e{mag})"] = sim

    df = save_df(data, "Table_4")
    print(df)
    return df

def table_5(max_s: int = 50, sim_mag=[2, 4, 6]) -> pd.DataFrame:
    print("Generating Table 5")
    data = {
        "s": [s for s in range(1, max_s + 1)],
        "Expected Score": [recursion.Es(s) for s in range(1, max_s + 1)],
    }

    for mag in tqdm(sim_mag, desc="Table 5"):
        sim = [average.avg_roll_ts(ts, trials=10**mag) for ts in range(1, max_s + 1)]
        data[f"Sim Avg (10e{mag})"] = sim

    df = save_df(data, "Table_5")
    print(df)
    return df

def table_6(max_s: int = 50) -> pd.DataFrame:
    print("Generating Table 6")
    data = {
        "s": [s for s in range(1, max_s + 1)],
        "Estimated Turns": [100 / (recursion.Es(s)) for s in trange(1, max_s + 1)],
        "Sim Avg (10e3)": [
            average.avg_turns_ts(ts, trials=10**3) for ts in trange(1, max_s + 1)
        ],
        "Sim Avg (10e5)": [
            average.avg_turns_ts(ts, trials=10**5) for ts in trange(1, max_s + 1)
        ],
    }

    df = save_df(data, "Table_6")
    print(df)
    return df

def table_7():
    data = {
        "x": [x for x in range(1, 6 + 1)],
        "Unbiased Die": [1 / 6] * 6,
        "Lower-biased Die": [i / 21 for i in reversed(range(1, 6 + 1))],
        "Upper-biased Die": [i / 21 for i in range(1, 6 + 1)],
        "Center-biased Die": [i / 12 for i in (1, 2, 3, 3, 2, 1)],
    }

    df = save_df(data, "Table_7")
    print(df)
    return df

if __name__ == '__main__':
    save_path = sys.argv[1]

table_1()
table_2()
table_3()

table_4()

table_5()
table_6()
table_7()
