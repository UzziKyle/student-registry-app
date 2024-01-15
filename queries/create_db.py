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
        password=DB_PASSWORD
    ) as connection:
        create_db_query = f"CREATE DATABASE {DATABASE}"
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
            
except Error as e:
    print(e)
    