from tkinter import *
from tkinter import Text
from tkinter import messagebox

window=Tk()

window.title('internship')
window.geometry('500x500')
label=Label(window,text='DETAILS OF INDIVIDUAL',fg='black',font=('arial',12,'bold')).pack(side='top',fill=X)

def add():
    x=name.get()
    y=phone.get()

    if len(y)==10:
        file=open('no.txt','a')
        file1=open('no.txt','r')
        test=file1.read()

        if y in test:
            messagebox.showwarning('title','number already exists')
        else:
            file.write(x+"--->"+y+"\n")
            print('\n')

            messagebox.showinfo('info','data saved succesfully')
    else:
        messagebox.showwarning('warning','enter the correct information')

def cleartext():
    display_text.delete("1.0","end")

def check():
    display_text.delete('1.0',END)
    data_file=open("no.txt","r")
    for val in data_file.readlines():
        display_text.insert(END,val+"\n")

def exit_btn():
    window.destroy()

name=StringVar()
phone=StringVar()

#INPUT FRAME

frame=Frame(width=400,height=300,bd=5,bg='white').place(x=60,y=60)
Label(window,text='ENTER INFORMATION HERE',fg='black',bg='blue',font=('arial',12,'bold')).place(x=60,y=25)

name_label=Label(frame,text='NAME',fg='black',font=('arial',12,'bold'))
name_label.place(x=75,y=95)

name_entry=Entry(frame,textvar=name,bd=4)
name_entry.place(x=250,y=95)

phone_no_label=Label(frame,text='Mob No.',fg='black',font=('arial',12,'bold'))
phone_no_label.place(x=75,y=140)

phone_no_entry=Entry(frame,textvar=phone,bd=4)
phone_no_entry.place(x=250,y=145)

button=Button(text='submit',command=add,activebackground='red',activeforeground='green').place(x=210,y=300)

#OUTPUT FRAME



Label(window,text='VIEW INFORMATION HERE',fg='black',bg='blue',font=('arial',12,'bold')).place(x=500,y=25)

display_text=Text(width=50,height=20)
display_text.place(x=500,y=50)

clear_button=Button(text='Clear',bd=4,command=cleartext)
clear_button.place(x=500,y=375)

check_button=Button(text='Check',bd=4,command=check)
check_button.place(x=550,y=375)

exit_button=Button(text='Exit',bd=4,command=exit_btn)
exit_button.place(x=700, y=375)

window.mainloop()