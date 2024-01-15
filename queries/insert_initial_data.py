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
        insert_record_query = """
        INSERT INTO students (first_name, last_name) VALUES
        ('Juan', 'Dela Cruz'),
        ('Ferdinand', 'Magellan'),
        ('Chris', 'Paul'),
        ('Robin', 'Gibb'),
        ('Dean', 'Martin');
        """
        with connection.cursor() as cursor:
            cursor.execute(insert_record_query)
            connection.commit()
            
except Error as e:
    print(e)
    