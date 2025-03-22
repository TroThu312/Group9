from tkinter import messagebox, END
import APi.Book_Management_Api as book_api
import Modules.MainPage.Main_View_Create as mainview
import APi.Book_Management_Api as bma
class Update_Book_Process:

    @staticmethod
    def get_data(obj): 
        book_id = obj.entry_bookid_quantity.get().strip()
        quantity_str = obj.entry_quantity.get().strip()
        if not book_id or not quantity_str:
            return None, None
        try:
            quantity = int(quantity_str)
        except ValueError:
            return None, None
        return book_id, quantity
    @staticmethod
    def add_book_button_handle(obj):
        book_id, quantity = Update_Book_Process.get_data(obj)
        if book_id is None or quantity is None:
            messagebox.showerror("Error", "Invalid Input")
            return
        api = book_api.Book_Management_Api()
        result = api.update_book_quantity(book_id, quantity, "add")
        if result == 0:
            messagebox.showinfo("Success", "Updated Successfully")
            Update_Book_Process.reset(obj)
        elif result == -1:
            messagebox.showerror("Error", "Book not found")
        elif result == -2:
            messagebox.showerror("Error", "Insufficient stock")
        else:
            messagebox.showerror("Error", "Update failed")

    @staticmethod
    def remove_book_button_handle(obj):
        book_id, quantity = Update_Book_Process.get_data(obj)
        if book_id is None or quantity is None:
            messagebox.showerror("Error", "Invalid Input")
            return

        api = book_api.Book_Management_Api()
        result = api.update_book_quantity(book_id, quantity, "remove")
        if result == 0:
            messagebox.showinfo("Success", "Remove Successfully")
            Update_Book_Process.reset(obj)
        elif result == -1:
            messagebox.showerror("Error", "Book not found")
        elif result == -2:
            messagebox.showerror("Error", "Insufficient stock")
        else:
            messagebox.showerror("Error", "Update failed")

    @staticmethod
    def update_book_info(obj):
        book_id = obj.entry_bookid_info.get().strip()
        title = obj.entry_title.get().strip()
        author = obj.entry_author.get().strip()
        genre = obj.entry_genre.get().strip()
        if not book_id or not title or not author or not genre:
            messagebox.showerror("Error","Invalid Input!")
            return
        update_data = {
            "Title": title,
            "Author": author,
            "Genre": genre
        }
        api = bma.Book_Management_Api()
        current_data = api.get_book_info(book_id)
        if not current_data:
            messagebox.showerror("Error", "Book not found!")
            return
        update_data = {}
        if title and title != current_data["Title"]:
            update_data["Title"] = title
        if author and author != current_data["Author"]:
            update_data["Author"] = author
        if genre and genre != current_data["Genre"]:
            update_data["Genre"] = genre
        result = api.update_book_info(book_id, update_data)
        
        if not update_data:
            messagebox.showinfo("Information", "No changes detected. The book information remains the same.")
            return 
        if result == 0:
            messagebox.showinfo("Sucess", "Book information updated successfully!")
            Update_Book_Process.reset(obj)
        elif result == -1:
            messagebox.showerror("Error", "Book not found!")
        else:
            messagebox.showerror("Error", "Update failed!")
    @staticmethod
    def reset(obj):
        obj.entry_bookid_info.delete(0, END)
        obj.entry_title.delete(0,END)
        obj.entry_author.delete(0,END)
        obj.entry_genre.delete(0,END)

    @staticmethod
    def back_button_handle(obj, username):
        obj.window.destroy()
        app = mainview.Main_View_Create(username)  
        app.window.mainloop()