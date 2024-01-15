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
        create_table_query = """
        CREATE TABLE students(
            stud_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            
except Error as e:
    print(e)
    