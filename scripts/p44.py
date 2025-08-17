# 44. Sort movies by vote_count and then by imdb_rating.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.sort_values(['vote_count','imdb_rating'], ascending=[False,False]))