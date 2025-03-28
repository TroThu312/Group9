from tkinter import messagebox
from tkinter import *
import APi.Login_Api as LoginApi
import Modules.MainPage.Main_View_Create as mvc
import Modules.Forget.Name.Forget_Name_Create as fnc

class Login_Process:
    @staticmethod
    def login_button_handle(obj):
        username = obj.name_entry.get().strip()
        password = obj.password_entry.get().strip()

        api = LoginApi.Login_Api()
        result = api.check_user_login(username, password)

        if result == -1:
            messagebox.showerror("Error", "Username/Email or password cannot be empty.")
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
            username = result
            messagebox.showinfo("Welcome", f"Welcome, {username}")
            obj.window.destroy()
            app = mvc.Main_View_Create(username)
            app.window.mainloop()
    @staticmethod
    def forget_button_handle(obj):
        obj.window.destroy()
        app =  fnc.Forget_Name_Create()
        app.window.mainloop()
