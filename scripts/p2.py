# 2. Display the shape (rows, columns) of the dataset.
import pandas as pd
df = pd.read_csv('messy_movies_500.csv')

print(df.shape)