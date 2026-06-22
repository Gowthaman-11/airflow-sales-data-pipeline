import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("/opt/airflow/data/sales.db")

customer_df = pd.read_sql(
    "SELECT * FROM dim_customer",
    conn
)

customer_df["effective_date"] = datetime.now().date()
customer_df["expiry_date"] = None
customer_df["is_current"] = "Y"

customer_df.to_sql(
    "dim_customer_history",
    conn,
    if_exists="replace",
    index=False
)

print("SCD Type 2 History Table Created Successfully")

conn.close()