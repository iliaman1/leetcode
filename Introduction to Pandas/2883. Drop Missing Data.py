import pandas as pd

def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name')