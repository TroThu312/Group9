from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv

class Api:
    def __init__(self):
        self.connector()

    # connect to mongodb
    def connector(self):
        load_dotenv(find_dotenv())
        host = os.getenv("HOSTNAME")
        # Dùng MongoDB Atlas thay vì Local
        self.client = MongoClient(host)

        # Chọn cơ sở dữ liệu
        self.db = self.client['Group9']

        # Chọn các collection
        self.admin_collection = self.db['admin']
        self.users_collection = self.db['users']
        self.warehouse_collection = self.db['books']
        self.invoices_collection = self.db['transactions']

# Kiểm tra kết nối
if __name__ == "__main__":
    api = Api()
    print("Connected to MongoDB successfully!")
    print("Collections:", api.db.list_collection_names())
