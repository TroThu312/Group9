from APi.Borrow_Return_Management_Api import *
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter.ttk import Treeview, Style
from tkinter import Scrollbar
import Modules.MainPage.Main_View_Create as mainview
class Return_Book_Process:
        
    def return_button_handle(return_book_instance):
        student_id = return_book_instance.entry_studentid.get().strip()
        book_id = return_book_instance.entry_bookid.get().strip()
    
        if not student_id or not book_id:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ mã sinh viên và mã sách.")
            return
        api = BorrowReturnManagementApi()
        result_code = api.return_book_api(student_id, book_id)
        
        if result_code == 1:
            messagebox.showinfo("Thành công", "Trả sách thành công.")
        elif result_code == -1:
            messagebox.showerror("Lỗi", f"Không tìm thấy giao dịch mượn sách cho sinh viên {student_id} với sách {book_id} đang được mượn.")
        elif result_code == -2:
            messagebox.showerror("Lỗi", f"Cập nhật giao dịch thất bại với sách {book_id}.")
        elif result_code == -3:
            messagebox.showerror("Lỗi", f"Không tìm thấy sách với mã {book_id} trong kho.")
        elif result_code == -4:
            messagebox.showerror("Lỗi", f"Cập nhật kho sách thất bại với sách {book_id}.")
        else:
            messagebox.showerror("Lỗi", "Có lỗi không xác định xảy ra.")

    def search_button_handle(return_book_instance):
        student_id = return_book_instance.entry_search.get().strip()
        if not student_id:
            messagebox.showerror("Lỗi", "Vui lòng nhập Student ID để tìm kiếm.")
            return
        api = BorrowReturnManagementApi()
        results = api.search_borrowed_books_by_student(student_id)

        if not results:
            messagebox.showinfo("Thông báo", "Không tìm thấy dữ liệu mượn sách cho sinh viên này.")
            return

        # Nếu đã có Treeview hiển thị kết quả, xoá đi trước khi tạo mới
        if hasattr(return_book_instance, 'tree') and isinstance(return_book_instance.tree, Treeview):
            return_book_instance.tree.destroy()

       # Tạo một frame để chứa Treeview và thanh cuộn
        frame = ttk.Frame(return_book_instance.window)
        frame.place(x=576, y=361, width=681, height=411)  # Vị trí của bảng và thanh cuộn

        # Tạo Scrollbar dọc
        y_scrollbar = Scrollbar(frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")

        # Tạo Treeview để hiển thị kết quả
        tree = ttk.Treeview(frame, columns=("Book_Id","Student_Id", "Name", "Title", "Borrow_Date"), show="headings", yscrollcommand=y_scrollbar.set)

        tree.heading("Book_Id", text = "Book ID")
        tree.heading("Student_Id", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Title", text="Title")
        tree.heading("Borrow_Date", text="Borrow Date")

        # Cài đặt cột với chiều rộng và căn giữa
        tree.column("Book_Id", width=90, anchor="center")  # Cột Student ID
        tree.column("Student_Id", width=80, anchor="center")  # Cột Student ID
        tree.column("Name", width=70, anchor="center")        # Cột Name
        tree.column("Title", width=240, anchor="center")       # Cột Title
        tree.column("Borrow_Date", width=90, anchor="center") # Cột Borrow Date
        #-80
        # Style cho Treeview
        style = Style()
        style.theme_use("default")
        style.configure("Treeview", background="#B9E3E9", foreground="black", rowheight=25, font=("Arial", 10))
        style.configure("Treeview.Heading",  background="#B9E3E9", foreground="black", font=("Arial", 10, "bold"))
        # Chèn dữ liệu vào Treeview
        for row in results:
            tree.insert("", "end", values=(row.get("Book_Id"), row.get("Student_Id"), row.get("Name"), row.get("Title"), row.get("Borrow_Date")))

        # Đặt lại các thanh cuộn với Treeview
        y_scrollbar.config(command=tree.yview)

        # Kích thước của Treeview
        tree.pack(fill="both", expand=True)

        return_book_instance.tree = tree

        return_book_instance.tree = tree  # Lưu lại đối tượng treeview để xử lý sau này (nếu cần)
    def reset_button_handle(return_book_instance):
        return_book_instance.entry_bookid.delete(0, 'end')
        return_book_instance.entry_search.delete(0, 'end')
        return_book_instance.entry_studentid.delete(0, 'end')
    
    @staticmethod
    def back_button_handle(obj, username):
        obj.window.destroy()
        app = mainview.Main_View_Create(username)
        app.window.mainloop()
