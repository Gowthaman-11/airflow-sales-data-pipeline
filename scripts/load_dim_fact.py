import sqlite3
import pandas as pd

conn = sqlite3.connect("/opt/airflow/data/sales.db")

df = pd.read_csv("/opt/airflow/data/output.csv")

customer_dim = df[["customer"]].drop_duplicates()
customer_dim["customer_id"] = range(1, len(customer_dim) + 1)

customer_dim.to_sql(
    "dim_customer",
    conn,
    if_exists="replace",
    index=False
)

fact_sales = df.merge(customer_dim, on="customer")

fact_sales = fact_sales[
    ["order_id", "customer_id", "amount"]
]

fact_sales.to_sql(
    "fact_sales",
    conn,
    if_exists="replace",
    index=False
)

print("Star Schema Created Successfully")

conn.close()