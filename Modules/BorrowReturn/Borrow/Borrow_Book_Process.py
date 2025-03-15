from tkinter import *
import Modules.MainPage.Main_View_Create as mv
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
        if Book_Id =="" or Student_Id == "":
            messagebox.showerror("Warning", "Please fill all the entries")
            return
        else:
            api = BorrowReturnManagementApi()
            c = api.check_book_borrow(Book_Id, Student_Id)
            if c == "Book not found":
                messagebox.showerror("Warning", "Book not found")
                self.entry_bookid.delete(0, END)
                self.entry_studentid.delete(0, END)
            elif c == "Nothing found":
                messagebox.showerror("Warning", "Error. Couldn't find any information related to input")
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
    def back_button_handle(self, username):
        self.window.destroy()
        app = mv.Main_View_Create(username)
        app.window.mainloop()
