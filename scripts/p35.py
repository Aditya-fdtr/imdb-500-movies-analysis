# 35. Select the top 5 longest movies.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.nlargest(5, 'runtime'))
# print(df['imdb_rating'].nlargest(5))
