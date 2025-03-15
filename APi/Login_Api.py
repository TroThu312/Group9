import APi.Main_Api as main_api
class Login_Api(main_api.Api):
    def __init__(self):
        super().__init__()
        self.connector()
    
    def check_user_login(self,username,password):
        if not username or not password:
            return -1 # Empty username or password
        user = self.admin_collection.find_one({'Username':username})
        if not user:
            return -2  # User not found
        if user['Password'] != password:
            return -3 # Incorrect password
        return 0 # Login Success
    
    def check_admin_email(self,email):
        check = self.admin_collection.find_one({'Email':email})
        if not check:
            return -1 # Email not found
        else:
            return 0 # Email found
        
    def change_password(self,username,password):
        self.admin_collection.update_one({'Email':username},{'$set':{'Password':password}})