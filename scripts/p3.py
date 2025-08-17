# 3. List all column names.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.columns.tolist())
