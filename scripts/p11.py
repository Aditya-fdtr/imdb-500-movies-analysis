# 11. Strip extra spaces from title and director columns.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['title'] = df['title'].str.strip()
df['director'] = df['director'].str.strip()
print(df['title'])