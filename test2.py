from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("My Dummy Window")
def insert():
 my_name = first_name.get()
 print("Your name is ",my_name)


label = Label(window,text="Enter Your Name",fg="red",bg="blue",font=("arial",17,"bold"))
label.place(x=20,y=80)
first_name = StringVar()
name = Entry(window,textvar=first_name)
name.place(x=240,y=90)
button = Button(window,text="Login",width=12,bg="red",fg="white",command=insert)
button.place(x=150,y=180)
window.mainloop()