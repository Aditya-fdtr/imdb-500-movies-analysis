# 19. Drop rows where title is missing.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df = df.dropna(subset=['title'])
