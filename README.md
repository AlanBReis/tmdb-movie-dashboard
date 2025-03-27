# TMDB Movie Dashboard

This project aims to create a **Movie Data Analysis Dashboard**, utilizing data collected from the **The Movie Database (TMDB)** API. Data collection will be done through an ETL pipeline using **Apache Airflow**, and the analysis will be performed in a **PostgreSQL** database.

## Features

### 1. **Data Collection**
- The **TMDB API** will be used to gather information about movies, including:
  - Movie title
  - Release date
  - Genre
  - Rating
  - Overview
- The data will be collected periodically and stored for further analysis.

### 2. **Data Transformation**
- The **Apache Airflow** pipeline will handle the following tasks:
  - Cleaning and transforming raw data into a structured format.
  - Aggregating ratings by genre and year.
  - Calculating average ratings and popularity metrics.
- This transformed data will be prepared for deeper analysis.

### 3. **Data Analysis**
- The **PostgreSQL** database will store and manage the transformed data.
- SQL queries will be used to:
  - Identify the highest-rated movies by genre or year.
  - Track trends in movie popularity over time.
  - Create rankings of movies based on different criteria (e.g., ratings, revenue, etc.).

### 4. **Data Visualization**
- Interactive visualizations will be created using **Plotly** or **Dash**, providing a user-friendly interface to explore the data.
  - Examples of visualizations include:
    - Bar charts for the highest-rated movies by genre.
    - Line charts showing movie popularity trends.
    - Pie charts displaying genre distribution across the movie database.
  - Real-time updates to the dashboard with the latest data.

---

## Technologies Used
- **TMDB API**: Data source for movie-related information.
- **Apache Airflow**: Orchestration tool for the ETL pipeline.
- **PostgreSQL**: Database to store transformed data.
- **Plotly/Dash**: Frameworks for creating interactive data visualizations.
