from APi.Main_Api import Api as main_api


class User_Api(main_api):

    def __init__(self):
        super().__init__()
        self.connector()

    def get_user_info(self):
        users = self.users_collection.find()
        return users

    def search_user(self, search_value):
        query = {
            "$or": [
                {"Student_Id": {"$regex": search_value, "$options": "i"}},  
                {"Name": {"$regex": search_value, "$options": "i"}} 
            ]
        }
        results = list(self.users_collection.find(query, {"_id": 0})) 
        return results


    def add_new_user(self, student_id, name, contact, address):
        user = self.users_collection.find_one({"Student_Id": student_id})
        sdt = self.users_collection.find_one({"Contract": contact})
        if user is None and sdt is None:
            new_user = {
                "Student_Id": student_id,
                "Name": name,
                "Contract": contact,
                "Address": address
                }
            self.users_collection.insert_one(new_user)
            return "Available"
        else:
            return "Not Available"

    def update_user(self, student_id, name, contact, address):
        user = self.users_collection.find_one({"Student_Id": student_id})
        sdt = self.users_collection.find_one({"Contract": contact})

        if user is None or sdt is None:
            return "Not Found"
        else:
            updated_fields = {}
            if name:
                updated_fields['Name'] = name
            if contact:
                updated_fields['Contact'] = contact
            if address:
                updated_fields['Address'] = address
            self.users_collection.update_one(
                {"Student_Id": student_id},
                {"$set": updated_fields}
            )
            return "Updated"

