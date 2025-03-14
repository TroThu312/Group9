from APi.Main_Api import Api as main_api
from datetime import datetime
from tkinter import messagebox

class BorrowReturnManagementApi(main_api):
    def __init__(self):
        super().__init__()  # Gọi hàm khởi tạo của Api để đảm bảo các collections được khởi tạo

    def check_book_borrow(self, book_id, student_id):
        # Kiểm tra xem sách có tồn tại không
        book = self.warehouse_collection.find_one({"Book_Id": book_id})  # Đổi books_collection thành warehouse_collection
        user = self.users_collection.find_one({"Student_id": student_id})
        if not book or not user:
            return "Nothing found"
        elif not book:
            return "Book not found"
        elif not user:
            return "Student not found"
        else:
            if book["Stock"] <= 0:
                    return "Book out of stock"
            else:
                # Cập nhật Stock và Borrowed_Count
                self.warehouse_collection.update_one(
                    {"Book_Id": book_id},
                    {"$inc": {"Stock": -1, "Borrowed_Count": 1}}
                )
                # Tạo transaction mới
                transaction_id = f"T{self.invoices_collection.count_documents({}) + 1:03d}"
                borrow_date = datetime.now().strftime("%Y-%m-%d")
                new_transaction = {
                    "Transaction_Id": transaction_id,
                    "Student_Id": student_id,
                    "Name": user["Name"],
                    "Books": [{
                        "Book_Id": book_id,
                        "Title": book["Title"],
                        "Borrow_Date": borrow_date,
                        "Return_Date": None,
                        "Status": "Borrowed"
                    }]
                }
                self.invoices_collection.insert_one(new_transaction)
                return "Book borrowed successfully"
