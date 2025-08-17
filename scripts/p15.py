# 15. Remove extra spaces in genres.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['genres'] = df['genres'].str.replace(r'\s*\|\s*', '|', regex=True)
