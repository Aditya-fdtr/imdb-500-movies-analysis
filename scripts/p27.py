# 27. Get all movies with an IMDb rating greater than 8.5.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['imdb_rating']>8.5])

