from datetime import datetime
from tkinter import *  
from tkinter.ttk import Treeview, Style
from APi.Borrow_Return_Management_Api import BorrowReturnManagementApi
from Modules.BorrowReturn.Return.Return_Book_Process import Return_Book_Process as rbp
from PIL import ImageTk 
from tkinter import messagebox 

class Return_Book_Create:

    def __init__(self, username): 
        self.window = Tk()  
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 1280
        self.window_height = 832
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#ffffff")  
        self.window.title('Return Book') 
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  

        # -----Background image-----
        self.background_image = PhotoImage(file=f"./Images/BorrowReturn/background_return.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # -----Back button-----
        self.back_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_back.png") 
        self.back_button = Button(image=self.back_image,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: rbp.back_button_handle(self, username),
                                  relief="flat"
                                  )
        self.back_button.place(x=40, y=180, width=151, height=50)

        # -----Reset button-----
        self.reset_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_reset.png")  
        self.reset_button = Button(image=self.reset_image,
                              borderwidth=0,
                              highlightthickness=0,
                              command=lambda: rbp.reset_button_handle(self),
                              relief="flat"
                              )
        self.reset_button.place(x=325, y=570, width=195, height=62)


        # -----Search button-----
        self.search_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_search.png")  
        self.search_button = Button(image=self.search_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: rbp.search_button_handle(self),
                                    relief="flat"
                                    )
        self.search_button.place(x=1062, y=198, width=195, height=62)
        # -----submit button-----
        self.submit_image = ImageTk.PhotoImage(file=f"./Images/BorrowReturn/button_submit.png")  
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
        self.frame_tree.place(x=576, y=270, width=681, height=411)

        self.tree = Treeview(self.frame_tree, columns=("Book_Id", "Student_Id", "Name", "Title", "Borrow_Date"), show="headings")
        self.tree.heading("Book_Id", text="Book ID")
        self.tree.heading("Student_Id", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Borrow_Date", text="Borrow Date")
        
        self.tree.column("Book_Id", width=90, anchor="center")
        self.tree.column("Student_Id", width=80, anchor="center")
        self.tree.column("Name", width=70, anchor="center")
        self.tree.column("Title", width=240, anchor="center")
        self.tree.column("Borrow_Date", width=90, anchor="center")

        self.scroll_y = Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        self.style = Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
                            background="#B9E3E9",  
                            foreground="black",  
                            rowheight=25,  
                            font=("Arial", 10))
        self.style.configure("Treeview.Heading",
                            background="#B9E3E9",  
                            foreground="black",  
                            font=("Arial", 10))

    def load_data(self):
        api = BorrowReturnManagementApi()
        results = api.load_data_api()
        self.tree.delete(*self.tree.get_children())
        for row in results:
            self.tree.insert("", "end", values=(row.get("Book_Id"), row.get("Student_Id"), row.get("Name"), row.get("Title"), row.get("Borrow_Date")))
            
    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 

        
