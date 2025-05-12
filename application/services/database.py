import snowflake.connector

def get_connection():
    """
    Establish and return a connection to the Snowflake database.
    """
    return snowflake.connector.connect(
        user='NIVEDITHA',
        password='90351@Revanthsai',
        account='frtcizk-rr68458',
        warehouse='COMPUTE_WH',
        database='MYDB',
        schema='MYSCHEMA'
    )
