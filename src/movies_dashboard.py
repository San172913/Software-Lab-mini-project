# Movie Ratings Dashboard

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load Dataset
data = pd.read_csv("data/movies.csv")

# 2️⃣ Basic Info
print("Dataset Info:")
print(data.info())
print("\nTop 5 Movies:\n", data.head())

# 3️⃣ Data Cleaning
data.dropna(inplace=True)
data['year'] = data['year'].astype(int)

# 4️⃣ Top 10 Movies by Rating
top_movies = data.sort_values(by='rating', ascending=False).head(10)
print("\nTop 10 Movies by Rating:\n", top_movies[['title', 'rating']])

plt.figure(figsize=(10,6))
plt.barh(top_movies['title'], top_movies['rating'], color='skyblue')
plt.xlabel('Rating')
plt.ylabel('Movie')
plt.title('Top 10 Movies by IMDb Rating')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('outputs/top_movies.png')
plt.show()

# 5️⃣ Genre-wise Average Rating
genre_group = data.groupby('genre')['rating'].mean().sort_values(ascending=False)
print("\nAverage Rating per Genre:\n", genre_group)

plt.figure(figsize=(10,6))
genre_group.plot(kind='bar', color='orange')
plt.title('Average IMDb Rating by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.savefig('outputs/genre_popularity.png')
plt.show()

# 6️⃣ Trend of Ratings Over Years
yearly_rating = data.groupby('year')['rating'].mean()
plt.figure(figsize=(10,6))
plt.plot(yearly_rating.index, yearly_rating.values, marker='o', color='green')
plt.title('Average IMDb Rating Over Years')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/rating_trend.png')
plt.show()

# 7️⃣ Correlation between Votes and Rating
correlation = np.corrcoef(data['votes'], data['rating'])[0, 1]
print(f"\nCorrelation between votes and rating: {correlation:.3f}")
