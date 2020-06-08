## **Linked profiles scraper with Selenium's webdriver, BigQuery and Airflow**
This is a simple scraper to get familiar with Airflow.
In order to run it all the dependencies must be installed, as well as Google Cloud Platform account (Google provides $300 worth of free credits). Airflow can be setup either locally or using Google Cloud Composer. 
##It consists of two Bash Operators:
- Selenium's scraper that saves profiles to CSV.
- CSV gets uploaded to BigQuery.

I decided to keep my DAG and operator scripts in separate forlders, to keep it clean and organized.
