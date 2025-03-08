from tkinter import messagebox, END
import APi.Book_Management_Api as book_api
import Modules.MainPage.Main_View_Create as mainview
class Update_Book_Process:
    @staticmethod
    def get_data(obj): # Lấy dữ liệu từ các ô nhập
        book_id = obj.entry_book_id.get().strip()
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
    def reset(obj):
        obj.entry_book_id.delete(0, END)
        obj.entry_quantity.delete(0, END)

    @staticmethod
    def back_button_handle(obj):
        obj.window.destroy()
        app = mainview.Main_View_Create()  # Gọi giao diện MainView
        app.window.mainloop()