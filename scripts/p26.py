# 26. Select all movies released after 2010.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['release_year']>2010])

# to get the total number of movies released after 2010
total_movies = df[df['release_year'] > 2010].shape[0]
print("Total movies Released After 2010:", total_movies)
