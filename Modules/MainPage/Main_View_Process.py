from tkinter import messagebox
import Modules.Login.Login_Create as llc
import Modules.Book.Add.Add_Book_Create as abc
import Modules.Book.Remove.Remove_Book_Create as rbc
import Modules.Book.Update.Update_Book_Create as ubc
import Modules.BorrowReturn.Borrow.Borrow_Book_Create as bbc
import Modules.BorrowReturn.Return.Return_Book_Create as brbc
import Modules.BorrowReturn.Show.Show_Book_Create as sbc
import Modules.User.Add_Update_User_Create as auuc
class Main_View_Process():

    @staticmethod
    def log_out_button_handle(obj):
        messagebox.showinfo("Logout", "Logged out successfully!")
        obj.window.destroy()
        app =llc.Login_Process_Create()
        app.window.mainloop()

    @staticmethod
    def show_book_button_handle(obj, username):
        obj.window.destroy()
        app =sbc.Show_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def return_book_button_handle(obj, username):
        obj.window.destroy()
        app = brbc.Return_Book_Create(username)
        app.window.mainloop()
    @staticmethod
    def borrow_book_button_handle(obj, username):
        obj.window.destroy()
        app = bbc.Borrow_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def add_book_button_handle(obj, username):
        obj.window.destroy()
        app =abc.Add_Book_Create(username)
        app.window.mainloop()
    @staticmethod
    def update_book_button_handle(obj, username):
        obj.window.destroy()
        app =ubc.Update_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def remove_book_button_handle(obj, username):
        obj.window.destroy()
        app = rbc.Remove_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def add_update_user_button_handle(obj, username):
        obj.window.destroy()
        app = auuc.Add_Update_User_Create(username)
        app.window.mainloop()