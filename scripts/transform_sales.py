from logger import logging
import pandas as pd
import json

logging.info("Transform Sales Started")

try:

    with open("/opt/airflow/config/config.json") as f:
        config = json.load(f)

    input_file = config["input_file"]
    output_file = config["output_file"]
    amount_threshold = config["amount_threshold"]

    df = pd.read_csv(input_file)

    print(df)

    filtered_df = df[df["amount"] > amount_threshold]

    filtered_df.to_csv(
        output_file,
        index=False
    )

    print("Output file created successfully")

    logging.info("Transform Sales Completed")

except Exception as e:
    logging.error(f"Transform Sales Failed: {e}")
    raise