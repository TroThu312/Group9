from datetime import datetime
from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
from Modules.BorrowReturn.Borrow.Borrow_Book_Process import Borrow_Book_Process as bbp  # Import module xử lý sự kiện của admin
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button


# Định nghĩa lớp giao diện Admin
class Borrow_Book_Create:

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
        # self.window.iconphoto(False, PhotoImage(file = f"../../../Images/BorrowReturn/User/MainPage/UserIcon.png"))# Đặt icon cho cửa sổ

        # Tạo một canvas (vùng vẽ) để chứa hình ảnh và các nút bấm
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  # Đặt vị trí canvas trong cửa sổ

        # -----Thêm hình nền-----
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_borrow.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Nút quay lại-----

        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png")  # tạo ảnh button
        self.back_button = Button(image=self.back_image,
                                   borderwidth=0,
                                   highlightthickness=0,
                                   command=lambda: bbp.back_button_handle(self, username),
                                   relief="flat"
                                   )
        self.back_button.place(x=40, y=180, width=151, height=50)

        # -----Nút reset-----

        self.reset_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_reset.png")  # tạo ảnh button
        self.reset_button = Button(image=self.reset_image,
                              borderwidth=0,
                              highlightthickness=0,
                              command=lambda: bbp.reset_button_handle(self),
                              relief="flat"
                              )
        self.reset_button.place(x=696, y=544, width=195, height=62)

        # -----Nút submit-----

        self.submit_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_submit.png")  # tạo ảnh button
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
        # -----Hiển thị thông tin-----
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85  , anchor="nw")
        self.update_time()

        def update_time():
            self.now_time = datetime.now().strftime("%H:%M:%S")  # Lấy thời gian hiện tại
            self.now_date = datetime.now().strftime("%d/%m/%Y")  # Lấy thời gian hiện tại
            self.time.config(text=self.now_time)  # Cập nhật vào Label
            self.date.config(text=self.now_date)
            self.window.after(1000, update_time)

        update_time()

        # Không cho phép thay đổi kích thước cửa sổ
        self.window.resizable(False, False)
        self.window.mainloop()
