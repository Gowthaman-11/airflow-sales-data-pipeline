import pandas as pd

df = pd.read_csv("/opt/airflow/data/output.csv")

if df.isnull().sum().sum() == 0:
    print("Data Quality Check Passed")
else:
    raise Exception("Null values found")