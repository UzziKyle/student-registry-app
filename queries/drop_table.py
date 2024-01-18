from getpass import getpass
from mysql.connector import connect, Error
from decouple import config

DATABASE: str = 'student_registry'
DB_USER: str = config('DB_USER')
DB_PASSWORD: str = config('DB_PASSWORD')

try:
    with connect(
        host="localhost",
        user=DB_USER,
        password=DB_PASSWORD,
        database=DATABASE,
    ) as connection:
        drop_table_query = "DROP TABLE students"
        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
            connection.commit()
            
except Error as e:
    print(e)
    