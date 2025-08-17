# 23. Standardize genres so each genre is separated by '|' and no extra spaces.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['genres'] = df['genres'].str.strip().str.replace(r'\s*\|\s*', '|', regex=True)
