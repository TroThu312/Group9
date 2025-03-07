from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
from PIL import ImageTk  # Phải thêm thư viện này để tạo ảnh button
from Modules.BorrowReturn.Borrow.Borrow_Book_Process import Borrow_Book_Process as bbp


# Định nghĩa lớp giao diện Admin
class Borrow_Book_Create:

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

        # -----Thêm hình nền-----
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_borrow.png")
        self.canvas.create_image(640.0, 428.0, image=self.background_image)

        # -----Nút quay lại-----
        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png")  # tạo ảnh button
        self.back_button = self.canvas.create_image(41, 181, image=self.back_image,
                                          anchor="nw")  # tạo button trên canva
        self.canvas.tag_bind(self.back_button, "<Button-1>",
                        lambda event: bbp.back_button_handle(self))  # Gọi hàm xử lý khi nhấn nút

        # -----Nút reset-----
        self.reset_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_reset.png")  # tạo ảnh button
        self.reset_button = self.canvas.create_image(706, 536, image=self.reset_image,
                                           anchor="nw")  # tạo button trên canva
        self.canvas.tag_bind(self.reset_button, "<Button-1>",
                        lambda event: bbp.reset_button_handle(self))  # Gọi hàm xử lý khi nhấn nút

        # -----Nút submit-----
        self.submit_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_submit.png")  # tạo ảnh button
        self.submit_button = self.canvas.create_image(398, 536, image=self.submit_image,
                                            anchor="nw")  # tạo button trên canva
        self.canvas.tag_bind(self.submit_button, "<Button-1>",
                        lambda event: bbp.borrow_button_handle(self))  # Gọi hàm xử lý khi nhấn nút

        # -----Bookid entry-----
        self.entry_bookid_image = PhotoImage(file=f"./Images/BorrowReturn/TextBox_borrow.png")
        self.canvas.create_image(601.62, 350.54, image=self.entry_bookid_image, anchor="nw")
        self.entry_bookid = Entry(
            bd=0,
            bg="#B8E2E9",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 14)
        )
        self.entry_bookid.place(
            x=615,
            y=355,
            width=287.0,
            height=40.0
        )

        # -----Studend id entry-----
        self.entry_studentid_image = PhotoImage(file=f"./Images/BorrowReturn/TextBox_borrow.png")
        self.canvas.create_image(601.62, 427.6, image=self.entry_studentid_image, anchor="nw")
        self.entry_studentid = Entry(
            bd=0,
            bg="#B8E2E9",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 14)
        )
        self.entry_studentid.place(
            x=615,
            y=431,
            width=287.0,
            height=40.0
        )



        # Không cho phép thay đổi kích thước cửa sổ
        self.window.resizable(False, False)

