# 25. Rename all columns to lowercase with underscores.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')
