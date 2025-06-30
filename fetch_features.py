print("🚀 Script started")

import pandas as pd
from snowflake_config import get_connection

try:
    conn = get_connection()
    query = "SELECT * FROM CUSTOMER_FEATURES;"
    df = pd.read_sql(query, conn)
    conn.close()

    print("Connected and data fetched.")
    print("Number of rows:", len(df))
    print(df.head())

except Exception as e:
    print(" An error occurred:", e)
