from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 5, 26),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    }

dag = DAG(
    'linkedin_scraper',
    default_args=default_args,
    description='linkedin scraper',
    schedule_interval=timedelta(days=1),
)


to_CSV = BashOperator(
    owner='airflow',
    task_id='toCSV',
    bash_command='python3 /Users/klaudialegutko/Projects/airflow-tutorial/airflow/scripts/toCSV/scrape.py',
    retries=3,
    dag=dag
)

to_CSV
