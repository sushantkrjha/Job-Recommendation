# Job Recommendation System

This project is an API-based Job Recommendation System built with Django and Django REST Framework. It recommends job postings to users based on their profiles and experience. The system uses the TF-IDF algorithm and cosine similarity to match user skills, desired job roles, and locations with job postings stored in the database.

## Features

- User profile input via a REST API
- Cosine similarity-based job recommendation
- Filtered job postings based on experience level, job type, and similarity threshold
- Top 5 job recommendations
- Job data includes title, company, location, type, required skills, and experience level

## Technologies Used

- Python
- Django
- Django REST Framework
- Scikit-learn (for TF-IDF and cosine similarity)
- SQLite 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sushantkrjha/Job-Recommendation
    ```

2. Navigate to the project directory:

    ```bash
    cd job-recommendation-system
    ```

3. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the Django database:

    ```bash
    python manage.py migrate
    ```


6. Run the Django development server:

    ```bash
    python manage.py runserver
    ```


## PROJECT Overview
1. User Profile Creation: The user submits a profile containing their skills, desired roles, experience level, preferred job type, and locations.

2. Data Retrieval: The algorithm retrieves job postings that match the user's experience level and job type.

3. Data Preparation:
*For each job posting, it creates a combined string of required skills, location, and job title.
*For the user profile, it generates a combined string of skills, locations, and desired roles.

4. Text Vectorization: The combined user and job strings are vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) to convert text data into numerical form, allowing for mathematical comparison.

5. Cosine Similarity Calculation: The algorithm computes the cosine similarity between the user vector and the job posting vectors to measure how closely related they are. A score close to 0.1 indicates high similarity (considering job_title and location score 0.1 filters in good result)

6. Filtering and Sorting:
 * It filters the job postings based on a predefined threshold score (e.g., 0.1).
 * It then sorts the remaining job postings in descending order of similarity scores.
7. Recommendation Generation: The top N job postings (e.g., 5) are selected and returned as recommendations.


## Assumptions or Design 

1. Choice of Similarity Measure: The algorithm uses cosine similarity because it is effective for measuring the similarity between two non-zero vectors in a high-dimensional space. It’s particularly useful for text data, where the magnitude of the vector may not be relevant, only the direction.

2. TF-IDF Vectorization: TF-IDF was chosen as the vectorization method since it reduces the impact of common terms (like 'the', 'and') that may not provide meaningful differentiation between job postings and user profiles. It emphasizes unique skills and terms relevant to the job market.

3. Threshold for Similarity: A threshold of 0.1 was established based on experimentation with sample data to ensure that only sufficiently similar job postings are recommended. This helps in reducing irrelevant job suggestions.

4. Use of JSON Fields: Skills, desired roles, and locations are stored as JSON fields to allow for flexible data structures, making it easier to handle lists of varying lengths.



## Challenges we Encountered and How we Addressed Them

1. Performance Issues: Initially, the vectorization and similarity calculations could be computationally intensive, especially with a large dataset. To mitigate this, caching strategies could be implemented, and only relevant job postings are retrieved based on initial filters (experience level and job type). This is TODO for me right now.

2. Threshold Adjustment: Finding the right similarity threshold was initially challenging, leading to either too few recommendations or irrelevant ones. This was resolved through testing and iteration, analyzing the performance of various thresholds against real user feedback.

3. User Input Validation: Ensuring that the user input is valid and complete posed some challenges. Input validation was implemented in the serializer to catch errors early and provide meaningful feedback to users.



