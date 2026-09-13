import streamlit as st

from recommender import recommend_movies_by_storyline

# Page Configuration
st.set_page_config(
    page_title="IMDb Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# Application Title
st.title("IMDb Movie Recommendation System")

st.write(
    "Enter a movie storyline to discover movies with similar storylines."
)

# User Input
user_storyline = st.text_area(
    "Enter your storyline:",
    placeholder=(
        "Example: A young scientist discovers a mysterious technology "
        "that could change the future, but powerful enemies try to "
        "stop the discovery."
    ),
    height=180
)


# Number of Recommendations
number_of_recommendations = st.slider(
    "Number of recommendations:",
    min_value=1,
    max_value=5,
    value=3
)


# Recommendation Button
if st.button("Find Similar Movies"):

    if not user_storyline.strip():

        st.warning("Please enter a storyline first.")

    else:

        with st.spinner("Finding similar movies..."):

            recommendations = recommend_movies_by_storyline(
                user_storyline=user_storyline,
                number_of_recommendations=number_of_recommendations
            )

        if recommendations.empty:

            st.warning(
                "No recommendations found. Please try another storyline."
            )

        else:

            st.subheader("Recommended Movies")

            for index, movie in recommendations.iterrows():

                st.markdown(f"### {index + 1}. {movie['Movie_Title']}")

                st.write(movie["Storyline"])

                # st.caption(
                #     f"Similarity Score: {movie['Similarity_Score']}"
                # )

                st.divider()