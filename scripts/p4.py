# 4. Display the data types of each column.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df.dtypes)