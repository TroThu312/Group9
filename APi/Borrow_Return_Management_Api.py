from APi.Main_Api import Api as main_api
from datetime import datetime
from tkinter import messagebox

class BorrowReturnManagementApi(main_api):
    def __init__(self):
        super().__init__()  # Gọi hàm khởi tạo của Api để đảm bảo các collections được khởi tạo
        self.connector()
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
            
    def return_book_api(self, student_id, book_id):
        """
        API trả sách:
        - Tìm giao dịch mượn sách của sinh viên có chứa sách với book_id và trạng thái "Borrowed".
        - Nếu tìm thấy, cập nhật trạng thái của sách sang "Returned" và cập nhật ngày trả.
        - Cập nhật dữ liệu kho sách: tăng Stock lên 1 và giảm Borrowed_Count đi 1.
        
        Trả về:
            1  : Trả sách thành công.
            -1 : Không tìm thấy giao dịch mượn sách cho sinh viên với sách đang được mượn.
            -2 : Cập nhật giao dịch thất bại.
            -3 : Không tìm thấy sách trong kho.
            -4 : Cập nhật kho sách thất bại.
        """
        
        # Tìm giao dịch mượn sách với trạng thái "Borrowed"
        transaction = self.invoices_collection.find_one({
            "Student_Id": student_id,
            "Books": {
                "$elemMatch": {
                    "Book_Id": book_id,
                    "Status": "Borrowed"
                }
            }
        })
        
        if transaction is None:
            return -1  # Không tìm thấy giao dịch mượn sách.
        
        # Cập nhật trạng thái trong giao dịch sang "Returned" và cập nhật ngày trả
        update_transaction = self.invoices_collection.update_one(
            {
                "Student_Id": student_id,
                "Books.Book_Id": book_id,
                "Books.Status": "Borrowed"
            },
            {
                "$set": {
                    "Books.$.Status": "Returned",
                    "Books.$.Return_Date": datetime.now().strftime("%Y-%m-%d")
                }
            }
        )
        
        if update_transaction.modified_count == 0:
            return -2  # Cập nhật giao dịch thất bại.
        
        # Cập nhật dữ liệu kho sách
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return -3  # Không tìm thấy sách trong kho.
        
        new_stock = book.get("Stock", 0) + 1
        new_borrowed_count = book.get("Borrowed_Count", 0) - 1 if book.get("Borrowed_Count", 0) > 0 else 0
        
        update_book = self.warehouse_collection.update_one(
            {"Book_Id": book_id},
            {"$set": {"Stock": new_stock, "Borrowed_Count": new_borrowed_count}}
        )
        
        if update_book.modified_count == 0:
            return -4  # Cập nhật kho sách thất bại.
        
        return 1  # Trả sách thành công.


    def search_borrowed_books_by_student(self, student_id):
        """
        API tìm kiếm sách đang mượn theo student_id:
        - Tìm các giao dịch có Student_Id = student_id.
        - Lọc ra các cuốn sách có Status là "Borrowed".
        - Trả về danh sách các dictionary với thông tin: Student_Id, Name, Title, Borrow_Date.
        """
        transactions = self.invoices_collection.find({"Student_Id": student_id})
        results = []
        for transaction in transactions:
            for book in transaction.get("Books", []):
                if book.get("Status") == "Borrowed":
                    results.append({
                        "Student_Id": transaction.get("Student_Id"),
                        "Name": transaction.get("Name"),
                        "Title": book.get("Title"),
                        "Borrow_Date": book.get("Borrow_Date")
                    })
        return results