# 39. Find the highest-rated movie per director.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

# print(df.groupby('director')['imdb_rating'].idxmax())

print(df.loc[df.groupby('director')['imdb_rating'].idxmax()])