# IMDb Storyline Movie Recommender

This project is a content-based movie recommendation system built using **IMDb movie data from 2024**. Users can enter a movie storyline, and the system recommends the top five movies with similar plot descriptions. The recommendation process uses Natural Language Processing, TF-IDF vectorization, and Cosine Similarity.

## Project Overview

The objective of this project is to recommend movies based on storyline similarity rather than ratings, actors, or popularity.

The movie data focuses on **IMDb movies released in 2024**. The data collection process was explored using web scraping with Selenium, while the recommendation system uses movie titles and storyline descriptions for text-based similarity analysis.

Users can enter a short movie storyline into the Streamlit application, and the system returns the top five movies with the most similar storylines from the IMDb 2024 movie dataset.

## Features

* Uses IMDb 2024 movie storyline data
* Supports IMDb data collection through Selenium web scraping
* Performs data cleaning and text preprocessing
* Converts storylines into numerical vectors using TF-IDF
* Calculates similarity using Cosine Similarity
* Accepts user-entered storylines
* Recommends the top five similar movies
* Displays movie names, storylines, and similarity scores
* Provides an interactive Streamlit interface

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* Selenium
* Web Scraping

## Project Structure

```text
imdb-storyline-movie-recommender/
│
├── data/
│   ├── imdb_data.csv
│   └── imdb_data_cleaned.csv
│
├── src/
    ├── app.py
│   ├── scrapper.py
│   └── recommender.py
│
└── README.md
```

## Dataset

The project uses movie information from **IMDb movies released in 2024**.

The dataset contains the following columns:

* `Movie_Title`: Name of the movie
* `Storyline`: Original movie storyline
* `storyline_word_count`: Number of words in the storyline
* `clean_storyline`: Cleaned storyline text used for NLP processing

The dataset contains **6,021 movie records**.

### Data Collection

IMDb movie data for 2024 was explored through web scraping using Selenium. The scraping workflow focused on collecting:

* Movie titles
* Movie storyline descriptions

The collected data was stored in CSV format for further cleaning, analysis, and recommendation modeling.

## Exploratory Data Analysis

The following checks were performed during EDA:

* Dataset shape and column information
* Data types
* Missing-value analysis
* Duplicate movie analysis
* Storyline word-count statistics
* Shortest and longest storyline inspection

### EDA Results

* Total movies: 6,021
* Missing values: None
* Duplicate movie titles: None
* Average storyline length: Approximately 33 words
* Minimum storyline length: 4 words
* Maximum storyline length: 463 words

## Methodology

### 1. Data Collection

IMDb movie information for 2024 was collected or prepared using movie titles and storyline descriptions. Selenium was explored as the web scraping tool for collecting the required information.

### 2. Data Loading

The IMDb 2024 dataset is loaded using Pandas.

### 3. Data Cleaning

The storyline text is cleaned using the following steps:

* Convert text to lowercase
* Remove punctuation and unnecessary characters
* Remove numbers and special characters
* Remove extra spaces
* Handle empty text values

The cleaned storyline is stored in a separate `clean_storyline` column.

### 4. TF-IDF Vectorization

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts each movie storyline into a numerical vector based on the importance of words within the dataset.

The vectorizer uses:

* English stop-word removal
* A maximum of 10,000 text features

The resulting TF-IDF matrix contains one row per movie and one column per selected text feature.

### 5. Cosine Similarity

Cosine Similarity is used to compare the user's storyline with every movie storyline in the dataset.

A higher similarity score indicates greater textual similarity between the storylines.

### 6. Recommendation

The system:

1. Accepts a storyline from the user
2. Cleans the input text
3. Converts the input into a TF-IDF vector
4. Compares it with all movie storyline vectors
5. Sorts movies by similarity score
6. Returns the top five recommended movies

## Application Workflow

```text
Collect or load IMDb 2024 movie data
        ↓
Clean and preprocess storyline text
        ↓
Create TF-IDF vectors
        ↓
User enters a storyline
        ↓
Clean the input storyline
        ↓
Convert input into a TF-IDF vector
        ↓
Compare input with movie storyline vectors
        ↓
Calculate Cosine Similarity
        ↓
Rank movies by similarity score
        ↓
Display top five recommended movies
```

## Running the Application

Run the Streamlit application from the project root directory:

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Input

```text
A young scientist discovers a mysterious technology that could change
the future, but powerful enemies try to stop the discovery.
```

The application will return the top five movies whose storylines are most similar to the entered text.

## Output

Each recommendation contains:

* Movie title
* Movie storyline
* Cosine similarity score

The similarity score represents textual similarity between the user-entered storyline and the movie storyline. It is not a movie rating or prediction score.

## Limitations

* Recommendations are based only on storyline text.
* The system does not consider ratings, genres, actors, directors, or user preferences.
* Very short inputs may produce less meaningful recommendations.
* TF-IDF may not understand deeper semantic meaning or synonyms.
* The recommendation quality depends on the quality and coverage of the IMDb 2024 dataset.
* Web scraping results may depend on IMDb page structure and availability.

## Author

**Rishi Swaminathan**
