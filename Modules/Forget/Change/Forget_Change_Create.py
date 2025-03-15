from tkinter import *
from PIL import Image, ImageTk
# import Modules.Forget.Change.Forget_Change_Process as fchp
class Forget_Change_Create:

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
        # file=f"./Images/MainPage/show_book_button.png"
        # Background Image
        self.background_image = PhotoImage(file=f"./Images/Forget/background_change.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Button change
        self.change_button_image = PhotoImage(file=f"./Images/Forget/change_button.png")
        self.change_button = Button(
            image=self.change_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("change"),
            relief="flat"
        )
        self.change_button.place(x=727.0, y=629.0, width=150.0, height=50.0)

        # Button back
        self.back_button_image = PhotoImage(file=f"./Images/Forget/back_button.png")
        self.back_button = Button(
            image=self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Back"),
            relief="flat"
        )
        self.back_button.place(x=365.0, y=192.0, width=82.0, height=67.0)

        # Entry - new
        self.new_entry = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font=('Arial', 20))
        self.new_entry.place(x=511.0, y=484.0, width=366.0, height=50.0)

        # Entry - confirm
        self.confirm_entry = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font=('Arial', 20))
        self.confirm_entry.place(x=511.0, y=549.0, width=366.0, height=50.0)

        self.window.resizable(False, False)
        self.window.mainloop()


