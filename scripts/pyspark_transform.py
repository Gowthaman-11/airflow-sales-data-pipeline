from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Sales ETL") \
    .getOrCreate()

df = spark.read.csv(
    "/opt/airflow/data/sales.csv",
    header=True,
    inferSchema=True
)

df.show()

filtered_df = df.filter(df.amount > 150)

filtered_df.show()

filtered_df.write.mode("overwrite").csv(
    "/opt/airflow/data/spark_output",
    header=True
)

print("PySpark Processing Completed")

spark.stop()