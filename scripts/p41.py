# 41. Find the release year with the most movies.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df['release_year'].value_counts().idxmax())