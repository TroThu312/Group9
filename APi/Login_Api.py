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
        return 0 # Login Sucess