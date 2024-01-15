from customtkinter import *


class AddForm(CTkFrame):
    FIRST_NAME_PLACEHOLDER: str = 'ex. Juan' 
    LAST_NAME_PLACEHOLDER: str = 'ex. Dela Cruz'
    
    def __init__(self, master: any) -> None:
        super().__init__(master)
        
        self.first_name_label = CTkLabel(master=self, text='First Name:')
        self.first_name_label.grid(row=0, column=0)
        
        self.first_name_entry = CTkEntry(master=self, placeholder_text=self.FIRST_NAME_PLACEHOLDER)
        self.first_name_entry.grid(row=0, column=1)
        
        self.last_name_label = CTkLabel(master=self, text='Last Name:')
        self.last_name_label.grid(row=1, column=0)
        
        self.last_name_entry = CTkEntry(master=self, placeholder_text=self.LAST_NAME_PLACEHOLDER)
        self.last_name_entry.grid(row=1, column=1)
        
        self.button_container = CTkFrame(master=self)
        self.button_container.grid(row=2, column=0, columnspan=2)
        
        self.add_button = CTkButton(master=self.button_container, text='Add')
        self.add_button.grid(row=0, column=0)
        
        self.clear_button = CTkButton(master=self.button_container, text='Clear', command=lambda: self.clear())
        self.clear_button.grid(row=0, column=1)
        
    def clear(self) -> None:
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        
        self.first_name_entry.configure(placeholder_text = self.FIRST_NAME_PLACEHOLDER)
        self.last_name_entry.configure(placeholder_text = self.LAST_NAME_PLACEHOLDER)
        
        self.master.focus_set()
        
    def get_inputs(self) -> tuple[str, str]:
        first_name: str = self.first_name_entry.get()
        last_name: str = self.last_name_entry.get()
        
        return first_name, last_name
    