from APi.Borrow_Return_Management_Api import *
import tkinter.messagebox as messagebox
from tkinter import ttk
import Modules.MainPage.Main_View_Create as mainview

class Return_Book_Process:
    
    @staticmethod
    def return_button_handle(return_book_instance):
        student_id = return_book_instance.entry_studentid.get().strip()
        book_id = return_book_instance.entry_bookid.get().strip()
        if not student_id or not book_id:
            messagebox.showerror("Error", "Please enter student ID and book ID.")
            return
        api = BorrowReturnManagementApi()
        result_code = api.return_book_api(student_id, book_id)
        
        if result_code == 1:
            messagebox.showinfo("Success", "Return book successfully.")
            return_book_instance.entry_bookid.delete(0, 'end')
            return_book_instance.entry_search.delete(0, 'end')
            return_book_instance.entry_studentid.delete(0, 'end')
            return_book_instance.load_data()
        elif result_code == -1:
            messagebox.showerror("Error", f"Transactions for Student ID {student_id} and Book ID {book_id} not found.")
        elif result_code == -2:
            messagebox.showerror("Error", f"Failed to update transactions for book ID {book_id}.")
        elif result_code == -3:
            messagebox.showerror("Error", f"Book ID {book_id} not found.")
        elif result_code == -4:
            messagebox.showerror("Error", f"Update for Book ID {book_id} failed.")
        else:
            messagebox.showerror("Error", "Unknown error.")

    @staticmethod
    def search_button_handle(return_book_instance):
        student_id = return_book_instance.entry_search.get().strip()
        if not student_id:
            messagebox.showerror("Error", "Please enter student ID.")
            return
        api = BorrowReturnManagementApi()
        results = api.search_borrowed_books_by_student(student_id)

        if not results:
            messagebox.showinfo("Notification", "This student has not borrowed any books.")
            return
        return_book_instance.tree.delete(*return_book_instance.tree.get_children())

        # Insert data to treeview
        for row in results:
            return_book_instance.tree.insert("", "end", values=(
                row.get("Book_Id"), row.get("Student_Id"), row.get("Name"), row.get("Title"), row.get("Borrow_Date")
        ))
    @staticmethod
    def reset_button_handle(return_book_instance):
        return_book_instance.entry_bookid.delete(0, 'end')
        return_book_instance.entry_search.delete(0, 'end')
        return_book_instance.entry_studentid.delete(0, 'end')
    
    @staticmethod
    def back_button_handle(obj, username):
        obj.window.destroy()
        app = mainview.Main_View_Create(username)
        app.window.mainloop()
