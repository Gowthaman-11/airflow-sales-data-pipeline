import pandas as pd
import sqlite3

conn = sqlite3.connect("/opt/airflow/data/sales.db")

orders = pd.read_sql("SELECT * FROM fact_orders", conn)

total_orders = len(orders)
total_quantity = orders["quantity"].sum()
total_revenue = orders["quantity"].sum() * 100

avg_order_value = total_revenue / total_orders

top_product = orders.groupby("product_id")["quantity"].sum().idxmax()

kpi = pd.DataFrame({
    "total_orders": [total_orders],
    "total_quantity": [total_quantity],
    "total_revenue": [total_revenue],
    "avg_order_value": [avg_order_value],
    "top_product": [top_product]
})

kpi.to_sql(
    "kpi_dashboard",
    conn,
    if_exists="replace",
    index=False
)

print("KPI Dashboard Created Successfully")

conn.close()