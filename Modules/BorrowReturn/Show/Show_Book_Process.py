from datetime import datetime
from tkinter import *
from tkinter.ttk import Treeview, Style
import APi.Borrow_Return_Management_Api as Bma
import Modules.MainPage.Main_View_Create as mainview

class Show_Book_Process:
    def __init__(self, window, entry_search):
        self.window = window
        self.entry_search = entry_search  # Lưu đối tượng entry tìm kiếm
        self.tree = None  # Khởi tạo biến tree (sẽ được tạo trong show_books)
        
    def show_button_handle(self):
        """Lấy dữ liệu từ MongoDB và hiển thị lên Treeview."""
        search = self.entry_search.get().strip()
        api = Bma.BorrowReturnManagementApi()
        books = api.show_book_api(search)

        # Kiểm tra nếu Treeview chưa được khởi tạo
        if not self.tree:
            print("Lỗi: Treeview chưa được tạo.")
            return

        # Xóa dữ liệu cũ trên Treeview trước khi hiển thị kết quả mới
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Nếu có kết quả, thêm dữ liệu vào Treeview
        if books:
            for book in books:
                self.tree.insert("", "end", values=(
                    book["Book_Id"], book["Title"], book["Author"], book["Genre"],
                    book["Stock"]
                ))
    @staticmethod
    def back_button_handle(obj, username):
        obj.window.destroy()
        app = mainview.Main_View_Create(username)
        app.window.mainloop()
