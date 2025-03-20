from tkinter import *
from PIL import Image, ImageTk
import Modules.Login.Login_Process as lgp

class Login_Process_Create:
    
    def __init__(self):
        self.window = Tk()
        # Lấy kích thước màn hình của máy tính
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        # Thiết lập kích thước cửa sổ ứng dụng
        self.window_width = 1280
        self.window_height = 832
        # Căn giữa cửa sổ ứng dụng trên màn hình
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Login")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        #file=f"./Images/MainPage/show_book_button.png"
        # Background Image
        self.background_image = PhotoImage(file=f"./Images/Login/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Button forgot password
        self.button_forgetpassword_image = PhotoImage(file=f"./Images/Login/button_forgetpassword.png")
        self.button_forgetpassword = Button(
            image=self.button_forgetpassword_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: lgp.Login_Process.forget_button_handle(self),
            relief="flat"
        )
        self.button_forgetpassword.place(x=483.0, y=574.0, width=180.0, height=30.0)

        # Button Login
        self.button_login_image = PhotoImage(file=f"./Images/Login/button_login.png")
        self.button_login = Button(
            image=self.button_login_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: lgp.Login_Process.login_button_handle(self),
            relief="flat"
        )
        self.button_login.place(x=709.0, y=629.0, width=140.0, height=50.0)

        # Entry 1 - Password
        self.password_entry = Entry(
            bd=5,
            show="*",
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font=('Arial', 20))
        self.password_entry.place(x=483.0, y=509.0, width=366.0, height=50.0)

        # Entry 2 - Username
        self.name_entry = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font=('Arial', 20))
        self.name_entry.place(x=483.0, y=440.0, width=366.0, height=50.0)
    
        self.window.resizable(False, False)
        self.window.mainloop()
