import Modules.Login.Login_Create as lgv
if __name__ == "__main__":
    print("Library Management App started")
    # app = sho.Return_Book_Create()
    app = lgv.Login_Process_Create()
    app.window.mainloop()