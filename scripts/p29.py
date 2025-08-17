# 29. Get all Drama movies.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['genres'].str.contains('Drama', case=False, na=False)])
