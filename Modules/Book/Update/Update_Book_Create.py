from tkinter import *  
from PIL import Image, ImageTk  # Phải thêm thư viện này để tạo ảnh button
import time
import tkinter as tk
def relative_to_assets(path: str) -> str:
    return f"./Images/Book/Update/{path}"
class Update_Book_Create:
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
        self.window.configure(bg="#ffffff")  
        self.window.title('Borrow Book')  
    

        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0) 
        # --- Hình nền  ---
        self.background_image = PhotoImage(file=relative_to_assets("background.png"))
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # ---- Button add --- 
        self.button_image_add = PhotoImage(file=relative_to_assets("button_add.png"))
        self.button_add = Button(
            image=self.button_image_add,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Button add Clicked"),
            relief="flat"
        )
        self.button_add.place(x=432.0,y=589.0,width=195.0,height=62.0)
       
        # ---- Button Remove --- 
        self.button_image_remove = PhotoImage (file=relative_to_assets("button_remove.png"))
        self.button_remove = Button(
            image=self.button_image_remove,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Button Remove Clicked"),
            relief="flat")
        self.button_remove.place(x=653.0,y=589.0,width=195.0,height=62.0)
        # ---- Button Back --- 
        self.button_image_back = PhotoImage (file=relative_to_assets("button_back.png"))
        self.button_back = Button(
            image=self.button_image_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Button Back Clicked"),
            relief="flat")
        self.button_back.place(x=41.0,y=181.0,width=151.0,height=50.0)
      # Hiển thị ngày & giờ
        self.date_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.date_label.place(x=745, y=85, anchor="nw")
        self.time_label = tk.Label(self.window, font=("Inter", 20,"bold"), bg="#9BC8FF")
        self.time_label.place(x=1104, y=85  , anchor="nw")
        self.update_time()
        
    
      # ---- Dòng nhập liệu ---- 
        self.canvas.create_image(714.0, 446.0)
        self.entry_book_id = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20,'bold')
        )
        self.entry_book_id.place(x=497.0, y=415.0, width=434.0, height=60.0)
        self.canvas.create_image(714,523)
        self.entry_quantity = Entry(
            bd = 5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font = ('Arial',20,'bold')
        )
        self.entry_quantity.place(x=497.0, y=492.0, width=434.0, height=60.0)
        self.window.mainloop()
if __name__ == "__main__":
    Update_Book_Create()