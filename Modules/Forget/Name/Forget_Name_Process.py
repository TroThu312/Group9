from tkinter import *
import Modules.Login.Login_Create as lc
import Modules.Forget.Code.Forget_Code_Create as fcc
from APi.Login_Api import *
from tkinter import messagebox
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Forget_Name_Process:
    verification_code = None
    admin_email_address = None

    @staticmethod
    def generate_verification_code():
    # Tao ma xac nhan ngau nhien
        characters = string.ascii_letters + string.digits
        Forget_Name_Process.verification_code = ''.join(random.choice(characters) for _ in range(6))
        return Forget_Name_Process.verification_code

    @staticmethod
    def send_button_handle(self):
        """Gửi email chứa mã xác nhận tới email của người dùng"""
        sender_email = "joohyunmm@gmail.com"  
        sender_password = "bvxi gpzq afjt zfle" 
        user_email = self.name_entry.get().strip()
        api = Login_Api()
        c = api.check_admin_email(user_email)
        if c == -1:
            messagebox.showerror("Error", "Email not found")
            return
        else:
            # Tạo mã xác nhận
            verification_code = Forget_Name_Process.generate_verification_code()
            Forget_Name_Process.admin_email_address = user_email
            # Tạo nội dung email
            subject = "Mã xác nhận"
            body = f"Mã xác nhận của bạn là: {verification_code}"

            # Tạo đối tượng email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = user_email  # Gửi đến email của người dùng
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Kết nối với server Gmail và gửi email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, user_email, msg.as_string())
                server.quit()
                print(f"Email đã được gửi tới {user_email}")
                reply = messagebox.askyesno("Notifications", "Email sent successfully. Press YES to continue.")
                if reply:
                    Forget_Name_Process.next_page(self)
                else:
                    messagebox.showerror("Notification", "Action Cancelled")
            except Exception as e:
                messagebox.showinfo("Error", "Can not sent email. Please re-enter your email.")


    @staticmethod
    def next_page(self):
        self.window.destroy()
        app = fcc.Forget_Code_Create()
        app.window.mainloop()

    @staticmethod
    def back_button_handle(obj):
        obj.window.destroy()
        app = lc.Login_Process_Create()
        app.window.mainloop()