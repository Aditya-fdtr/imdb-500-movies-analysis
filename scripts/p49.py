# 49. Create a bar plot of the number of movies per director.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('messy_movies_500.csv')
movies_per_director = df['director'].value_counts()

movies_per_director = df['director'].value_counts().head(10)  # top 10 directors

plt.figure(figsize=(10,6))
movies_per_director.plot(kind='bar')

plt.title("Number of Movies per Director")
plt.xlabel("Director")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.show()



