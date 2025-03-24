from APi.Main_Api import Api as main_api
from datetime import datetime

class BorrowReturnManagementApi(main_api):
    def __init__(self):
        super().__init__()  
        self.connector()

    def load_data_api(self):
        all_transactions = self.invoices_collection.find()  
        borrowed_transactions = []

        for transaction in all_transactions:
            borrowed_books = [
                book for book in transaction.get("Books", []) if book.get("Status") == "Borrowed"
            ]
            for book in borrowed_books:
                borrowed_transactions.append({
                    "Book_Id": book.get("Book_Id"),
                    "Student_Id": transaction.get("Student_Id"),
                    "Name": transaction.get("Name"),
                    "Title": book.get("Title"),
                    "Borrow_Date": book.get("Borrow_Date")
                })

        return borrowed_transactions  
    def check_book_borrow(self, book_id, student_id):
        book = self.warehouse_collection.find_one({"Book_Id": book_id})  
        user = self.users_collection.find_one({"Student_Id": student_id})
        if not book or not user:
            return "Nothing found"
        elif not book:
            return "Book not found"
        elif not user:
            return "Student not found"
        existing_borrow = self.invoices_collection.find_one({
            "Student_Id": student_id,
            "Books": {
                "$elemMatch": {
                    "Book_Id": book_id,
                    "Status": "Borrowed"
                }
            }
        })
        if existing_borrow:
            return "Book already borrowed"
        else:
            if book["Stock"] <= 0:
                    return "Book out of stock"
            else:
                # Update stock and borrowed count
                self.warehouse_collection.update_one(
                    {"Book_Id": book_id},
                    {"$inc": {"Stock": -1, "Borrowed_Count": 1}}
                )
                # Create new transaction 
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
        # Search for the transaction with "Borrowed" status
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
            return -1  # Not found transaction
        
        # Update "Returned" status and return date
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
            return -2  # Failed to update transaction.
        
        # Update warehouse data
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return -3  # No book found 
        
        new_stock = book.get("Stock", 0) + 1
        new_borrowed_count = book.get("Borrowed_Count", 0) - 1 if book.get("Borrowed_Count", 0) > 0 else 0
        
        update_book = self.warehouse_collection.update_one(
            {"Book_Id": book_id},
            {"$set": {"Stock": new_stock, "Borrowed_Count": new_borrowed_count}}
        )
        
        if update_book.modified_count == 0:
            return -4  # Warehouse update failed.
        
        return 1  # Return book successfully.


    def search_borrowed_books(self, search):
        query = {
        "$or": [
            {"Student_Id": {"$regex": search, "$options": "i"}},  
            {"Name": {"$regex": search, "$options": "i"}},        
            {"Books.Title": {"$regex": search, "$options": "i"}}  
            ]
        }

        transactions = self.invoices_collection.find(query)  
        results = []

        for transaction in transactions:
            for book in transaction.get("Books", []):
                if book.get("Status") == "Borrowed":
                    results.append({
                        "Book_Id": book.get("Book_Id"),
                        "Student_Id": transaction.get("Student_Id"),
                        "Name": transaction.get("Name"),
                        "Title": book.get("Title"),
                        "Borrow_Date": book.get("Borrow_Date")
                    })

        return results
    
    def show_book_api(self, search):
        query = {
            "$or": [
                {"Book_Id": {"$regex": search, "$options": "i"}},
                {"Title": {"$regex": search, "$options": "i"}},
                {"Author": {"$regex": search, "$options": "i"}},
                {"Genre": {"$regex": search, "$options": "i"}}
            ]
        }
        books = list(self.warehouse_collection.find(query))
        return books