# 45. Rank movies based on IMDb rating.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['rating_rank'] = df['imdb_rating'].rank(ascending=False)
