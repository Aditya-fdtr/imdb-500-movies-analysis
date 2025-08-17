# 20. Convert release_year to integer type.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['release_year'] = df['release_year'].astype(int)