# 17. Fill missing imdb_rating with the median rating.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['imdb_rating'] = df['imdb_rating'].fillna(df['imdb_rating'].median())