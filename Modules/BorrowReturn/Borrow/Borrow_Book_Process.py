from tkinter import *
# import Modules.Book.Borrow.Main_View as mv
from tkinter import messagebox
from APi.Borrow_Return_Management_Api import *

class Borrow_Book_Process:
    @staticmethod
    def reset_button_handle(self):
        self.entry_bookid.delete(0, END)
        self.entry_studentid.delete(0, END)
        messagebox.showinfo("Reset", "Reset successfully!")

    @staticmethod
    def borrow_button_handle(self):
        Book_Id = self.entry_bookid.get()
        Student_Id = self.entry_studentid.get()
        api = BorrowReturnManagementApi()
        c = api.check_book_borrow(Book_Id, Student_Id)
        if c == "Book not found":
            messagebox.showerror("Warning", "Book not found")
            self.entry_bookid.delete(0, END)
            self.entry_studentid.delete(0, END)

        elif c == "Student not found":
            messagebox.showerror("Warning", "Student not found")
            self.entry_bookid.delete(0, END)
            self.entry_studentid.delete(0, END)

        elif c == "Book out of stock":
            messagebox.showerror("Warning", "Book out of stock")
            self.entry_bookid.delete(0, END)
            self.entry_studentid.delete(0, END)
        elif c == "Book borrowed successfully":
            messagebox.showinfo("Success", "Book borrowed successfully")
            self.entry_bookid.delete(0, END)
            self.entry_studentid.delete(0, END)

    @staticmethod
    def back_button_handle(self):
        self.window.destroy()
        app = mv.Main_View()
        app.window.mainloop()
