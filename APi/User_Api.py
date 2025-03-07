from datetime import datetime
from APi.Main_Api import Api as main_api


class User_Api(main_api):

    def __init__(self):
        super().__init__()
        self.connector()

    def add_new_user(self, student_id, name, contact, address):
        user = self.users_collection.find_one({"Student_Id": student_id})
        if user is None:
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
        if user is None:
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

