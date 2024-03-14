import pandas as pd


def change_datatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})
