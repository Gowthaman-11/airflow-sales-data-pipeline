import json

with open("/opt/airflow/config/pipeline_config.json") as f:
    config = json.load(f)

print(config)
print("Source File:", config["source_file"])
print("Target Table:", config["postgres_table"])