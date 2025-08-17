# 43. Sort movies by IMDb rating (descending).
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.sort_values('imdb_rating', ascending=False))