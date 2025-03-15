from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
from Modules.Book.Remove.Remove_Book_Process import Remove_Book_Process as rbp
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button
import time
import tkinter as tk

class Remove_Book_Create:
    def update_time(self):
        current_date = time.strftime("%Y-%m-%d")
        current_time = time.strftime("%H:%M:%S")
        self.date_label.config(text=f"{current_date}")
        self.time_label.config(text=f"{current_time}")
        self.window.after(1000, self.update_time)

    def __init__(self, username):  # Phương thức khởi tạo class
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
        self.window.title('Borrow Book')  # Đặt tiêu đề của cửa sổ ứng dụng

        # Tạo một canvas (vùng vẽ) để chứa hình ảnh và các nút bấm
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  # Đặt vị trí canvas trong cửa sổ
        # --- Hình nền  ---
        self.background_image = PhotoImage(file=f"./Images/Book/Remove/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # ---- Button submit ---
        self.submit_button_image = PhotoImage(file=f"./Images/Book/Remove/submit_button.png")
        self.submit_button = Button(image=self.submit_button_image, borderwidth=0, highlightthickness=0,
                                    relief="flat",
                                    command=lambda: rbp.submit_button_handle(self) )
        self.submit_button.place(x=544.0, y=511.0, width=195.0, height=62.0)



        # ---- Button Back ---
        self.back_button_image = PhotoImage(file=f"./Images/Book/Remove/back_button.png")
        self.back_button = Button(image=self.back_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                  command=lambda: rbp.back_button_handle(self, username))
        # command = lambda: rbp.Remove_Book_Process.back_button_handle(self))
        self.back_button.place(x=41.0, y=181.0, width=151.0, height=50.0)


        # Hiển thị ngày & giờ
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85, anchor="nw")
        self.update_time()

        # ---- Dòng nhập liệu ----
        self.book_id_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20, 'bold'))
        self.book_id_entry.place(x=497.0, y=421.0, width=434.0, height=60.0)

        self.window.mainloop()
