import sqlite3
import pandas as pd
from sqlalchemy import create_engine

sqlite_conn = sqlite3.connect("/opt/airflow/data/sales.db")

dim_customer = pd.read_sql(
    "SELECT * FROM dim_customer",
    sqlite_conn
)

fact_sales = pd.read_sql(
    "SELECT * FROM fact_sales",
    sqlite_conn
)

engine = create_engine(
    "postgresql://airflow:airflow@airflow-postgres:5432/airflow"
)

dim_customer.to_sql(
    "dim_customer",
    engine,
    if_exists="replace",
    index=False
)

fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded To PostgreSQL Successfully")