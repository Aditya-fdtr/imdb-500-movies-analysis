# 33. Get movies where genre contains both 'Action' and 'Adventure'.

import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

print(df[df['genres'].str.contains("Action", case=False, na=False) &
   df['genres'].str.contains("Adventure", case=False, na=False)])

# or 
# df[df['genres'].str.contains("(?=.*Action)(?=.*Adventure)", case=False, na=False)]
   