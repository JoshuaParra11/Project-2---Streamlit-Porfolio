# Project-2---Streamlit-Porfolio
Streamlit Portfolio to showcase coursework from CS39AE Data Visualization.

# CS39AE Data Visualization Portfolio

This project is an interactive web application built with Streamlit to showcase data visualization coursework for CS39AE. The app provides an exploratory data analysis (EDA) and dashboard for the Denver Traffic Accidents dataset, demonstrating skills in data cleaning, processing, and visualization.

The teacher allowed us to combine new data visualization coding techniques with an online platform to create a
professional portfolio and create opportunity for employment as we start and develop our careers.

## Developer

- **Name:** Joshua Parra
- **Contact:** jp144ft@gmail.com

## App Navigation Overview

The portfolio is organized into several pages, accessible via a custom sidebar:

- **Home:** A landing page introducing the portfolio.
- **About Me:** Contains my professional bio, skills, and visualization philosophy.
- **EDA Gallery:** A multi-page gallery showcasing different charts and analyses of the dataset.
- **Dashboard:** An interactive dashboard to explore trends and patterns from the data.
- **Future Work:** Outlines plans for future projects and enhancements.

## Dataset Information

- **Dataset Name:** Denver Traffic Accidents
- **Source:** [Denver's Open Data Catalog](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-traffic-accidents)
- **Records:** The dataset contains 15000+ entries for traffic incidents in Denver.
- **Data Preprocessing:**
    - Removed over 10+ columns that were unnecessary for this analysis (e.g., `incident_id`, `offense_id`, `geo_x`, `geo_y`).
    - Dropped columns with a very high percentage of missing values that were not central to the analysis (e.g., `TU1_pedestrian_action`).
    - The cleaned data is saved as `Denver_Traffic_Clean.csv` and used by the application.
- **Ethics Note:** This dataset contains anonymized information about public traffic incidents. The analysis focuses on high-level trends, such as location and time, and does not attempt to identify or analyze the behavior of specific individuals involved.

## Requirements

All necessary Python libraries are listed in the `requirements.txt` file. To install them, run:
```bash
pip install -r requirements.txt
```

## Screenshots

*[Optional: Add 1-3 screenshots of your app pages here to help viewers preview the interface.]*

## AI Assistance Acknowledgment

This project was developed with the assistance of an AI programming partner to help with debugging, code generation for css and javascript snippets, and best practices. Since the course only lasts a semester and the
focus is to learn visualization techniques, the use of AI was permitted to compensate for lack of time and website development knowledge.