import Modules.BorrowReturn.Show.Show_Book_Process as sbp
from datetime import datetime
from tkinter import *  
from tkinter.ttk import Style, Treeview
from PIL import ImageTk  
from tkinter import messagebox 
import APi.Book_Management_Api as bma

class Show_Book_Create:

    def __init__(self, username): 
        self.window = Tk()  
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 1280
        self.window_height = 832
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                      (self.screen_width - self.window_width) // 2,
                                      self.window.winfo_y()))
        self.window.configure(bg="#ffffff")  
        self.window.title('Borrow Book') 
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  

        # -----Background image-----
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_show.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Back button-----
        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png")  
        self.back_button = self.canvas.create_image(41, 181, image=self.back_image,
                                          anchor="nw") 
        self.canvas.tag_bind(self.back_button, "<Button-1>",
                        lambda event: sbp.Show_Book_Process.back_button_handle(self, username))  


        # -----Search button-----

        self.search_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_search.png")  
        self.search_button = Button(image=self.search_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: sbp.Show_Book_Process.show_button_handle(self),
                                    relief="flat"
                                    )
        self.search_button.place(x=805, y=265, width=195, height=62)

        self.entry_search = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.entry_search.place(
            x=366,
            y=265,
            width=427,
            height=62
        )

        self.name = Label(self.window, text= username, font=("Inter", 20, "bold"), bg="#9BC8FF")
        self.name.place(x=150, y=85, anchor="nw")
        self.date = Label(self.window, text="23/2/2025", font=("Inter", 20, "bold"), bg="#9CC8FF")
        self.date.place(x=760, y=85, anchor="nw")
        self.time = Label(self.window, font=("Inter", 20, "bold"), bg="#9CC8FF")
        self.time.place(x=1073, y=85, anchor="nw")

        def update_time():
            self.now_time = datetime.now().strftime("%H:%M:%S")  
            self.now_date = datetime.now().strftime("%d/%m/%Y") 
            self.time.config(text=self.now_time)  
            self.date.config(text=self.now_date)
            self.window.after(1000, update_time)
        update_time()
        self.setup_treeview()
        self.load_data()
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

        
    def setup_treeview(self):
        self.frame_tree = Frame(self.window)
        self.frame_tree.place(x=75, y=350, width=1130, height=365)

        self.tree = Treeview(self.frame_tree)
        self.tree["columns"] = ("Book ID", "Title", "Author", "Genre", "Stock")

        self.tree.column("#0", width=0, stretch=NO)  
        self.tree.column("Book ID", anchor=CENTER, width=240)
        self.tree.column("Title", anchor=W, width=360)
        self.tree.column("Author", anchor=W, width=220)
        self.tree.column("Genre", anchor=CENTER, width=150)
        self.tree.column("Stock", anchor=CENTER, width=120)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Book ID", text="Book ID", anchor=CENTER)
        self.tree.heading("Title", text="Title", anchor=CENTER)
        self.tree.heading("Author", text="Author", anchor=CENTER)
        self.tree.heading("Genre", text="Genre", anchor=CENTER)
        self.tree.heading("Stock", text="Stock", anchor=CENTER)

        self.scroll_y = Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x = Scrollbar(self.frame_tree, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_y.pack(side="right", fill="y")
        self.scroll_x.pack(side="bottom", fill="x")
        self.tree.pack(side="left", fill="both", expand=False)

        self.style = Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                            background="#B9E3E9",  
                            foreground="black",  
                            rowheight=25, 
                            font=("Arial", 15))

        self.style.configure("Treeview.Heading",
                            background="#B9E3E9",  
                            foreground="black",  
                            font=("Arial", 15))
    
    def load_data(self):
        api = bma.Book_Management_Api()
        results = api.get_books_info()
        self.tree.delete(*self.tree.get_children())
        for row in results:
            self.tree.insert("", "end", values=(row.get("Book_Id"), row.get("Title"), row.get("Author"), row.get("Genre"), row.get("Stock")))

    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 
