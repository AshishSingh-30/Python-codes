from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("500x550")
window.title("[ GAME ]")
window.configure(bg="indigo")


def pop():
    file = messagebox.askyesno("WARNING","Please enter the no. (1-3)")
    if file == True:
        messagebox.showinfo("INFO"," Press ok .")
    else:
        messagebox.showinfo("INFO","Pahli fursat mein nikal.")
        window.quit()


def gaming1():
    number_choice = int(user_input_value.get())

    record = open("history.txt","a")
    #record.write("\n")
    record = open("history.txt","r")   
    
    if number_choice == 1:
        number_input_choice = "Rock"
    elif number_choice == 2:
        number_input_choice = "Paper"
    else:
        number_input_choice = "Scissor"
    if number_choice > 3 or number_choice < 1:
        pop()
    else:
        device_choice = random.randint(1,3)

        while number_choice == device_choice:
            device_choice = random.randint(1,3)
    
        if device_choice == 1:
            device_input_choice = "Rock"
        elif device_choice == 2:
            device_input_choice = "Paper"
        else:
            device_input_choice = "Scissor"

        if ((number_choice == 1 and device_choice == 2) or (number_choice == 2 and device_choice == 1)):
            messagebox.showinfo("info","Paper wins in this situation")
            result = "Paper"
        elif ((number_choice == 2 and device_choice == 3) or (number_choice == 3 and device_choice == 2)):
            messagebox.showinfo("info","Scissor wins in this situation")
            result = "Scissor"
        else:
            messagebox.showinfo("info","Rock wins in this situation")
            result = "Rock"

        if number_input_choice == result:
            messagebox.showinfo("info","You Win")
        else:
            messagebox.showinfo("info","Device Win")
        record1 = open("history.txt","a")
        record1.write("number choice : " +str(number_choice) +"-"+ number_input_choice +"   "+" device choice : "+ str(device_choice) +"-"+ device_input_choice +"\n")
        print("\n")


def showing():
    user_input_entry.delete(0,END)
    text_1.delete(1.0,END)
    rest = open("history.txt","r")
    for a in rest.readlines():
        text_1.insert(END, a)


def clearing():
    text_1.delete(1.0,END)

  

label_0 = Label(window,text="1=ROCK  / 2=PAPER  / 3=SCISSOR",bg="white",font="arial,20,bold",width=30,height=2)
label_0.place(x=120,y=0)

user_input = Label(window,text="Enter the number :",bg="white",font="arial,15,bold")
user_input.place(x=30,y=70)

user_input_value = IntVar()

user_input_entry = Entry(window,font="20",textvar=user_input_value)
user_input_entry.place(x=180,y=70)

ok = Button(text=" OK ",bg="RED",font="arial,15,bold",command=gaming1)
ok.place(x=200,y=130)

show = Button(text=" Show ",bg="Light blue",font="arial,15,bold",command=showing)
show.place(x=30,y=190)

clear = Button(text=" Clear ",bg="Light blue",font="arial,15,bold",command=clearing)
clear.place(x=410,y=190)

frame = Frame(bd=4,width=440,height=310)
frame.place(x=30,y=230)

text_1 = Text(frame,width=53,height=19)
text_1.place(x=0,y=0)

window.mainloop()