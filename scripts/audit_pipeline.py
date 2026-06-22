import psycopg2

conn = psycopg2.connect(
    host="postgres",
    database="airflow",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

cur.execute("""
INSERT INTO audit_log
(dag_name, task_name, status, records_processed)
VALUES
('sales_pipeline',
 'audit_pipeline',
 'SUCCESS',
 6)
""")

conn.commit()

cur.close()
conn.close()

print("Audit Record Inserted")