# 5. Show the number of missing values in each column.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.isnull().sum())