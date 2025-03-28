from tkinter import *
import Modules.MainPage.Main_View_Create as mv
from tkinter import messagebox
from APi.Book_Management_Api import *

class Remove_Book_Process:

    @staticmethod
    def submit_button_handle(self):
        Book_Id = self.book_id_entry.get()
        if not Book_Id:
            messagebox.showerror("Warning", "Please enter Book ID")
            return
        else:
            api = Book_Management_Api()
            c = api.remove_items(Book_Id)
            if c == "Not found":
                messagebox.showerror("Warning", "Book not found")
            elif c == "Done":
                messagebox.showinfo("SUCCESS!", "BOOK REMOVED!")
                self.book_id_entry.delete(0, END)
            else:
                messagebox.showinfo("Notification", "Action Cancelled")

    @staticmethod
    def back_button_handle(self, username):
        self.window.destroy()
        app = mv.Main_View_Create(username)
        app.window.mainloop()
