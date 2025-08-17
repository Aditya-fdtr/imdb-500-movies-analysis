# 50. Find the correlation between runtime and IMDb rating.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[['runtime','imdb_rating']].corr())