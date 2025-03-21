from tkinter import *
import Modules.MainPage.Main_View_Process as mvp
import time
import tkinter as tk
from tkinter import messagebox 

class Main_View_Create:
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
                                      (self.screen_width - self.window_width) // 2,
                                      self.window.winfo_y()))
        self.window.configure(bg="#FFFFFF")
        self.window.title('Admin')  

        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  

        # -----Background image-----.
        self.background_image = PhotoImage(file=f"./Images/MainPage/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Date and time label
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85, anchor="nw")
        self.update_time()

        # -----Buttons-----

        self.show_book_button_image = PhotoImage(file=f"./Images/MainPage/show_book_button.png")
        self.show_book_button = Button(image=self.show_book_button_image, borderwidth=0,
                                       highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.show_book_button_handle(self, username))
        self.show_book_button.place(x=1012.0, y=477, width=195, height=59)

        self.logout_button_image = PhotoImage(file=f"./Images/MainPage/logout_button.png")
        self.logout_button = Button(image=self.logout_button_image, borderwidth=0,
                                    highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.log_out_button_handle(self))
        self.logout_button.place(x=1012.0, y=558, width=195, height=59)

        self.return_book_button_image = PhotoImage(file=f"./Images/MainPage/return_book_button.png")
        self.return_book_button = Button(image=self.return_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.return_book_button_handle(self, username) )
        self.return_book_button.place(x=1012.0, y=389, width=195, height=59)

        self.borrow_book_button_image = PhotoImage(file=f"./Images/MainPage/borrow_book_button.png")
        self.borrow_book_button = Button(image=self.borrow_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.borrow_book_button_handle(self,  username))
        self.borrow_book_button.place(x=1012.0, y=308, width=195, height=59)

        self.add_book_button_image = PhotoImage(file=f"./Images/MainPage/add_book_button.png")
        self.add_book_button = Button(image=self.add_book_button_image, borderwidth=0,
                                      highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.add_book_button_handle(self,  username))
        self.add_book_button.place(x=781.0, y=308, width=195, height=59)

        self.update_book_button_image = PhotoImage(file=f"./Images/MainPage/update_book_button.png")
        self.update_book_button = Button(image=self.update_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.update_book_button_handle(self,  username) )
        self.update_book_button.place(x=781.0, y=390, width=195, height=59)

        self.remove_book_button_image = PhotoImage(file=f"./Images/MainPage/remove_book_button.png")
        self.remove_book_button = Button(image=self.remove_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.remove_book_button_handle(self, username) )
        self.remove_book_button.place(x=781.0, y=477, width=195, height=59)

        self.add_update_user_button_image = PhotoImage(file=f"./Images/MainPage/add_update_user_button.png")
        self.add_update_user_button = Button(image=self.add_update_user_button_image, borderwidth=0,
                                             highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.add_update_user_button_handle(self,  username))
        self.add_update_user_button.place(x=781.0, y=558, width=195, height=59)

        self.window.resizable(False, False)  
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()
    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 


