from tkinter import *
import Modules.MainPage.Main_View_Create as mv
from tkinter import messagebox
from APi.User_Api import *
import re

class Add_Update_User_Process:

    @staticmethod
    def add_button_handle(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()
        if not student_id or not name or not contact or not address:
            messagebox.showerror("Warning", "Please fill all the entries")
            return
        elif not (re.search(r'[a-zA-Z]', student_id) and re.search(r'\d', student_id)):
            messagebox.showerror("Error", "Student ID must contain both letters and numbers")
            return
        elif not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name must contain only letters")
            return
        elif not contact.isdigit():
            messagebox.showerror("Error", "Contact must contain only numbers")
            return
        if address.isdigit():
            messagebox.showerror("Error", "Address cannot contain only numbers")
            return
        else:
            api = User_Api()
            c = api.add_new_user(student_id, name, contact, address)
            if c == "Available":
                messagebox.showinfo("SUCCESS!", "USER ADDED!")
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)
                self.load_data()
            elif c == "Not Available":
                messagebox.showerror("Warning", "User already exists")

    @staticmethod
    def update_button_handle(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()
        if not student_id or not name or not contact or not address:
            messagebox.showerror("Warning", "Please fill all the entries")
            return
        else:
            api = User_Api()
            c = api.update_user(student_id, name, contact, address)
            if c == "Not Found":
                messagebox.showerror("Warning", "User not found!")
            elif c == "Updated":
                messagebox.showinfo("SUCCESS!", "User updated!")
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)
                self.load_data()
    def search_button_handle(self):
        search_value = self.search_entry.get().strip()

        if not search_value:
            messagebox.showerror("Warning", "Please enter a keyword to search!")
            return

        api = User_Api()
        results = api.search_user(search_value)  

        if not results:
            messagebox.showinfo("Info", "No user found!")
            return
        self.load_search_data(results)

    @staticmethod
    def reset_button_handle(self):
        self.student_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.address_entry.delete(0, END)
        
    @staticmethod
    def back_button_handle(self, username):
        self.window.destroy()
        app = mv.Main_View_Create(username)
        app.window.mainloop()
    
