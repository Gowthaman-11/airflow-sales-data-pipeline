import logging

logging.basicConfig(
    filename="/opt/airflow/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)