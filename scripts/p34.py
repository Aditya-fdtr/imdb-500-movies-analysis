# 34. Select only the title and imdb_rating columns.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[['title', 'imdb_rating']])