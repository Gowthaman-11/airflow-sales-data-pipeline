# Airflow Sales Data Pipeline

## Overview

An End-to-End ETL Data Pipeline built using Apache Airflow, Python, SQLite, PostgreSQL, and Docker.

## Features

* Data Ingestion
* Data Validation
* Data Quality Checks
* SQLite Loading
* PostgreSQL Loading
* Incremental Loading
* Audit Logging
* Alert Notifications
* File Sensor Monitoring
* Retry Strategy

## Tech Stack

* Apache Airflow
* Python
* Pandas
* SQLite
* PostgreSQL
* Docker
* Git & GitHub

## DAG Flow

transform_sales
→ validate_sales
→ data_quality
→ load_to_sqlite
→ load_dim_fact
→ generate_kpis
→ incremental_load
→ load_to_postgres
→ audit_logger
→ alert_task

## Project Structure

config/
dags/
data/
scripts/
docker-compose.yml

## How to Run

1. Start Docker Desktop
2. Run:
   docker compose up -d
3. Open Airflow:
   http://localhost:8080
4. Trigger sales_pipeline DAG
5. Monitor task execution in Graph View

## Author

Gowthaman K
AWS Data Engineer
