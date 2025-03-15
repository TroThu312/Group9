from tkinter import *
import Modules.Forget.Name.Forget_Name_Create as fnc
import Modules.Forget.Change.Forget_Change_Create as fcc
import Modules.Forget.Name.Forget_Name_Process as fnp
from tkinter import messagebox

class Forget_Code_Process:

    @staticmethod
    def submit_button_handle(obj):
        otp_entry = obj.code_entry.get().strip()
        correct_otp = fnp.Forget_Name_Process.verification_code
        if otp_entry == correct_otp:
            Forget_Code_Process.next_page(obj)
        else:
            messagebox.showerror("Error", "Invalid OTP")

    @staticmethod
    def back_button_handle(obj):
        obj.window.destroy()
        app = fnc.Forget_Name_Create()
        app.window.mainloop()

    @staticmethod
    def next_page(self):
        self.window.destroy()
        app = fcc.Forget_Change_Create()
        app.window.mainloop()