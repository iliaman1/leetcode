import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals['weight'] > 100, ['name', 'weight']].sort_values(by='weight', ascending=False)[['name']]
