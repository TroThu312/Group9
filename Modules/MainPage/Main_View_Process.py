from tkinter import messagebox
#from tkinter import *
import Modules.Login.Login_Create as llc
import Modules.Book.Add.Add_Book_Create as abc
import Modules.Book.Remove.Remove_Book_Create as rbc
import Modules.Book.Update.Update_Book_Create as ubc
import Modules.BorrowReturn.Borrow.Borrow_Book_Create as bbc
import Modules.BorrowReturn.Return.Return_Book_Create as brbc
import Modules.BorrowReturn.Show.Show_Book_Create as sbc
import Modules.User.Add_Update_User_Create as auuc
# Các view khác
class Main_View_Process():

    @staticmethod
    def log_out_button_handle(obj):
        messagebox.showinfo("Logout", "Logged out successfully!")
        obj.window.destroy()
        # Chuyển sang màn hình Login
        app =llc.Login_Process_Create()
        app.window.mainloop()

    @staticmethod
    def show_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Show Book:
        - Hiển thị danh sách sách (chức năng xem sách)
        """
        #messagebox.showinfo("Show Books", "Displaying book list...")
        # Thêm logic mở giao diện xem sách nếu có.
        obj.window.destroy()
        app =sbc.Show_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def return_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Return Book:
        - Thực hiện xử lý trả sách
        """
        #messagebox.showinfo("Return Book", "Book returned successfully!")
        # Thêm logic xử lý trả sách nếu có.
        obj.window.destroy()
        app = brbc.Return_Book_Create(username)
        app.window.mainloop()
    @staticmethod
    def borrow_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Borrow Book:
        - Thực hiện xử lý mượn sách
        """
        #messagebox.showinfo("Borrow Book", "Book borrowed successfully!")
        # Thêm logic xử lý mượn sách nếu có.
        obj.window.destroy()
        app = bbc.Borrow_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def add_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Add Book:
        - Mở giao diện thêm sách (Add Book Process) hoặc thực hiện chức năng thêm sách.
        """
        #messagebox.showinfo("Add Book", "Add Book button clicked.")
        obj.window.destroy()
        app =abc.Add_Book_Create(username)
        app.window.mainloop()
    @staticmethod
    def update_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Update Book:
        - Mở giao diện cập nhật sách.
        """
        #messagebox.showinfo("Update Book", "Update Book button clicked.")
        # Ví dụ: mở giao diện Update Book Process
        obj.window.destroy()
        app =ubc.Update_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def remove_book_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Remove Book:
        - Mở giao diện xoá sách (Remove Book Process)
        """
        # messagebox.showinfo("Remove Book", "Remove Book button clicked.")
        # obj.window.destroy()
        # from Modules.Book.Remove_Book_Process import Remove_Book_Process
        # app = Remove_Book_Process()
        # app.window.mainloop()
        obj.window.destroy()
        app = rbc.Remove_Book_Create(username)
        app.window.mainloop()

    @staticmethod
    def add_update_user_button_handle(obj, username):
        """
        Xử lý khi nhấn nút Add_update User:
        - Mở giao diện cập nhật thông tin người dùng.
        """
        #messagebox.showinfo("Add_Update User", "Add_Update User button clicked.")
        # Thêm logic mở giao diện cập nhật user nếu có.
        obj.window.destroy()
        app = auuc.Add_Update_User_Create(username)
        app.window.mainloop()