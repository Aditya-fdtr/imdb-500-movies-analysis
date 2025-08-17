# 12. Convert title to title case.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

df['title'] = df['title'].str.title()