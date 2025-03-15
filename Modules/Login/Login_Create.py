from tkinter import *
from PIL import Image, ImageTk
from Modules.Login.Login_Process import Login_Process as lp

def relative_to_assets(path: str) -> str:
    return f"./Images/Login/{path}"

class Login_Process_Create:
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x832")
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

        # Background Image
        self.background_image = PhotoImage(file=relative_to_assets("background.png"))
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Button forgot password
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_forgotpass.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Button Forgot Pass Clicked"),
            relief="flat"
        )
        self.button_1.place(x=496.0, y=658.0, width=296.0, height=30.0)

        # Button Login
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_login.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: lp.login_button_handle(self),
            relief="flat"
        )
        self.button_2.place(x=713.0, y=581.0, width=149.0, height=50.0)

        # Entry 
        self.entry_image_1 = PhotoImage(file=relative_to_assets("image_password.png"))
        self.canvas.create_image(645.0, 536.0, image=self.entry_image_1)
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(x=499.0, y=514.0, width=360.0, height=42.0)

        # Entry 2
        self.entry_image_2 = PhotoImage(file=relative_to_assets("image_username.png"))
        self.canvas.create_image(639.0, 459.0, image=self.entry_image_2)
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(x=498.0, y=437.0, width=360.0, height=42.0)
    
        self.window.resizable(False, False)
        self.window.mainloop()

if __name__ == "__main__":
    Login_Process_Create()