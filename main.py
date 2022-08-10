from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1000x600+150+50")
        self.root.resizable(False, False)

#         background Image
        self.bg= PhotoImage(file="C:/Users/Wanjohi/Desktop/images/dssss.png")
        self.bg_image= Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=250, y=100, width=500, height=400)

        title=Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"),fg="#6162FF",bg="white" ).place(x=60, y=20)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"),fg="#1d1d1d", bg="white").place(x=60, y=90)

        #username
        user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15),bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        #password

        paswrd = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #button
        forget= Button (Frame_login,text="forgot password?",cursor="hand2",bd=0, font=("Goudy old style", 12 ),fg="#6162FF", bg="white").place(x=90, y=280)
        forget = Button(Frame_login ,command=self.check_function ,cursor="hand2", text="Login?", bd=0, font=("Goudy old style", 15), bg="#6162FF",fg="white").place(x=90, y=320, width=180, height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get()=="":
            messagebox.showerror("Error", "All fiels are required", parent=self.root)
        elif self.username.get()!= "miriam" or self.password.get()!="7468":
            messagebox.showerror("Error", "Invalid Username or Password" ,parent=self.root)
        else:
            messagebox.showinfo("welcome", f"welcome {self.username.get()}")



root = Tk()
obj = Login(root)
root.mainloop()