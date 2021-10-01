from tkinter import *

root = Tk()
root.geometry('900x600+50+50')
root.title('Home page')


mailLabel =Label(root, text='welcome', font=('arial', 50, 'bold'), bg='white', fg='black')
mailLabel.place(x=220, y=32)
root.mainloop()