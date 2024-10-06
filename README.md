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



