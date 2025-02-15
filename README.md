**Introduction**

![image](https://github.com/user-attachments/assets/d3e6840d-3077-44da-bd12-e807ecbf6764)

In today's digital world, choosing a movie can be overwhelming with so many options available. I created this Movie Recommendation System to make it easier for users to discover movies they’ll love based on their preferences and past ratings. This system uses a mix of collaborative filtering and content-based filtering to provide personalized recommendations. It is built using Python, Pandas, and Scikit-Learn, with data from the MovieLens dataset.

**Why I Built This Project**
My goal with this project was to:
* Create a smart movie recommendation engine that helps users find relevant movies easily.
* Explore different recommendation techniques (content-based filtering, collaborative filtering, and hybrid models).
* Evaluate the system’s performance using Precision@K, Recall@K, and RMSE to ensure quality recommendations.

**Dataset I Used**
To make this recommendation system work, I used the MovieLens dataset, which provides real-world movie ratings from users. It contains:
•	ratings.csv – User ratings for different movies.
•	movies.csv – Movie titles, release years, and genres.
This dataset is freely available at MovieLens.

**How It Works**
This system generates recommendations using two key techniques:
**4.1 Content-Based Filtering**
•	This method recommends movies based on their features (genres, metadata, etc.).
* ![image](https://github.com/user-attachments/assets/e3c76805-7bde-4625-b656-591e0ba08f2f)
* 
**How I did it:**
* Extracted movie genres and structured them into a usable format.
* Used cosine similarity to find movies that are most alike.
* Recommended movies similar to those the user has already watched and liked.

  
**4.2 Collaborative Filtering**
•	Instead of relying on movie attributes, this technique analyzes user behavior to find patterns.
•	Two approaches I implemented:
o	User-User Similarity: Finds users with similar movie tastes and recommends movies they enjoyed.
o	Item-Item Similarity: Recommends movies that are similar to those the user has already rated.
•	The system uses cosine similarity to measure relationships between users and movies.

![image](https://github.com/user-attachments/assets/38a32588-2c9b-4eb6-b2a8-dd9e5ff73f5c)

**4.3 Hybrid Model** (Best of Both Worlds!)
Since both techniques have their strengths and weaknesses, I combined them into a hybrid approach to improve accuracy and variety in recommendations.

**Steps I Took to Build This**
**1 Data Preprocessing**
Before making recommendations, I had to clean and prepare the data:
* Checked for missing values and removed incomplete records.
* Normalized ratings using MinMaxScaler to ensure uniformity.
* Transformed genres into a machine-readable format.
**2 Training the Model & Evaluating Its Performance**
•	I trained the model using movie ratings and metadata.
•	To measure how well it performs, I used:
            o	Precision@K & Recall@K – Determines how relevant recommendations are.
            o	RMSE (Root Mean Square Error) – Measures accuracy of predicted ratings.

**What I Observed**
After running multiple tests, here’s what I found:
* Collaborative filtering works best when users have a long history of ratings.
* Content-based filtering is useful for users with fewer ratings.
* The hybrid model produces better recommendations overall.
* The system can be extended beyond movies – it could work for books, music, e-commerce, and more!




**How I Can Make It Even Better**
I have a few ideas to take this project further:
Deep Learning-Based Recommendations – Implementing Neural Collaborative Filtering (NCF) to improve accuracy.
Hybrid Model Optimization – Fine-tuning how content-based and collaborative filtering work together.
Deploying as a Web App – Making it accessible through a Flask or Django-based web interface.
Real-Time Recommendations – Using live data processing to update suggestions dynamically.

**Future Neural Collaborative Filtering**
This was a fun and rewarding project that allowed me to dive deep into recommendation systems. I successfully built a Movie Recommendation System that provides personalized movie suggestions using collaborative filtering and content-based filtering.
There’s always room for improvement, and I look forward to implementing deep learning and real-time recommendations to take it to the next level!

![image](https://github.com/user-attachments/assets/adc48674-3e1b-41d5-8864-2b2d9bf44ac1)

