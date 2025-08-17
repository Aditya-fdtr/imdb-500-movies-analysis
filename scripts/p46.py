# 46. Create a new column decade from release_year.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['decade'] = (df['release_year']//10)*10

print(df['decade'])