from datetime import datetime
from APi.Main_Api import Api as main_api


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
        # Kiểm tra trùng lặp theo Book_Id
        existing_book_by_id = self.warehouse_collection.find_one({'Book_Id': book_id})
        if existing_book_by_id:
            # Nếu sách đã tồn tại, cập nhật số lượng sách
            current_quantity = existing_book_by_id["Stock"]
            if current_quantity < 30:
                new_quantity = min(30, current_quantity + stock)  # Đảm bảo không vượt quá 30
                self.warehouse_collection.update_one(
                    {'Book_Id': book_id}, {'$set': {'Stock': new_quantity}})
                return 0  # Thành công
            else:
                return -2  # Số lượng sách đã đầy
        # Kiểm tra trùng lặp theo Title, Author, Genre
        existing_book_by_info = self.warehouse_collection.find_one({
            'Title': title,
            'Author': author,
            'Genre': genre
        })
        if existing_book_by_info:
            # Nếu Title, Author, Genre đã tồn tại → Báo lỗi
            return -3
        # Get book information from Book_id in the collection
        required_fields = {"Book_Id", "Title", "Author", "Genre", "Stock"}
        if required_fields.issubset(json_data.keys()):
            json_data.setdefault("Borrowed_Count", 0)
            self.warehouse_collection.insert_one(json_data)
            return 0  # Thành công
        else:
            return -1  # Thiếu thông tin


    def update_items(self, json_data, book_id):
        # Get book information from json_data
        book = self.warehouse_collection.find_one({'Book_ID': book_id})
        _id = book['_id']  # Get the ID of the book
        if 'Book_ID' in json_data:
            if self.warehouse_collection.find_one({'Book_ID': json_data['Book_ID']}) is not None:
                return -2  # Error: Book_ID already exists in the database
        updated_fields = {}
        if 'Genre' in json_data:
            try:
                datetime.datetime.strptime(json_data['Genre'], "%Y/%m/%d")
                updated_fields['Genre'] = json_data['Genre']
            except ValueError:
                return -3  # Error: Genre format is incorrect
        if 'Film' in json_data:
            updated_fields['Film'] = json_data['Film']
        if 'Author' in json_data:
            updated_fields['Author'] = json_data['Author']
        # Update the book information in the database
        if updated_fields:
            self.warehouse_collection.update_one({'Book_ID': book_id}, {'$set': updated_fields})
            return 0  # Update successful
        else:
            # No new information was updated
            return -1

    def remove_items(self, book_id):
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return "Not found"
        else:
            book_id = book['Book_Id']  # get id of book
            self.warehouse_collection.delete_one({'Book_Id': book_id})
            return "Done"
    def update_book_quantity(self, book_id, quantity, action):
        book = self.warehouse_collection.find_one({'Book_Id': book_id})
        if not book:
            return -1  # Sách không tồn tại

        current_stock = book.get("Stock", 0)
        if action == "add":
            new_stock = current_stock + quantity
        elif action == "remove":
            if quantity > current_stock:
                return -2  # Không đủ số lượng để trừ
            new_stock = current_stock - quantity
        else:
                return -3  # Action không hợp lệ

        self.warehouse_collection.update_one({'Book_Id': book_id}, {'$set': {'Stock': new_stock}})
        return 0
    def update_book_info(self, book_id, update_data):
        book = self.warehouse_collection.find_one({"Book_Id": book_id})
        if not book:
            return -1
        
        self.warehouse_collection.update_one({"Book_Id": book_id}, {"$set": update_data})
        return 0
