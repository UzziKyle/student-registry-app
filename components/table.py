from customtkinter import *
from tkinter import ttk


class Table(CTkFrame):
    def __init__(self, master: any):
        super().__init__(master)
        
        self.button_container = CTkFrame(master=self)
        self.button_container.grid(row=0, column=0, columnspan=2)
        
        self.edit_button = CTkButton(master=self.button_container, text='Edit', state='disabled')
        self.edit_button.grid(row=0, column=0)
        
        self.delete_button = CTkButton(master=self.button_container, text='Delete', state='disabled')
        self.delete_button.grid(row=0, column=1)
                
        self.tree = ttk.Treeview(self, selectmode='browse')
        self.tree['columns'] = ('Student ID', 'First Name', 'Last Name')
        
        self.tree.column('#0', width=0, stretch=False)
        self.tree.column('Student ID', anchor='w', stretch=False)
        self.tree.column('First Name', anchor='w', stretch=True)
        self.tree.column('Last Name', anchor='w', stretch=True)
        
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading('Student ID', text='Student ID', anchor='w')
        self.tree.heading('First Name', text='First Name', anchor='w')
        self.tree.heading('Last Name', text='Last Name', anchor='w')
        
        self.tree.grid(row=1, column=0, padx=(10, 0), pady=(15, 5), sticky='nsew')
        self.tree.bind('<Button>', self.activate_buttons)
        self.tree.bind('<FocusOut>', self.deactivate_buttons)
        
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, padx=(0,10), pady=(15, 5), sticky='ns')
        
    def refresh_table(self, values):
        for col in self.tree['columns']:
            self.tree.delete(*self.tree.get_children())        
        try:
            for value in values:
                self.tree.insert(parent='', index='end', iid=value, values=(value))
        except:
            pass
        
    def activate_buttons(self, event = None):
        self.edit_button.configure(state='active')
        self.delete_button.configure(state='active')
        
    def deactivate_buttons(self, event = None):
        self.edit_button.configure(state='disabled')
        self.delete_button.configure(state='disabled')
        