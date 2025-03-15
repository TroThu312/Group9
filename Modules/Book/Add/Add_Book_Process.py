from tkinter import *
from tkinter import messagebox
import APi.Book_Management_Api as book_api
import Modules.MainPage.Main_View_Create as mainview

class Add_Book_Process:

    @staticmethod
    def get_json_data(obj):
        book_id = obj.entry_book_id.get().strip()
        title = obj.entry_title.get().strip()
        author = obj.entry_author.get().strip()
        genre = obj.entry_genre.get().strip()
        stock = obj.entry_stock.get().strip()

        # Kiểm tra nếu có trường nào bị bỏ trống hoặc số lượng không hợp lệ
        if not all([book_id, title, author, genre, stock]):
            messagebox.showerror("Invalid Input", "Please fill in all fields.")
            return None
         # Kiểm tra kiểu dữ liệu và tính hợp lệ
        if not book_id.isalnum():
            messagebox.showerror("Invalid Data", "Book ID must contain letters.")
            return None
        
        if title.isdigit():
            messagebox.showerror("Invalid Data", "Title must not be a number.")
            return None
        
        if author.isdigit():
            messagebox.showerror("Invalid Data", "Author must not be a number.")
            return None
        
        if genre.isdigit():
            messagebox.showerror("Invalid Data", "Genre must not be a number.")
            return None
        
        try:
            stock = int(stock)
            if stock <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Data", "Stock must be a positive integer.")
            return None

        return {
            "Book_Id": book_id,
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Stock": stock
        }

    @staticmethod
    def add_button_handle(obj):
        book_data = Add_Book_Process.get_json_data(obj)
        if book_data is None:
            return

        api = book_api.Book_Management_Api()
        result = api.add_new_book(book_data)

        if result == 0:
            messagebox.showinfo("Success", "Updated Successfully")
            Add_Book_Process.reset_button_handle(obj)
        elif result == -1:
            messagebox.showerror("Error", "Incomplete data.")
        elif result == -2:
            messagebox.showerror("Error", "Stock limit exceeded.")
        elif result == -3:
            messagebox.showerror("Error", "This book existed in library.")
        else:
            messagebox.showerror("Error", "An error occurred while adding the book.")

    @staticmethod
    def reset_button_handle(obj):
        obj.entry_book_id.delete(0, END)
        obj.entry_title.delete(0, END)
        obj.entry_author.delete(0, END)
        obj.entry_genre.delete(0, END)
        obj.entry_stock.delete(0, END)

    @staticmethod
    def back_button_handle(obj):
        obj.window.destroy()
        app = mainview.Main_View_Create()
        app.window.mainloop()
