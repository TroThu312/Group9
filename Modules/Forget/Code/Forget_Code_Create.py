from tkinter import *
import Modules.Forget.Code.Forget_Code_Process as fcp
from tkinter import messagebox 

class Forget_Code_Create:

    def __init__(self):
        self.window = Tk()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 1280
        self.window_height = 832
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))
        self.window.configure(bg="#FFFFFF")
        self.window.title("Forget Password")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        # Background Image
        self.background_image = PhotoImage(file=f"./Images/Forget/background_code.png")
        self.canvas.create_image(640.0, 416.0, image=self.background_image)

        # Button send
        self.next_button_image = PhotoImage(file=f"./Images/Forget/next_button.png")
        self.next_button = Button(
            image=self.next_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: fcp.Forget_Code_Process.submit_button_handle(self),
            relief="flat"
        )
        self.next_button.place(x=709.0, y=609.0, width=140.0, height=50.0)

        # Button back
        self.back_button_image = PhotoImage(file=f"./Images/Forget/back_button.png")
        self.back_button = Button(
            image=self.back_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: fcp.Forget_Code_Process.back_button_handle(self) ,
            relief="flat"
        )
        self.back_button.place(x=365.0, y=192.0, width=82.0, height=67.0)

        # Entry - code
        self.code_entry = Entry(
            bd=5,
            bg="#F1F4F6",
            fg="#000716",
            highlightthickness=0,
            font=('Arial', 20))
        self.code_entry.place(x=483.0, y=513.0, width=366.0, height=50.0)

        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()
    def on_close(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to exit?"):
            self.window.destroy()  
        else:
            return 



