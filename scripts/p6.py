# 6. Show basic statistics for numerical columns.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.describe())