import snowflake.connector

def get_connection():
    conn = snowflake.connector.connect(
        user='Anish3004',
        password='anishrout3004BDS0112',
        account='LTSFLEG-MO32405',  
        warehouse='ML_WH',
        database='ML_PROJECT',
        schema='FEATURES'
    )
    return conn
