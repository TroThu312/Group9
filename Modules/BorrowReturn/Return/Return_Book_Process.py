from APi.Borrow_Return_Management_Api import *
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter.ttk import Treeview, Style
from tkinter import Scrollbar
import Modules.MainPage.Main_View_Create as mainview
import Modules.BorrowReturn.Return.Return_Book_Create as rbc
class Return_Book_Process:
    
    @staticmethod
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
            return_book_instance.entry_bookid.delete(0, 'end')
            return_book_instance.entry_search.delete(0, 'end')
            return_book_instance.entry_studentid.delete(0, 'end')
            return_book_instance.load_data()
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

    @staticmethod
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
        return_book_instance.tree.delete(*return_book_instance.tree.get_children())

        # Chèn dữ liệu mới vào Treeview
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
