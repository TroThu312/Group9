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

    # def show_books(self):
    #     """Tạo Treeview và hiển thị trên giao diện (chỉ gọi một lần khi khởi tạo)."""
    #     # Frame chứa Treeview
    #     self.frame_tree = Frame(self.window)
    #     self.frame_tree.place(x=75, y=350, width=1130, height=365)

    #     # Treeview (ban đầu không có dữ liệu)
    #     self.tree = Treeview(self.frame_tree, columns=("Book ID", "Name", "Author", "Genre", "Stock", "Borrowed"), show="headings")

    #     # Cấu hình các cột
    #     self.tree.column("Book ID", anchor=CENTER, width=150)
    #     self.tree.column("Name", anchor=W, width=300)
    #     self.tree.column("Author", anchor=W, width=200)
    #     self.tree.column("Genre", anchor=CENTER, width=150)
    #     self.tree.column("Stock", anchor=CENTER, width=100)
    #     self.tree.column("Borrowed", anchor=CENTER, width=120)

    #     # Tiêu đề cột
    #     self.tree.heading("Book ID", text="Book ID", anchor=CENTER)
    #     self.tree.heading("Name", text="Name", anchor=CENTER)
    #     self.tree.heading("Author", text="Author", anchor=CENTER)
    #     self.tree.heading("Genre", text="Genre", anchor=CENTER)
    #     self.tree.heading("Stock", text="Stock", anchor=CENTER)
    #     self.tree.heading("Borrowed", text="Borrowed", anchor=CENTER)

    #     # Thanh cuộn
    #     self.scroll_y = Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
    #     self.tree.configure(yscrollcommand=self.scroll_y.set)

    #     self.scroll_x = Scrollbar(self.frame_tree, orient="horizontal", command=self.tree.xview)
    #     self.tree.configure(xscrollcommand=self.scroll_x.set)

    #     # Đặt vị trí scrollbar
    #     self.scroll_y.pack(side="right", fill="y")
    #     self.scroll_x.pack(side="bottom", fill="x")
    #     self.tree.pack(side="left", fill="both", expand=True)

    #     # Style cho Treeview
    #     style = Style()
    #     style.theme_use("default")
    #     style.configure("Treeview", background="#B9E3E9", foreground="black", rowheight=50, font=("Arial", 20))
    #     style.configure("Treeview.Heading",  background="#B9E3E9", foreground="black", font=("Arial", 20, "bold"))
    #     self.window.resizable(False, False)
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
