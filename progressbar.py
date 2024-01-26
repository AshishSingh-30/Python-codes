from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry("400x250")
root.title("Transcation")
root.configure(bg="black")

def start():
    for i in range(11):
        label.config(text=my['value'])
        my['value'] += 10
        root.update_idletasks()
        time.sleep(0.8)

def back():
    quit()

label = Label(root,text="")
label.pack(pady=20)

my_label = Label(root,text="Processing....",bg="black",fg="white",font="times 15 bold")
my_label.place(x=8,y=15)

my = ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
my.pack(pady=20)

b = Button(root,text="start",command=start)
b.pack(pady=20)

b2 = Button(root,text="Done",command=back)
b2.pack(pady=20)

root.mainloop()