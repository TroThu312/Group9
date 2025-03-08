from datetime import datetime
from APi.Main_Api import Api as main_api


class Book_Management_Api(main_api):

    def __init__(self):
        super().__init__()
        self.connector()

    def add_new_book(self, json_data):
        # Get Book_ID from json_data
        book_id = json_data["Book_Id"]
        # Get book information from Book_id in the collection
        book = self.warehouse_collection.find_one({'Book_Id': book_id})
        if book is None:
            # Check if the information in json_data is complete or not
            S = 0
            for key, value in json_data.items():
                if self.warehouse_collection.find_one({key: value}) is None:
                    S += 1
                else:
                    continue
            if S == 6:  # (Book_Id, Title, Author, Genre, Stock, Borrowed Count)
                # If all 6 pieces of information are available, add a new book to the database
                self.warehouse_collection.insert_one(json_data)
                return 0  # Success
            else:
                # Error: missing information
                return -1
        else:
            # Update the number of books in the database
            current_quantity = book["Stock"]
            if current_quantity < 30:
                new_quantity = current_quantity + json_data["Stock"]
                self.warehouse_collection.update_one(
                    {'Book_ID': book_id}, {'$set': {'Stock': new_quantity}})
                return 0  # Success
            else:
                # Error: book quantity is full
                return -2

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

