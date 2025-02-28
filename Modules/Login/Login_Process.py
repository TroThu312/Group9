from tkinter import messagebox
from tkinter import *
import APi.Login_Api as LoginApi
class Login_Process:
    @staticmethod
    def login_button_handle(obj):
        username = obj.name_entry.get().strip()
        password = obj.password_entry.get().strip()

        api = LoginApi.Login_Api()
        result = api.check_user_login(username, password)

        if result == -1:
            messagebox.showerror("Error", "Username or password cannot be empty.")
            obj.name_entry.delete(0, END)
            obj.password_entry.delete(0, END)
        elif result == -2:
            messagebox.showerror("Error", "User not found.")
            obj.name_entry.delete(0, END)
            obj.password_entry.delete(0, END)
        elif result == -3:
            messagebox.showerror("Error", "Incorrect password.")
            obj.password_entry.delete(0, END)
        else:
            # Đăng nhập thành công
            messagebox.showinfo("Welcome", f"Welcome, Admin!")