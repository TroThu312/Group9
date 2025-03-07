from tkinter import *
# import Modules.Book.Borrow.Main_View as mv
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
                self.book_id_entry.delete(0, END)
            elif c == "Done":
                messagebox.showerror("SUCCESS!", "BOOK REMOVED!")
                self.book_id_entry.delete(0, END)

    @staticmethod
    def back_button_handle(self):
        self.window.destroy()
        app = mv.Main_View()
        app.window.mainloop()
