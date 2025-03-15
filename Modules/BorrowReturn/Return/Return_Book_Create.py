from datetime import datetime
from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
from tkinter.ttk import Treeview, Style
from Modules.BorrowReturn.Return.Return_Book_Process import Return_Book_Process as rbp
#import Return_Book_Process as rbp  # Import module xử lý sự kiện của admin
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button


# Định nghĩa lớp giao diện Admin
class Return_Book_Create:

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
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_return.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Nút quay lại-----
        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png")  # tạo ảnh button
        self.back_button = Button(image=self.back_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: rbp.back_button_handle(self, username),
                                  relief="flat"
                                  )
        self.back_button.place(x=40, y=180, width=151, height=50)

        # -----Nút reset-----
        self.reset_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_reset.png")  # tạo ảnh button
        self.reset_button = Button(image=self.reset_image,
                              borderwidth=0,
                              highlightthickness=0,
                              command=lambda: rbp.reset_button_handle(self),
                              relief="flat"
                              )
        self.reset_button.place(x=325, y=570, width=195, height=62)


        # -----Nút Search-----
        self.search_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_search.png")  # tạo ảnh button
        self.search_button = Button(image=self.search_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: rbp.search_button_handle(self),
                                    relief="flat"
                                    )
        self.search_button.place(x=1062, y=198, width=195, height=62)
        # -----Nút submit-----
        self.submit_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_submit.png")  # tạo ảnh button
        self.submit_button = Button(image=self.submit_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: rbp.return_button_handle(self),
                                    relief="flat"
                                    )
        self.submit_button.place(x=82, y=570, width=195, height=62)

        # -----Bookid entry-----

        self.entry_bookid = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_bookid.place(
            x=202,
            y=404,
            width=333,
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
            x=202,
            y=494,
            width=333,
            height=60
        )

        # -----Search entry-----
        self.entry_search = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_search.place(
            x=628,
            y=198,
            width=427,
            height=62
        )

        # -----Hiển thị thông tin-----
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date = Label(self.window, text="23/2/2025", font=("Inter", 20, "bold"), bg="#9CC8FF", fg="#3413AF")
        self.date.place(x=760, y=85, anchor="nw")
        self.time = Label(self.window, font=("Inter", 20, "bold"), bg="#9CC8FF", fg="#3413AF")
        self.time.place(x=1073, y=85, anchor="nw")

        def update_time():
            self.now_time = datetime.now().strftime("%H:%M:%S")  # Lấy thời gian hiện tại
            self.now_date = datetime.now().strftime("%d/%m/%Y")  # Lấy thời gian hiện tại
            self.time.config(text=self.now_time)  # Cập nhật vào Label
            self.date.config(text=self.now_date)
            self.window.after(1000, update_time)

        update_time()

        # # -----Hiển thị thông tin cho treeview-----
        # self.frame_tree = Frame(self.window)
        # self.frame_tree.place(x=576, y=282, width=680, height=490)

        # self.tree = Treeview(self.frame_tree)
        # self.tree["columns"] = ("Book ID", "Name", "Author", "Edition", "Quantity")

        # self.tree.column("#0", width=0, stretch=NO)  # Cột ẩn (dùng khi tạo cây)
        # self.tree.column("Book ID", anchor=CENTER, width=140)
        # self.tree.column("Name", anchor=W, width=300)
        # self.tree.column("Author", anchor=W, width=140)
        # self.tree.column("Edition", anchor=CENTER, width=80)
        # self.tree.column("Quantity", anchor=CENTER, width=80)

        # # Thêm tiêu đề
        # self.tree.heading("#0", text="", anchor=W)
        # self.tree.heading("Book ID", text="Book ID", anchor=CENTER)
        # self.tree.heading("Name", text="Name", anchor=CENTER)
        # self.tree.heading("Author", text="Author", anchor=CENTER)
        # self.tree.heading("Edition", text="Edition", anchor=CENTER)
        # self.tree.heading("Quantity", text="Quantity", anchor=CENTER)

        # # -------tạo scrollbar----------------
        # self.scroll_y = Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        # self.tree.configure(yscrollcommand=self.scroll_y.set)

        # # Tạo Scrollbar ngang
        # self.scroll_x = Scrollbar(self.frame_tree, orient="horizontal", command=self.tree.xview)
        # self.tree.configure(xscrollcommand=self.scroll_x.set)

        # # Đặt vị trí các thành phần
        # self.scroll_y.pack(side="right", fill="y")
        # self.scroll_x.pack(side="bottom", fill="x")
        # self.tree.pack(side="left", fill="both", expand=False)

        # # -------Thiết lập style cho treeview----------------
        # self.tree = Style()
        # self.tree.theme_use("default")
        # self.tree.configure("Treeview",
        #                background="#B9E3E9",  # Màu nền của bảng
        #                foreground="black",  # Màu chữ
        #                rowheight=30,  # Độ cao mỗi dòng
        #                font=("Arial", 15))
        # #-------heading----------------
        # self.tree.configure("Treeview.Heading",
        #                background="#B9E3E9",  # Màu nền của bảng
        #                foreground="black",  # Màu chữ
        #                # Độ cao mỗi dòng
        #                font=("Arial", 15))

        # Không cho phép thay đổi kích thước cửa sổ
        self.window.resizable(False, False)
        self.window.mainloop()
