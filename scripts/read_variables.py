from airflow.models import Variable

print("DB Host:", Variable.get("db_host"))
print("DB Name:", Variable.get("db_name"))
print("DB User:", Variable.get("db_user"))