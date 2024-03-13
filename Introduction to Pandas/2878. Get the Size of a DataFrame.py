from typing import List

import pandas as pd


def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
