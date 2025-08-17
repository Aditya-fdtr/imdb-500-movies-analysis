# 1. Load the dataset and display the first 5 rows.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')
print(df.head())