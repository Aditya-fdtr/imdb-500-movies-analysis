# 42. Find the director with the highest average IMDb rating.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.groupby('director')['imdb_rating'].mean().idxmax())