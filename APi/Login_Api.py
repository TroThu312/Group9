import APi.Main_Api as main_api
class Login_Api(main_api.Api):
    def __init__(self):
        super().__init__()
        self.connector()
    
    def check_user_login(self,username_or_email,password):
        if not username_or_email or not password:
            return -1 # Empty username or password
        if "@" in username_or_email:
            user = self.admin_collection.find_one({"Email": username_or_email})
        else:
            user = self.admin_collection.find_one({'Username':username_or_email})
        if not user:
            return -2  # User not found
        if user['Password'] != password:
            return -3 # Incorrect password
        return user["Username"]
    
    def check_admin_email(self,email):
        check = self.admin_collection.find_one({'Email':email})
        if not check:
            return -1 # Email not found
        else:
            return 0 # Email found
        
    def change_password(self,username,password):
        self.admin_collection.update_one({'Email':username},{'$set':{'Password':password}})