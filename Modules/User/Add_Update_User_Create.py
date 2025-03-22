from tkinter import *  
from Modules.User.Add_Update_User_Process import Add_Update_User_Process as auup 
from datetime import datetime
from tkinter.ttk import Treeview, Style
import APi.User_Api as ua
from tkinter import messagebox 

class Add_Update_User_Create:
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
        self.window.title('Add Update User')  
        self.canvas = Canvas(self.window, bg="#ffffff", height=832, width=1280,
                             bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)  
        # --- Background image ---
        self.background_image = PhotoImage(file=f"./Images/User/background.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # ---- Button add ---
        self.add_button_image = PhotoImage(file=f"./Images/User/add_button.png")
        self.add_button = Button(image=self.add_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                 command=lambda: auup.add_button_handle(self))
        self.add_button.place(x=132.0, y=635.0, width=100.0, height=55.0)

        # ---- Button update-
        self.update_button_image = PhotoImage(file=f"./Images/User/update_button.png")
        self.update_button = Button(image=self.update_button_image, borderwidth=0, highlightthickness=0,
                                    relief="flat",command=lambda: auup.update_button_handle(self))
        self.update_button.place(x=257.0, y=635.0, width=130.0, height=55.0)

        # ---- Button reset ---
        self.reset_button_image = PhotoImage(file=f"./Images/User/reset_button.png")
        self.reset_button = Button(image=self.reset_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                   command=lambda: auup.reset_button_handle(self))
        self.reset_button.place(x=412.0, y=635.0, width=110.0, height=55.0)

        # ---- Button Back ---
        self.back_button_image = PhotoImage(file=f"./Images/User/back_button.png")
        self.back_button = Button(image=self.back_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                  command=lambda: auup.back_button_handle(self, username))
        self.back_button.place(x=40.0, y=180.0, width=151.0, height=50.0)

        # ---- Button Search ---
        self.search_button_image = PhotoImage(file=f"./Images/User/search_button.png")
        self.search_button = Button(image=self.search_button_image, borderwidth=0, highlightthickness=0, relief="flat",
                                  command=lambda: auup.search_button_handle(self))
        self.search_button.place(x=1102.0, y=225.0, width=150.0, height=62.0)

        # ---- Entry fields ----
        self.student_id_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                      font=('Arial', 20))
        self.student_id_entry.place(x=236.0, y=328.0, width=330.0, height=62.0)

        self.name_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                font=('Arial', 20))
        self.name_entry.place(x=236.0, y=400.0, width=330.0, height=62.0)

        self.contact_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20))
        self.contact_entry.place(x=236.0, y=472.0, width=330.0, height=62.0)

        self.address_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20))
        self.address_entry.place(x=236.0, y=544.0, width=330.0, height=62.0)

        self.search_entry = Entry(bd=5, bg="#F1F4F6", fg="#000716", highlightthickness=0,
                                   font=('Arial', 20))
        self.search_entry.place(x=698.0, y=225.0, width=380.0, height=62.0)


        self.name = Label(self.window, text=username, font=("Inter", 20, "bold"), bg="#9BC8FF")
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
        self.frame_tree.place(x=620, y=295, width=650, height=411)
        self.tree = Treeview(self.frame_tree, columns=("Student_Id", "Name", "Contract", "Address"), show="headings")
        self.tree.heading("Student_Id", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contract", text="Contract")
        self.tree.heading("Address", text="Address")
        self.tree.column("Student_Id", width=90, anchor="center")
        self.tree.column("Name", width=150, anchor="center")
        self.tree.column("Contract", width=150, anchor="center")
        self.tree.column("Address", width=180, anchor="center")

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
        api = ua.User_Api()
        results = api.get_user_info()
        self.tree.delete(*self.tree.get_children())
        for row in results:
            self.tree.insert("", "end", values=(row.get("Student_Id"), row.get("Name"), row.get("Contract"), row.get("Address")))
            
    def load_search_data(self, data):
        self.tree.delete(*self.tree.get_children())
        for row in data:
            self.tree.insert("", "end", values=(row.get("Student_Id"), row.get("Name"), row.get("Contract"), row.get("Address")))
    
    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 



