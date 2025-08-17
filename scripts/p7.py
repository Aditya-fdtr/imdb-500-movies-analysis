# 7. Display unique genres.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df['genres'].unique().tolist())