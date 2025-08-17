# 32. Get movies released between 1990 and 2000.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[(df['release_year'] > 1900) & (df['release_year'] < 2000)])
