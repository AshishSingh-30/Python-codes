from tkinter import *
from tkinter import Text
from tkinter import messagebox

root = Tk()
root.geometry("500x500")

def getvalues():
    words = namevalue.get()
    number = phonevalue.get()
    
    if len(number) == 10 and number.isnumeric():
        check = open('numbers.txt','a')
        check1 = open('numbers.txt','r')
        test = check1.read()

        if number in test:
            messagebox.showwarning("title","Numbers already exists")
        else:
            check.write(words + " = " + number + "\n")
            print("\n")

            messagebox.showinfo("info","Data accepted")
    else:
        messagebox.showwarning("warning","Enter the correct information")
    
def checking():
    text_1.delete('1.0', END)
    rest = open("numbers.txt","r")
    for a in rest.readlines():
       text_1.insert(END, a + "\n")

def clear():
    text_1.delete("1.0","end")



label1 = Label(root,text="ENTER YOUR INFORMATION HERE",fg="black",bg="light blue",font="arial,12,bold")
label1.grid(row=0,column=3)

name=Label(root,text="ENTER NAME")
name.grid(row=1,column=2)

phone=Label(root,text="PHONE NUMBER")
phone.grid(row=2,column=2)

namevalue=StringVar()
phonevalue=StringVar()

nameentry=Entry(root,textvar=namevalue)
nameentry.grid(row=1,column=3)

phoneentry=Entry(root,textvar=phonevalue)
phoneentry.grid(row=2,column=3)

insert = Button(text="Insert",command=getvalues)
insert.grid(row=6,column=3)

frame = Frame(bd=4,width=500,height=450)
frame.place(x=30,y=245)

label2=Label(root,text="VIEW INFORMATION HERE",fg="black",bg="red",font="arial,12,bold")
label2.grid(row=7,column=3)

text_1 = Text(frame,width=40,height=10)
text_1.grid(row=8,column=3)

Check_button = Button(text="Check",bd=4,command=checking)
Check_button.grid(row=9,column=3)

clear_button = Button(text="Clear",bd=4,command=clear)
clear_button.grid(row=9,column=4)

root.mainloop()