# 13. Convert director to proper case.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')
 
df['director'] = df['director'].str.title()