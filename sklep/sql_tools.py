from local_settings import database_settings
from psycopg2 import connect
def execute_query(query):
    connection = connect(**database_settings)
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(query)
        try:
            result = cursor.fetchall()
        except:
            result = None
        connection.close()
        return result




