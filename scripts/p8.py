# 8. Count the number of unique movie titles.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df['title'].nunique())