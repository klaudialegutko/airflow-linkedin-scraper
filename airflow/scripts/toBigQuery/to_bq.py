from google.cloud import bigquery

client = bigquery.Client()
filename = '/Users/klaudialegutko/Projects/airflow-tutorial/linkedin_profiles.csv'
dataset_id = 'linkedin_profiles'
table_id = 'data_engineers'


dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True

with open(filename, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

job.result()  # Waits for table load to complete.

print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
