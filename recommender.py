import re

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Cleaned Dataset
DATA_PATH = "data/imdb_data_cleaned.csv"

df = pd.read_csv(DATA_PATH)

df["clean_storyline"] = df["clean_storyline"].fillna("")

# Text Cleaning Function
def clean_text(text):
    """
    Cleans the input storyline.
    """

    text = str(text).lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000
)

tfidf_matrix = tfidf_vectorizer.fit_transform(
    df["clean_storyline"]
)


# Storyline-Based Recommendation Function
def recommend_movies_by_storyline(
    user_storyline,
    number_of_recommendations=5
):
    """
    Recommends movies based on a user-entered storyline.
    """

    if not user_storyline or not user_storyline.strip():
        return pd.DataFrame(
            columns=[
                "Movie_Title",
                "Storyline",
                "Similarity_Score"
            ]
        )

    # Clean the user's storyline
    cleaned_storyline = clean_text(user_storyline)

    # Convert the user's storyline into a TF-IDF vector
    user_vector = tfidf_vectorizer.transform(
        [cleaned_storyline]
    )

    # Compare user storyline with all movie storylines
    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    ).flatten()

    # Get indices of movies with highest similarity
    recommended_indices = similarity_scores.argsort()[
        ::-1
    ][:number_of_recommendations]

    # Create recommendation result
    recommendations = df.iloc[
        recommended_indices
    ][
        ["Movie_Title", "Storyline"]
    ].copy()

    # Add similarity scores
    recommendations["Similarity_Score"] = [
        round(similarity_scores[index], 4)
        for index in recommended_indices
    ]

    return recommendations.reset_index(drop=True)

# Test the Recommendation System
sample_storyline = """
A young scientist discovers a mysterious technology
that could change the future, but powerful enemies
try to stop the discovery.
"""

recommendations = recommend_movies_by_storyline(
    sample_storyline,
    number_of_recommendations=5
)

print("\nTop 5 Recommended Movies:\n")

if recommendations.empty:
    print("Please enter a valid storyline.")
else:
    print(
        recommendations.to_string(index=False)
    )
