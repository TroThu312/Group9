import time
from tkinter import *  
from Modules.BorrowReturn.Borrow.Borrow_Book_Process import Borrow_Book_Process as bbp  
from PIL import Image, ImageTk  
import tkinter as tk


# Định nghĩa lớp giao diện Admin
class Borrow_Book_Create:

    def update_time(self):
        current_date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S")
        self.date_label.config(text=f"{current_date}")
        self.time_label.config(text=f"{current_time}")
        self.window.after(1000, self.update_time)
    def __init__(self, username):  
        self.window = Tk()  
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 1280
        self.window_height = 832
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#ffffff")  
        self.window.title('Borrow Book') 
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  

        # -----Background Image-----
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_borrow.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Back button-----

        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png")  
        self.back_button = Button(image=self.back_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=lambda: bbp.back_button_handle(self, username),
                                   relief="flat"
                                   )
        self.back_button.place(x=40, y=180, width=151, height=50)

        # -----reset button-----

        self.reset_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_reset.png")  
        self.reset_button = Button(image=self.reset_image,
                              borderwidth=0,
                              highlightthickness=0,
                              command=lambda: bbp.reset_button_handle(self),
                              relief="flat"
                              )
        self.reset_button.place(x=696, y=544, width=195, height=62)

        # -----submit button-----

        self.submit_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_submit.png")  
        self.submit_button = Button(image=self.submit_image,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: bbp.borrow_button_handle(self),
                               relief="flat"
                               )
        self.submit_button.place(x=397, y=544, width=195, height=62)

        # -----Bookid entry-----


        self.entry_bookid = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",

            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_bookid.place(
            x=509,
            y=371,
            width=434,
            height=60
        )

        # -----Studend id entry-----
        self.entry_studentid = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_studentid.place(
            x=509,
            y=446,
            width=434,
            height=60
        )
        # -----Show info-----
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85  , anchor="nw")
        self.update_time()

        # Non resizable window
        self.window.resizable(False, False)
        self.window.mainloop()
