# 37. Find the average runtime per release year.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.groupby('release_year')['runtime'].mean())