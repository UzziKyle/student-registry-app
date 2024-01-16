from mysql.connector import connect, Error
from customtkinter import *
from components.add_form import AddForm
from components.table import Table
from components.update_form import UpdateForm
from decouple import config


class App(CTk):
    DATABASE: str = 'student_registry'
    DB_USER: str = config('DB_USER')
    DB_PASSWORD: str = config('DB_PASSWORD')
    
    def setup(self) -> None:
        self.form.add_button.configure(command=lambda : self.add())
        self.table.edit_button.configure(command=lambda: self.open_update_form())
        self.table.delete_button.configure(command=lambda: self.delete())
        self.refresh_table(values=self.read())
    
    def __init__(self) -> None:
        super().__init__()
        
        self.title('Student Registry')
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)    
            
        self.form = AddForm(master=self)
        self.form.grid(row=0, column=0, sticky='nsew')
        
        self.table = Table(master=self)
        self.table.grid(row=0, column=1)
        
        self.setup()
            
    def connect_to_database(self):
        connection = connect(
            host='localhost',
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            db=self.DATABASE
            )
        
        return connection
    
    def execute_query(self, query: str):
        print(query)
        try:
            with self.connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    connection.commit()
        except Error as e:
            print(e)
    
    def refresh_table(self, values):
        self.table.refresh_table(values=values)
    
    def validate_values(self, values):
        if hasattr(values, '__iter__'):
            for value in values:
                if (value == '') or (value == ' '):
                    return False
        
        else:
            if (values == '') or (values == ' '):
                return False
            
        return True
    
    def read(self):
        try:
            with self.connect_to_database() as connection:
                with connection.cursor() as cursor:
                    cursor.execute('SELECT * FROM students')
                    results = cursor.fetchall()
                    connection.commit()
                    
            return results
        except Error as e:
            print(e)
            
    def add(self):
        inputs = self.form.get_inputs()
        inputs_are_valid = self.validate_values(values=inputs)
        
        if not inputs_are_valid:
            return
        
        first_name, last_name = inputs
        
        insert_student_query = """
        INSERT INTO students (first_name, last_name) 
        VALUES ('%s', '%s')
        """ % (first_name, last_name)
        
        self.execute_query(query=insert_student_query)
        self.refresh_table(values=self.read())
        
    def delete(self):
        item_row = self.table.tree.focus()
        item = self.table.tree.item(item_row) # {'text': '', 'image': '', 'values': [stud_id, first_name, last_name], 'open': 0, 'tags': ''}
        values = item['values']  
        values_are_valid = self.validate_values(values=values)
        
        if not values_are_valid:
            return
        
        stud_id, first_name, last_name = values
        
        delete_student_query = """
        DELETE FROM students WHERE stud_id = %s
        """ % (stud_id)
        
        self.execute_query(query=delete_student_query)
        self.refresh_table(values=self.read())
        self.table.deactivate_buttons()
            
    def open_update_form(self):
        item_row = self.table.tree.focus()
        item = self.table.tree.item(item_row) # {'text': '', 'image': '', 'values': [stud_id, first_name, last_name], 'open': 0, 'tags': ''}
        values = item['values'] 
        
        update_form = UpdateForm(values=values)
        
        update_form.update_button.configure(
            command=lambda: self.update(values=update_form.get_new_values(), toplevel_window=update_form)
            )
        
    def update(self, values, toplevel_window):
        values_are_valid = self.validate_values(values=values)
        
        if not values_are_valid:
            return
        
        stud_id, first_name, last_name = values
        
        update_student_query = """
        UPDATE 
            students
        SET
            first_name = '%s',
            last_name = '%s'
        WHERE
            stud_id = %s
        """ % (first_name, last_name, stud_id)
        
        self.execute_query(query=update_student_query)
        self.refresh_table(values=self.read())
        toplevel_window.destroy()
        

if __name__ == '__main__':
    app = App()
    app.mainloop()
    