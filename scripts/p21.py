# 21. Convert runtime, imdb_rating, and vote_count to numeric types.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df[['runtime','imdb_rating','vote_count']] = df[['runtime','imdb_rating','vote_count']].apply(pd.to_numeric)
