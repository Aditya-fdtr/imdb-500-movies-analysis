# 30. Get movies with runtime less than 100 minutes.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['runtime']<100])

# to find the total number of movies with runtime less than 100 minutes

print(df[df['runtime']<100].shape[0])
