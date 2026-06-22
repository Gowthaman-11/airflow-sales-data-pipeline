import pandas as pd
import sqlite3

customers = pd.read_csv("/opt/airflow/data/customers.csv")
products = pd.read_csv("/opt/airflow/data/products.csv")
orders = pd.read_csv("/opt/airflow/data/orders.csv")

conn = sqlite3.connect("/opt/airflow/data/sales.db")

customers.to_sql("dim_customer", conn, if_exists="replace", index=False)
products.to_sql("dim_product", conn, if_exists="replace", index=False)
orders.to_sql("fact_orders", conn, if_exists="replace", index=False)

conn.close()

print("Star Schema Loaded Successfully")