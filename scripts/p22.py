# 22. Remove duplicate rows.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df = df.drop_duplicates()