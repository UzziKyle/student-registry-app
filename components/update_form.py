from customtkinter import *


class UpdateForm(CTkToplevel):
    def setup(self):
        self.first_name_entry.insert('end', self.first_name)
        self.last_name_entry.insert('end', self.last_name)
        
    def __init__(self, values):
        super().__init__()
        
        if values == '':
            self.destroy()
        
        self.stud_id, self.first_name, self.last_name = values

        self.title(f'Update Student #{self.stud_id}')
        
        self.first_name_label = CTkLabel(master=self, text='First Name:')
        self.first_name_label.grid(row=0, column=0)
        
        self.first_name_entry = CTkEntry(master=self)
        self.first_name_entry.grid(row=0, column=1)
        
        self.last_name_label = CTkLabel(master=self, text='Last Name:')
        self.last_name_label.grid(row=1, column=0)
        
        self.last_name_entry = CTkEntry(master=self)
        self.last_name_entry.grid(row=1, column=1)
        
        self.button_container = CTkFrame(master=self)
        self.button_container.grid(row=2, column=0, columnspan=2)
        
        self.update_button = CTkButton(master=self.button_container, text='Update')
        self.update_button.grid(row=0, column=0)
        
        self.cancel_button = CTkButton(master=self.button_container, text='Cancel', command=lambda: self.destroy())
        self.cancel_button.grid(row=0, column=1)
        
        self.setup()
        
    def get_new_values(self):
        self.first_name: str = self.first_name_entry.get()
        self.last_name: str = self.last_name_entry.get()
        
        return self.stud_id, self.first_name, self.last_name
        
    