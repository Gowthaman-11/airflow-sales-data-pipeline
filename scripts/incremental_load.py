import json
import pandas as pd

with open("/opt/airflow/config/watermark.json") as f:
    watermark = json.load(f)

last_id = watermark["last_processed_id"]

df = pd.read_csv("/opt/airflow/data/sales.csv")

new_data = df[df["order_id"] > last_id]

print("New Records")
print(new_data)

if len(new_data) > 0:
    new_max_id = int(new_data["order_id"].max())

    with open("/opt/airflow/config/watermark.json", "w") as f:
        json.dump(
            {"last_processed_id": new_max_id},
            f
        )

print("Incremental Load Completed")