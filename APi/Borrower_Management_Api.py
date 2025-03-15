import APi.Main_Api as main_api

class Borrower_Management_Api(main_api.Api):
    def __init__(self):
        super().__init__()
        self.connector()
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
       