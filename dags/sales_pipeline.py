from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2026, 6, 17),
    schedule=None,
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=1)
    }
) as dag:

    transform_sales = BashOperator(
        task_id="transform_sales",
        bash_command="python /opt/airflow/scripts/transform_sales.py"
    )

    validate_sales = BashOperator(
        task_id="validate_sales",
        bash_command="python /opt/airflow/scripts/validate_sales.py"
    )

    data_quality = BashOperator(
        task_id="data_quality",
        bash_command="python /opt/airflow/scripts/data_quality.py"
    )

    load_to_sqlite = BashOperator(
        task_id="load_to_sqlite",
        bash_command="python /opt/airflow/scripts/load_to_sqlite.py"
    )

    load_dim_fact = BashOperator(
        task_id="load_dim_fact",
        bash_command="python /opt/airflow/scripts/load_dim_fact.py"
    )

    generate_kpis = BashOperator(
        task_id="generate_kpis",
        bash_command="python /opt/airflow/scripts/generate_kpis.py"
    )

    load_to_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /opt/airflow/scripts/load_to_postgres.py"
    )

    incremental_load = BashOperator(
        task_id="incremental_load",
        bash_command="python /opt/airflow/scripts/incremental_load.py"
    )

    audit_logger = BashOperator(
        task_id="audit_logger",
        bash_command="python /opt/airflow/scripts/audit_logger.py"
    )

    alert_task = BashOperator(
        task_id="alert_task",
        bash_command="python /opt/airflow/scripts/send_alert.py"
    )

    (
        transform_sales
        >> validate_sales
        >> data_quality
        >> load_to_sqlite
        >> load_dim_fact
        >> generate_kpis
        >> load_to_postgres
        >> incremental_load
        >> audit_logger
        >> alert_task
    )