# 47. Split genres into separate rows (one genre per row).
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df = df.assign(genres=df['genres'].str.split('|')).explode('genres')
