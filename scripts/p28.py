# 28. Get all movies directed by Christopher Nolan.
import pandas as pd

df = pd.read_csv('messy_movies_500.csv')

nolan_movies = df[df['director'].str.contains('Christopher Nolan', case=False , na=False)]

print(nolan_movies)

# Explanation
# Ignores case sensitivity (case=False → matches "christopher nolan", "CHRISTOPHER NOLAN", etc.)
# Handles missing values (na=False → avoids errors if some rows have NaN in director)