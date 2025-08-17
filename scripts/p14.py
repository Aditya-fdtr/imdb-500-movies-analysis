# 14. Replace ',' in genres with '|'.
import pandas as pd 

df = pd.read_csv('messy_movies_500.csv')

df['genres'] = df['genres'].str.replace(',' , '|')

print(df['genres'])