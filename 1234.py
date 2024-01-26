from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os

window = Tk()
window.geometry("500x400")
window.title(" -/ATM MACHINE/- ")
window.resizable(0,0)

def finish_reg():
    name = reg_name.get()
    age = reg_age.get()
    gender = reg_gender.get()
    password = reg_password.get()
    accounts = ("action.txt")

    if name == " " or age == " " or gender == " " or password == " ":
        messagebox.showerror("Error","please fill all details")
    '''elif name.isnumeric() and gender.isnumeric():
        messagebox.showwarning("Warning","Please filll details correctly")
    elif (age.isnumeric() == False) and (password.isnumeric() == False):
        messagebox.showwarning("Warning","Please filll details correctly")
    elif password <= str(8):
        messagebox.showwarning("Warning","Maximum Password till 8 digit only")
    '''
    for name_check in accounts:
        if name == name_check:
            messagebox.showerror("Error","Accounts already created!")
            return

        else:
            new_file = open(name,"w")
            new_file.write(name+"\n")
            new_file.write(age+"\n")
            new_file.write(gender+"\n")
            new_file.write(password+"\n")
            new_file.write("0")
            new_file.close()
            messagebox.showinfo("INFO","Account has been created")





def register():
    global reg_name,reg_age,reg_gender,reg_password

    reg_name = StringVar()
    reg_age = StringVar()
    reg_gender = StringVar()
    reg_password = StringVar()

    register = Toplevel(window)
    register.geometry("500x450")
    register.title(" Register ")
    register.configure(bg="blue")
    register.resizable(0,0)

    label_0 = Label(register,text="( ENTER THE DETAILS TO REGISTER ACCOUNT )",fg="black",font="lucida 15 bold",width=40,height=3)
    label_0.place(x=10,y=10)

    label_1 = Label(register,text="Enter the name  ",fg="black",bg="light grey",font="lucida 15 bold",width=18,height=1)
    label_1.place(x=20,y=130)

    label_2 = Label(register,text="Enter the age  ",fg="black",bg="light grey",font="lucida 15 bold",width=18,height=1)
    label_2.place(x=20,y=180)

    label_3 = Label(register,text="Enter the gender  ",fg="black",bg="light grey",font="lucida 15 bold",width=18,height=1)
    label_3.place(x=20,y=240)

    label_4 = Label(register,text="Enter the password  ",fg="black",bg="light grey",font="lucida 15 bold",width=18,height=1)
    label_4.place(x=20,y=290)

    name_entry = Entry(register,textvar=reg_name,font="arial 15 bold")
    name_entry.place(x=260,y=130)

    age_entry = Entry(register,textvar=reg_age,font="arial 15 bold")
    age_entry.place(x=260,y=180)

    gender_entry = Entry(register,textvar=reg_gender,font="arial 15 bold")
    gender_entry.place(x=260,y=240)

    password_entry = Entry(register,textvar=reg_password,font="arial 15 bold")
    password_entry.place(x=260,y=290)

    reg_but = Button(register,text=" Done ",fg="white",bg="red",width=10,height=2,font="arial 15 bold",command=finish_reg)
    reg_but.place(x=190,y=340)




bg = PhotoImage(file="Tkinter images\\bg.png")

bg_img = Label(window,image=bg)
bg_img.place(x=0,y=0)

#label_0 = Label(window,text="  WELCOME TO SBI  ",fg="blue",font="lucida 20 bold",width=23,height=3)
#label_0.place(x=50,y=50)

img2 = PhotoImage(file="Tkinter images\\WTS.png")

bg_img1 = Label(window,image=img2)
bg_img1.place(x=70,y=60)

but_0 = Button(window,text=" Register ",fg="white",bg="red",width=10,height=2,font="arial 15 bold",command=register)
but_0.place(x=200,y=150)

but_1 = Button(window,text=" Login ",fg="white",bg="red",width=10,height=2,font="arial 15 bold")#,command=login)
but_1.place(x=200,y=230)

window.mainloop()