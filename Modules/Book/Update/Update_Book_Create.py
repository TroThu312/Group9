from datetime import datetime
from tkinter import *  
from PIL import ImageTk  
from Modules.Book.Update.Update_Book_Process import Update_Book_Process as ubp
import time
from tkinter import messagebox 

class Update_Book_Create:
    def update_time(self):
        current_date = time.strftime("%d/%m/%Y")
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
        self.window.title('Update Book') 
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  

        # -----Background image-----
        self.background_image = PhotoImage(file=f"./Images/Book/Update/background_update.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Back button-----

        self.back_image = ImageTk.PhotoImage(file=f"./Images/Book/Update/button_back.png")  
        self.back_button = Button(image=self.back_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=lambda: ubp.back_button_handle(self, username),
                                   relief="flat"
                                   )
        self.back_button.place(x=40, y=180, width=151, height=50)

        # -----Add button-----

        self.add_image = ImageTk.PhotoImage(file=f"./Images/Book/Update/button_add.png")  
        self.add_button = Button(image=self.add_image,
                              borderwidth=0,
                              highlightthickness=0,
                              command=lambda: ubp.add_book_button_handle(self),
                              relief="flat"
                              )
        self.add_button.place(x=104, y=576, width=195, height=62)

        # -----Remove button-----

        self.remove_image = ImageTk.PhotoImage(file=f"./Images/Book/Update/button_remove.png")  
        self.remove_button = Button(image=self.remove_image,
                               borderwidth=0,
                               highlightthickness=0,
                               command=lambda: ubp.remove_book_button_handle(self),
                               relief="flat"
                               )
        self.remove_button.place(x=357, y=576, width=195, height=62)

        # -----Update button-----

        self.update_image = ImageTk.PhotoImage(file=f"./Images/Book/Update/button_update.png")  
        self.update_button = Button(image=self.update_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: ubp.update_book_info(self),
                                    relief="flat"
                                    )
        self.update_button.place(x=715, y=676, width=195, height=62)

        # ---- Reset button-----

        self.reset_image = ImageTk.PhotoImage(file=f"./Images/Book/Update/button_reset.png")  
        self.reset_button = Button(image=self.reset_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: ubp.reset(self),
                                    relief="flat"
                                    )
        self.reset_button.place(x=982, y=676, width=195, height=62)

        # -----Bookid entry quantity-----


        self.entry_bookid_quantity = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",

            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_bookid_quantity.place(
            x=269,
            y=403,
            width=319,
            height=60
        )

        # ----- Quantity entry-----
        self.entry_quantity = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_quantity.place(
            x=269,
            y=486,
            width=319,
            height=60
        )

        # ----- Bookid infor entry-----
        self.entry_bookid_info = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_bookid_info.place(
            x=850,
            y=322,
            width=360,
            height=60
        )

        # ----- title entry-----
        self.entry_title = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_title.place(
            x=850,
            y=406,
            width=360,
            height=60
        )
        # ----- author entry-----
        self.entry_author = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_author.place(
            x=850,
            y=490,
            width=360,
            height=60
        )

        # ----- genre entry-----
        self.entry_genre = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_genre.place(
            x=850,
            y=574,
            width=360,
            height=60
        )

        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85  , anchor="nw")
        self.update_time()

        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()
    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 
