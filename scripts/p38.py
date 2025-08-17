# 38. Find the total vote count per genre (split genres first).
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

# print(df.groupby('genres')['vote_count'].count())
print(df.assign(genres=df['genres'].str.split('|')).explode('genres').groupby('genres')['vote_count'].sum()
)
# 👉 Step by step Explanation:

# df['genres'].str.split('|')
# Splits "Action|Adventure|Fantasy" → ['Action', 'Adventure', 'Fantasy'].
# Each movie now has a list of genres.

# .assign(genres=...)
# Creates a new column genres with those lists (replaces original genres).

# .explode('genres')
# Converts list values into separate rows.