# 31. Get movies with vote_count greater than 1 million.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['vote_count']>1_000_000])