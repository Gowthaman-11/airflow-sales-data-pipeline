import pandas as pd
from logger import logging

logging.info("Data Quality Check Started")

df = pd.read_csv("/opt/airflow/data/output.csv")

# Null Check
if df.isnull().sum().sum() > 0:
    raise Exception("Null values found")

# Duplicate Check
if df.duplicated().sum() > 0:
    raise Exception("Duplicate records found")

# Schema Validation
expected_columns = [
    "order_id",
    "customer",
    "amount"
]

if list(df.columns) != expected_columns:
    raise Exception("Schema mismatch")

logging.info("Data Quality Check Passed")
print("Data Quality Check Passed")