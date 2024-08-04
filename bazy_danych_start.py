import psycopg2
from local_settings2 import database_settings as db_s


connection = psycopg2.connect(**db_s)
cursor = connection.cursor()
query = "select * from product;"
cursor.execute(query)
data = cursor.fetchall()
for row in data:
    print(row)
connection.close()