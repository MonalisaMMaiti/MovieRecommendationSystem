**Objective**
The goal of this project is to build a Movie Recommendation System that suggests movies to users based on their past ratings and preferences. 
The system leverages collaborative filtering and content-based filtering techniques using the MovieLens dataset.

**Project Breakdown:**

1. Data Collection & Processing
      The dataset (ml-latest-small.zip) is downloaded from MovieLens and extracted automatically.
      The project primarily uses two CSV files:
      ratings.csv: Contains user ratings for different movies.
      movies.csv: Contains movie titles and their associated genres.
      Preprocessing Steps:
      Checks for missing values and removes them if any.
      Normalizes user ratings using MinMaxScaler.
      Splits genres into a structured format for better analysis.

2. Recommendation Approaches
      This project implements two key recommendation techniques:

**Collaborative Filtering (User-User & Item-Item)**
Find similar users who have rated the same movies.
It uses similarity measures like Cosine Similarity to determine how closely related users or items are.
Recommends movies that similar users have liked.
**Content-Based Filtering**
It uses movie genres and metadata to find similar movies.
Works by recommending movies with similar features to those a user has previously rated highly.
**. Model Evaluation & Performance Metrics**
To assess the system’s effectiveness, the following evaluation metrics are used:

**Precision@K & Recall@K:** Measures how well the recommendation system ranks relevant movies.
**Root Mean Square Error (RMSE):** Evaluates the accuracy of predicted ratings.

**Technologies Used**
Python
Pandas (For data handling)
Scikit-Learn (For similarity calculations)
NumPy (For numerical computations)
MovieLens Dataset (For training and evaluation)

**Future Enhancements**
Implement Neural Collaborative Filtering (Deep Learning Approach)


