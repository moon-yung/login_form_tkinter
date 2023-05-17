import tkinter as tk
import tkinter.font as font
from tkinter import *



#Initialize the main window
root = tk.Tk()
root.title("Log in Form")
root.resizable(False,False)
root.geometry("657x510+500+100")

#background of main window
bg = tk.PhotoImage(file="C:\images\mainbg.png")
Label(root,image=bg).place(x=0, y=0)

#top icon
userpic = tk.PhotoImage(file="C:\images\loginuser.png")
Label(root, image=userpic, bg='white').place(x=191, y=71)

title_login = tk.PhotoImage(file="C:\images\header_login.png")
Label(root, image=title_login, bg='white').place(x=181, y=123)

email = tk.PhotoImage(file="C:\images\email.png")
Label(root, image=email, bg='white').place(x=102, y=195)

line1 = tk.PhotoImage(file="C:\images\line.png")
Label(root, image=line1, bg='white').place(x=104, y=245)

pword = tk.PhotoImage(file="C:\images\password.png")
Label(root, image=pword, bg='white').place(x=102, y=270)

hidepass = tk.PhotoImage(file="C:\images\hidepass.png")
Label(root, image=hidepass, bg='white').place(x=298, y=288)

line2 = tk.PhotoImage(file="C:\images\line.png")
Label(root, image=line2, bg='white').place(x=102, y=318.23)

btn_login = tk.PhotoImage(file="C:\images\login.png")
Label(root, image=btn_login, bg='white').place(x=165, y=358)

not_member = tk.PhotoImage(file="C:\images\membernot.png")
Label(root, image=not_member, bg='white').place(x=140, y=401)

signup = tk.PhotoImage(file="C:\images\signmember.png")
Label(root, image=signup, bg='white').place(x=246, y=401)

forgotpass = tk.PhotoImage(file="C:\images\passforgot.png")
Label(root, image=forgotpass, bg='white').place(x=173, y=453)





root.mainloop()