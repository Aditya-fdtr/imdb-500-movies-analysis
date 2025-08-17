# 48. Create a histogram of IMDb ratings.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('messy_movies_500.csv')

plt.figure(figsize=(8,6))
plt.hist(df['imdb_rating'], bins=20, edgecolor='black')  

plt.title("Distribution of IMDb Ratings")
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Movies")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
