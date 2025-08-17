# 36. Find the average IMDb rating per director.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.groupby('director')['imdb_rating'].mean())