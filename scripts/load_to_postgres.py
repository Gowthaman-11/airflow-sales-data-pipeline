import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://airflow:airflow@postgres:5432/airflow"
)

df = pd.read_csv("/opt/airflow/data/output.csv")

customers = df[["customer"]].drop_duplicates()
customers.columns = ["customer_name"]

customers.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

print("Customer Dimension Loaded")