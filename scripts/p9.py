# 9. Show the top 10 directors by the number of movies.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df['director'].value_counts().head(10))