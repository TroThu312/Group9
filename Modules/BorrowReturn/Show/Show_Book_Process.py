from datetime import datetime
from tkinter import *
from tkinter.ttk import Treeview, Style
import APi.Borrow_Return_Management_Api as Bma
import Modules.MainPage.Main_View_Create as mainview
from tkinter import messagebox

class Show_Book_Process:
    def __init__(self, window, entry_search):
        self.window = window
        self.entry_search = entry_search  
        self.tree = None  
        
    def show_button_handle(self):
        search = self.entry_search.get().strip()
        api = Bma.BorrowReturnManagementApi()
        books = api.show_book_api(search)
        if not self.tree:
            messagebox.showerror("Error", "Treeview not initialize.")
            return
        for item in self.tree.get_children():
            self.tree.delete(item)
        if books:
            for book in books:
                self.tree.insert("", "end", values=(
                    book["Book_Id"], book["Title"], book["Author"], book["Genre"],
                    book["Stock"]
                ))
                
    @staticmethod
    def back_button_handle(obj, username):
        obj.window.destroy()
        app = mainview.Main_View_Create(username)
        app.window.mainloop()
