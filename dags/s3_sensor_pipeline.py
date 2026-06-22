from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="s3_sensor_pipeline",
    start_date=datetime(2026, 6, 17),
    schedule=None,
    catchup=False
) as dag:

    wait_for_file = FileSensor(
        task_id="wait_for_file",
        filepath="/opt/airflow/data/sales.csv",
        poke_interval=10,
        timeout=60
    )

    transform_sales = BashOperator(
        task_id="transform_sales",
        bash_command="python /opt/airflow/scripts/transform_sales.py"
    )

    wait_for_file >> transform_sales