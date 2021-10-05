from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
#import Frontend.Dashboard

class login_system:
    def __init__(self, project):
        self.project = project
        self.project.geometry("1900x1500+0+0")


        login_system_frame = Frame(self.project, bg="white")
        login_system_frame.place(x=120, y=100, height=500, width=600)

        Title=Label(login_system_frame,text="Login Here",bg="white",fg='#4d0000',font=("Impact",35,"bold",))
        Title.place(x=210,y=30)

        self.username_image = ImageTk.PhotoImage(Image.open("C:/Users/DELL/PycharmProjects/pythonProject26/image/user1.png"))
        back_ground_label = Label(login_system_frame, bg='white',image=self.username_image)
        back_ground_label.place(x=188,y=194)
        self.u_entry = StringVar()
        self.username_entry = Entry(login_system_frame, bd=0, textvar=self.u_entry,relief=FLAT, width=19, bg='white', font=("Courier New", 14))
        self.username_entry.place(x=218, y=194)
        username = Label(login_system_frame, text="Username", bd=0,fg='Black', bg='white',font=("Arial bold", 14))
        username.place(x=190, y=150)

        username_seperator=ttk.Separator(login_system_frame,orient='horizontal')
        username_seperator.place(x=190,y=220,width=240)
#>>>>>>>>>>>>>>>>>>>>>password<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

        password = Label(login_system_frame, text="Password", bd=0, fg='Black', bg='white', font=("Arial bold", 14))
        password.place(x=190, y=240)

        password_seperator = ttk.Separator(login_system_frame, orient='horizontal')
        password_seperator.place(x=190, y=309, width=240)
        self.p_entry = StringVar()
        self.password_entry = Entry(login_system_frame, bd=0, show="*",textvar=self.p_entry, width=19, bg='white',font=("Courier New", 14))
        self.password_entry.place(x=218, y=283)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<BUTTON<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
        self.login_image = ImageTk.PhotoImage( Image.open("C:/Users/DELL/PycharmProjects/pythonProject26/image/login.png"))
        self.button2 = Button(login_system_frame, text="Log in",command=self.login, relief=FLAT,image=self.login_image, width=150, height=23, bg="pink", fg="blue")
        self.button2.place(x=221, y=330)

    def login(self):
        if self.username_entry.get()=="Legends" and self.password_entry.get()=="issss":
            messagebox.showinfo("Info",f" Welcome {self.username_entry.get()} and your password is: {self.password_entry.get()}")
            self.project.destroy()
            self.new=Tk()


        else:
            messagebox.showerror("Error","Invalid username or password")






if _name__=="__main_":
    tk=Tk()
    obj=login_system(tk)
    tk.mainloop()