from APi.Main_Api import Api as main_api
from tkinter import messagebox

class Book_Management_Api(main_api):

    def __init__(self):
        super().__init__()
        self.connector()
    def get_book_info(self, book_id):
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        return book
    def get_books_info(self):
        all_books = self.warehouse_collection.find()
        list_of_book = []
        for book in all_books:
            list_of_book.append({
                "Book_Id": book.get("Book_Id"),
                "Title": book.get("Title"),
                "Author": book.get("Author"),
                "Genre": book.get("Genre"),
                "Stock": book.get("Stock")
            })
        return list_of_book
    def add_new_book(self, json_data):
        book_id = json_data["Book_Id"]
        title = json_data["Title"]
        author = json_data["Author"]
        genre = json_data["Genre"]
        stock = json_data["Stock"]
        # Check Book_Id duplication
        existing_book_by_id = self.warehouse_collection.find_one({'Book_Id': book_id})
        if existing_book_by_id:
            # If Book_Id already exists → Update the quantity
            current_quantity = existing_book_by_id["Stock"]
            if current_quantity < 30:
                new_quantity = min(30, current_quantity + stock)  
                self.warehouse_collection.update_one(
                    {'Book_Id': book_id}, {'$set': {'Stock': new_quantity}})
                messagebox.showinfo("Success", "Book quantity updated successfully")
                return 0  # Success
            else:
                return -2  # Error: Quantity exceeds the limit
        # Check Title, Author, Genre duplication
        existing_book_by_info = self.warehouse_collection.find_one({
            'Title': title,
            'Author': author,
            'Genre': genre
        })
        if existing_book_by_info:
            return -3
        # Get book information from Book_id in the collection
        required_fields = {"Book_Id", "Title", "Author", "Genre", "Stock"}
        if required_fields.issubset(json_data.keys()):
            json_data.setdefault("Borrowed_Count", 0)
            self.warehouse_collection.insert_one(json_data)
            return 0  # Success
        else:
            return -1  # Missing required fields

    def remove_items(self, book_id):
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return "Not found"
        else:
            reply = messagebox.askyesno("Delete", "Are you sure you want to delete this product?")
            if reply:
                self.warehouse_collection.delete_one({'Book_Id': book_id})
                return "Done"
            
    def update_book_quantity(self, book_id, quantity, action):
        book = self.warehouse_collection.find_one({'Book_Id': book_id})
        if not book:
            return -1  # Book is not existed

        current_stock = book.get("Stock", 0)
        if action == "add":
            new_stock = current_stock + quantity
        elif action == "remove":
            if quantity > current_stock:
                return -2  # Not enough quantity to decrease
            new_stock = current_stock - quantity
        else:
                return -3  # Action invalid

        self.warehouse_collection.update_one({'Book_Id': book_id}, {'$set': {'Stock': new_stock}})
        return 0
    def update_book_info(self, book_id, update_data):
        if not book_id.isdigit():
            return -1
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return -1
        
        self.warehouse_collection.update_one({"Book_Id": book_id}, {"$set": update_data})
        return 0
