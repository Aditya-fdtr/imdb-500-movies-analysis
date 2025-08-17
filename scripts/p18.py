# 18. Fill missing vote_count with 0.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['vote_count'] = df['vote_count'].fillna(0)