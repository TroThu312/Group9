from tkinter import *
import Modules.Forget.Code.Forget_Code_Create as fcc
import Modules.Forget.Name.Forget_Name_Process as fnp
from APi.Login_Api import *
from tkinter import messagebox

class Forget_Change_Process:
    
    @staticmethod
    def change_button_handle(obj):
        new_password = obj.new_entry.get().strip()
        confirm_password = obj.confirm_entry.get().strip()
        if new_password == confirm_password:
            api = Login_Api()
            username = fnp.Forget_Name_Process.admin_email_address
            password = obj.confirm_entry.get().strip()
            api.change_password(username, password)
            messagebox.showinfo("Success", "Password changed successfully")
            Forget_Change_Process.back_to_login(obj)
        else:
            messagebox.showerror("Error", "Password does not match")


    @staticmethod
    def back_to_login(self):
        from Modules.Login.Login_Create import Login_Process_Create
        self.window.destroy()
        app = Login_Process_Create()
        app.window.mainloop()

    @staticmethod
    def back_button_handle(obj):
        obj.window.destroy()
        app = fcc.Forget_Code_Create()
        app.window.mainloop()

    

