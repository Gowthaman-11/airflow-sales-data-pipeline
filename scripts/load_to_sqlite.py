import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("/opt/airflow/data/output.csv")

engine = create_engine("sqlite:////opt/airflow/data/sales.db")

df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data loaded to SQLite successfully")