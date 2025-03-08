from tkinter import *
import Modules.MainView.MainView_create as mv
from tkinter import messagebox
from APi.User_Api import *



class Add_Update_User_Process:
    @staticmethod
    def reset_button_handle(self):
        self.student_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.address_entry.delete(0, END)
        messagebox.showinfo("Reset", "Reset successfully!")

    @staticmethod
    def add_button_handle(self):
        student_id = self.student_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()
        if not student_id or not name or not contact or not address:
            messagebox.showerror("Warning", "Please fill all the entries")
            return
        else:
            api = User_Api()
            c = api.add_new_user(student_id, name, contact, address)
            if c == "Available":
                messagebox.showerror("SUCCESS!", "USER ADDED!")
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)
            elif c == "Not Available":
                messagebox.showerror("Warning", "User already exists")
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)


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
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)
            elif c == "Updated":
                messagebox.showerror("SUCCESS!", "User updated!")
                self.student_id_entry.delete(0, END)
                self.name_entry.delete(0, END)
                self.contact_entry.delete(0, END)
                self.address_entry.delete(0, END)

    @staticmethod
    def back_button_handle(self):
        self.window.destroy()
        app = mv.Main_View()
        app.window.mainloop()
