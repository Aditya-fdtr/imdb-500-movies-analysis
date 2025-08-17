# 16. Fill missing runtime with the mean runtime.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['runtime'] = df['runtime'].fillna(df['runtime'].mean())