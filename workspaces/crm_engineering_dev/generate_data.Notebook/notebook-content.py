# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fde62d46-a52e-463e-8385-d0e5f34e4907",
# META       "default_lakehouse_name": "lh_crm_engineering",
# META       "default_lakehouse_workspace_id": "b2a9aa4f-208f-43d4-8a63-8d52fa86866f",
# META       "known_lakehouses": [
# META         {
# META           "id": "fde62d46-a52e-463e-8385-d0e5f34e4907"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "3b3f0a1b-789c-9f3d-4c14-1025b7525afb",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# CELL ********************

# Databricks / Fabric Notebook
# 📚 Generate Synthetic CRM Data (Bronze Layer)
# This notebook creates synthetic datasets for customers, products, and sales, and stores them as Delta Lake tables in the Bronze layer.

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta
import uuid

# Initialize Faker with Brazilian locale
fake = Faker('pt-BR')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# 🧑‍💼 Generate Customers

def generate_customers(n=500):
    """Generate synthetic customer records."""
    data = []
    for _ in range(n):
        data.append	({
            "customer_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=70).isoformat(),
            "state": fake.estado_sigla(),
            "signup_date": fake.date_this_decade().isoformat()
        })
    return pd.DataFrame(data)

df_customers = generate_customers(500)
display(df_customers)

#Save as Delta table in Bronze
spark_df = spark.createDataFrame(df_customers)
spark_df.write.format("delta").mode("overwrite").save("Table/bronze_customer")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
