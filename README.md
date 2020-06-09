## **LinkedIn scraper with Selenium's webdriver, BigQuery and Airflow**
This is a simple scraper to get familiar with Airflow. It scrapes LinkedIn profiles related to certain job role and city, saves to CSV, and stores it in BigQuery.
### In order to run it:
1. Install Airflow (or use Google's Composer), and set up Google Cloud Platform account (Google provides $300 worth of free credits), to access Composer and BigQuery.
2. To get familiar with Airflow its structure, follow this quickstart: https://airflow.apache.org/docs/stable/start.html.
3. For BigQuery, I found these tutorials helpful: https://cloud.google.com/bigquery/docs/tutorials.
4. To run your DAG, install and import all dependencies for python scripts, and simply trigger DAG in Airflow's UI.
