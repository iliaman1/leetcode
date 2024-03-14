import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
print(df.shape)  # Return a tuple representing the dimensionality of the DataFrame.
print(df['Name'].shape)
print(df[['Name', 'Age']].head(3))
print(df.loc[[0, 3, 7], ['Survived', 'Pclass']])
print(df.loc[df['Age'] == 18, ['Name', 'Survived']])
df_without_duplicate_age = df.drop_duplicates(subset='Age', keep='last', inplace=False)  # inplace=False is default
df_without_non_name = df.dropna(subset='Name')
# print(df[df['Age'] < 10])
print(df[df['Age'].isin((5, 16))])
