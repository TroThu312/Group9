from tkinter import *
import Modules.MainPage.Main_View_Process as mvp
from PIL import Image, ImageTk
import time
import tkinter as tk


class Main_View_Create:
    def update_time(self):
        current_date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S")
        self.date_label.config(text=f"{current_date}")
        self.time_label.config(text=f"{current_time}")
        self.window.after(1000, self.update_time)

    def __init__(self):  # Phương thức khởi tạo class
        self.window = Tk()  # Khởi tạo cửa sổ giao diện chính

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
        self.window.configure(bg="#ffffff")  # Đặt màu nền cho cửa sổ
        self.window.title('Admin')  # Đặt tiêu đề của cửa sổ ứng dụng
        # self.window.iconphoto(False, PhotoImage(file = f"./Images/User/MainPage/UserIcon.png"))# Đặt icon cho cửa sổ

        # Tạo một canvas (vùng vẽ) để chứa hình ảnh và các nút bấm
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  # Đặt vị trí canvas trong cửa sổ

        # -----Thêm hình nền-----.
        self.background_image = PhotoImage(file=f"./Images/MainPage/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Hiển thị ngày giờ
        self.date_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85, anchor="nw")
        self.update_time()

        # -----Các nút-----

        self.show_book_button_image = PhotoImage(file=f"./Images/MainPage/show_book_button.png")
        self.show_book_button = Button(image=self.show_book_button_image, borderwidth=0,
                                       highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.show_book_button_handle(self))
        # command = lambda: mvp.Main_View_Process.show_book_button_handle(self))
        self.show_book_button.place(x=1012.0, y=477, width=195, height=59)

        self.logout_button_image = PhotoImage(file=f"./Images/MainPage/logout_button.png")
        self.logout_button = Button(image=self.logout_button_image, borderwidth=0,
                                    highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.log_out_button_handle(self))
        # command = lambda: mvp.Main_View_Process.logout_button_handle(self))
        self.logout_button.place(x=1012.0, y=558, width=195, height=59)

        self.return_book_button_image = PhotoImage(file=f"./Images/MainPage/return_book_button.png")
        self.return_book_button = Button(image=self.return_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.return_book_button_handle(self) )
        # command = lambda: mvp.Main_View_Process.return_book_button_handle(self))
        self.return_book_button.place(x=1012.0, y=389, width=195, height=59)

        self.borrow_book_button_image = PhotoImage(file=f"./Images/MainPage/borrow_book_button.png")
        self.borrow_book_button = Button(image=self.borrow_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.borrow_book_button_handle(self))
        # command = lambda: mvp.Main_View_Process.borrow_book_button_handle(self))
        self.borrow_book_button.place(x=1012.0, y=308, width=195, height=59)

        self.add_book_button_image = PhotoImage(file=f"./Images/MainPage/add_book_button.png")
        self.add_book_button = Button(image=self.add_book_button_image, borderwidth=0,
                                      highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.add_book_button_handle(self))
        # command = lambda: mvp.Main_View_Process.add_book_button_handle(self))
        self.add_book_button.place(x=781.0, y=308, width=195, height=59)

        self.update_book_button_image = PhotoImage(file=f"./Images/MainPage/update_book_button.png")
        self.update_book_button = Button(image=self.update_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat",command = lambda: mvp.Main_View_Process.update_book_button_handle(self) )
        # command = lambda: mvp.Main_View_Process.update_book_button_handle(self))
        self.update_book_button.place(x=781.0, y=390, width=195, height=59)

        self.remove_book_button_image = PhotoImage(file=f"./Images/MainPage/remove_book_button.png")
        self.remove_book_button = Button(image=self.remove_book_button_image, borderwidth=0,
                                         highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.remove_book_button_handle(self) )
        # command = lambda: mvp.Main_View_Process.remove_book_button_handle(self))
        self.remove_book_button.place(x=781.0, y=477, width=195, height=59)

        self.add_update_user_button_image = PhotoImage(file=f"./Images/MainPage/add_update_user_button.png")
        self.add_update_user_button = Button(image=self.add_update_user_button_image, borderwidth=0,
                                             highlightthickness=0, relief="flat", command = lambda: mvp.Main_View_Process.add_update_user_button_handle(self))
        # command = lambda: mvp.Main_View_Process.add_update_user_button_handle(self))
        self.add_update_user_button.place(x=781.0, y=558, width=195, height=59)

        self.window.resizable(False, False)  # Không cho phép thay đổi kích thước cửa sổ

        self.window.mainloop()


