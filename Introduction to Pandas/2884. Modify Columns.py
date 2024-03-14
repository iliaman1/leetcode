import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees
