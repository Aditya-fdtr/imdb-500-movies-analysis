# 10. Check if there are duplicate rows.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.duplicated().sum())