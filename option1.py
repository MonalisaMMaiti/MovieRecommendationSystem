# Import necessary libraries
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from scipy.sparse.linalg import svds
from collections import defaultdict

# Load the MovieLens dataset
# Download the dataset from https://grouplens.org/datasets/movielens/
ratings = pd.read_csv('ml-latest-small/ratings.csv')  # User ratings
movies = pd.read_csv('ml-latest-small/movies.csv')   # Movie metadata

# Display dataset info
print("Ratings Dataset:")
print(ratings.head())
print("\nMovies Dataset:")
print(movies.head())

# Data Preprocessing
# Merge ratings and movies data
data = pd.merge(ratings, movies, on='movieId')

# Create user-item interaction matrix
user_item_matrix = data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Normalize the user-item matrix (subtract user mean)
user_mean_ratings = user_item_matrix.mean(axis=1)
user_item_matrix_normalized = user_item_matrix.sub(user_mean_ratings, axis=0)

# Collaborative Filtering: Matrix Factorization (SVD)
# Perform Singular Value Decomposition (SVD)
user_item_matrix_normalized = csr_matrix(user_item_matrix_normalized.values)
U, sigma, Vt = svds(user_item_matrix_normalized, k=50)  # k is the number of latent factors
sigma = np.diag(sigma)

# Reconstruct the predicted ratings matrix
predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_mean_ratings.values.reshape(-1, 1)
predicted_ratings_df = pd.DataFrame(predicted_ratings, columns=user_item_matrix.columns, index=user_item_matrix.index)

# Evaluation: Train-Test Split
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Function to calculate RMSE
def rmse(predicted, actual):
    return np.sqrt(mean_squared_error(predicted, actual))

# Evaluate the model on test data
test_user_item_matrix = test_data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
test_user_mean_ratings = test_user_item_matrix.mean(axis=1)
test_user_item_matrix_normalized = test_user_item_matrix.sub(test_user_mean_ratings, axis=0)

# Predict ratings for the test set
test_predicted_ratings = predicted_ratings_df.loc[test_user_item_matrix.index, test_user_item_matrix.columns]

# Calculate RMSE
rmse_value = rmse(test_predicted_ratings.values, test_user_item_matrix_normalized.values)
print(f"\nRMSE: {rmse_value}")

# Function to recommend top N movies for a user
def recommend_movies(user_id, n=10):
    user_ratings = predicted_ratings_df.loc[user_id]
    user_ratings_sorted = user_ratings.sort_values(ascending=False)
    user_ratings_sorted = user_ratings_sorted[user_ratings_sorted > 0]  # Filter out unrated movies
    top_movies = user_ratings_sorted.head(n)
    return movies[movies['movieId'].isin(top_movies.index)]

# Example: Recommend top 10 movies for user 1
user_id = 1
recommended_movies = recommend_movies(user_id)
print(f"\nTop 10 Recommended Movies for User {user_id}:")
print(recommended_movies[['title', 'genres']])

# Evaluation: Precision@K
def precision_at_k(user_id, k=10):
    recommended_movies = recommend_movies(user_id, k)
    actual_movies = data[data['userId'] == user_id].sort_values(by='rating', ascending=False)['movieId']
    relevant_movies = set(recommended_movies['movieId']).intersection(set(actual_movies))
    return len(relevant_movies) / k

# Calculate Precision@K for user 1
precision_k = precision_at_k(user_id)
print(f"\nPrecision@10 for User {user_id}: {precision_k}")