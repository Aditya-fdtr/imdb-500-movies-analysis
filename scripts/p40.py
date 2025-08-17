# 40. Count the number of movies per genre.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.assign(genres=df['genres'].str.split('|'))
  .explode('genres')
  .groupby('genres')['title']
  .count()
)