```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load user data and product data
user_data = pd.read_csv('user_data.csv')
product_data = pd.read_csv('product_data.csv')

# Function to generate user profile
def generate_user_profile(user_id):
    user_profile = user_data[user_data['userID'] == user_id]
    return user_profile

# Function to generate product features
def generate_product_features():
    product_features = product_data[['productID', 'productName', 'productDescription', 'productPrice', 'retailerID']]
    return product_features

# Function to create a content-based recommendation system
def content_based_recommendation(user_id):
    user_profile = generate_user_profile(user_id)
    product_features = generate_product_features()

    # Combine user profile and product features
    combined_features = pd.concat([user_profile, product_features], axis=1)

    # Convert text to matrix of token counts
    count = CountVectorizer()
    count_matrix = count.fit_transform(combined_features)

    # Compute cosine similarity matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Get the pairwsie similarity scores of all products with that user
    sim_scores = list(enumerate(cosine_sim[user_id]))

    # Sort the products based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar products
    sim_scores = sim_scores[1:11]

    # Get the product indices
    product_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar products
    return product_data.iloc[product_indices]
```