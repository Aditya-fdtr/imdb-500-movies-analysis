# 24. Remove leading/trailing spaces in all string columns.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df = df.apply(lambda x:x.str.strip() if x.dtype=='object' else x)