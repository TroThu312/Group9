from tkinter import *  # Import toàn bộ thư viện Tkinter để tạo giao diện GUI
  # Import module xử lý sự kiện của admin
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button
import time
import tkinter as tk
from Modules.Book.Add.Add_Book_Process import Add_Book_Process as adp
def relative_to_assets(path: str) -> str:
    return f"./Images/Book/Add/{path}"
class Add_Book_Create:
    def update_time(self):
        current_date = time.strftime("%d/%m/%Y")
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
                                      (self.screen_width - self.window_width) // 2,
                                      self.window.winfo_y()))
        self.window.configure(bg="#ffffff")  # Đặt màu nền cho cửa sổ
        self.window.title('Borrow Book')  # Đặt tiêu đề của cửa sổ ứng dụng
        # self.window.iconphoto(False, PhotoImage(file = relative_to_assets("User/MainPage/UserIcon.png"))# Đặt icon cho cửa sổ

        # Tạo một canvas (vùng vẽ) để chứa hình ảnh và các nút bấm
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  # Đặt vị trí canvas trong cửa sổ
        # --- Hình nền  ---
        self.background_image = PhotoImage(file=f"./Images/Book/Add/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # ---- Button add --- 
        self.button_image_add = PhotoImage(file=f"./Images/Book/Add/button_add.png")
        self.button_add = Button(
            image=self.button_image_add,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: adp.add_button_handle(self),
            relief="flat")
        self.button_add.place(x=428.0,y=681.0,width=195.0,height=62.0)
       
        # ---- Button Reset --- 
        self.button_image_reset = PhotoImage (file=f"./Images/Book/Add/button_reset.png")
        self.button_reset = Button(
            image=self.button_image_reset,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: adp.reset_button_handle(self),
            relief="flat")
        self.button_reset.place(x=657.0,y=681.0,width=195.0,height=62.0)
        # ---- Button Back --- 
        self.button_image_back = PhotoImage (file=f"./Images/Book/Add/button_back.png")
        self.button_back = Button(
            image=self.button_image_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: adp.back_button_handle(self, username),
            relief="flat")
        self.button_back.place(x=41.0,y=181.0,width=151.0,height=50.0)
      # Hiển thị ngày & giờ
        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85  , anchor="nw")
        self.update_time()
        
        
    
    # ---- Dòng nhập liệu ---- 
        self.entry_book_id = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20)
        )
        self.entry_book_id.place(x=475.0, y=290.0, width=450.0, height=62.0)

        self.entry_title = Entry(
            bd = 5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20)
        )
        self.entry_title.place(x=475.0, y=367.0, width=450.0, height=62.0)
        
        self.entry_author = Entry(
            bd = 5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20)
        )
        self.entry_author.place(x=475.0, y=444.0, width=450.0, height=62.0)
        self.entry_genre = Entry(
            bd = 5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20)
        )
        self.entry_genre.place(x=475.0, y=521.0, width=450.0, height=62.0)
        self.entry_stock = Entry(
            bd = 5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20)
        )
        self.entry_stock.place(x=475.0, y=598.0, width=450.0, height=62.0)
        self.window.mainloop()
