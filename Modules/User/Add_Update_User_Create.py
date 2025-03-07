from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
from Modules.User.Add_Update_User_Process import Add_Update_User_Process as uup  # Import module xử lý sự kiện của admin
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button
import time
import tkinter as tk


class Update_User_Create:
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
        self.window.title('Borrow Book')  # Đặt tiêu đề của cửa sổ ứng dụng
        # self.window.iconphoto(False, PhotoImage(file = f"./Images/User/MainPage/UserIcon.png"))# Đặt icon cho cửa sổ

        # Tạo một canvas (vùng vẽ) để chứa hình ảnh và các nút bấm
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  # Đặt vị trí canvas trong cửa sổ
        # --- Hình nền  ---
        self.background_image = PhotoImage(file=f"./Images/update_user/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)



        # ---- Button add ---
        self.add_button_image = PhotoImage(file=f"./Images/update_user/add_button.png")
        self.add_button = Button(image=self.add_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                 command=lambda: uup.add_button_handle(self))
        # command = lambda: uup.Update_User_Process.add_button_handle(self))
        self.add_button.place(x=326.0, y=637.0, width=195.0, height=62.0)

        # ---- Button update-
        self.update_button_image = PhotoImage(file=f"./Images/update_user/update_button.png")
        self.update_button = Button(image=self.update_button_image, borderwidth=0, highlightthickness=0,
                                    relief="flat",command=lambda: uup.update_button_handle(self))
        # command = lambda: uup.Update_User_Process.update_button_handle(self))
        self.update_button.place(x=543.0, y=637.0, width=195.0, height=62.0)

        # ---- Button reset ---
        self.reset_button_image = PhotoImage(file=f"./Images/update_user/reset_button.png")
        self.reset_button = Button(image=self.reset_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                   command=lambda: uup.reset_button_handle(self))

        self.reset_button.place(x=760.0, y=637.0, width=195.0, height=62.0)

        # ---- Button Back ---
        self.back_button_image = PhotoImage(file=f"./Images/update_user/back_button.png")
        self.back_button = Button(image=self.back_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                  command=lambda: uup.back_button_handle(self))

        self.back_button.place(x=41.0, y=181.0, width=151.0, height=50.0)

        # Hiển thị ngày & giờ
        self.date_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85, anchor="nw")
        self.update_time()

        # ---- Dòng nhập liệu ----
        self.student_id_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                      font=('Arial', 20, 'bold'))
        self.student_id_entry.place(x=508.0, y=317.0, width=434.0, height=62.0)

        self.name_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                font=('Arial', 20, 'bold'))
        self.name_entry.place(x=508.0, y=394.0, width=434.0, height=62.0)

        self.contact_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20, 'bold'))
        self.contact_entry.place(x=508.0, y=471.0, width=434.0, height=62.0)

        self.address_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20, 'bold'))
        self.address_entry.place(x=508.0, y=548.0, width=434.0, height=62.0)

        self.window.mainloop()


if __name__ == "__main__":
    Update_User_Create()