from tkinter import *
from tkinter import Text
from tkinter import messagebox



window = Tk()

window.title('inetrship')
window.geometry('500x500')
label = Label(window, text='DETAILS OF PERSON',fg='black', font=('arial', 12, 'bold')).pack(side='top', fill=X)


def add():
    x = name.get()
    y = phone.get()


    if len(y) == 10:
        file = open('geek.txt', 'a')
        file1 = open('geek.txt', 'r')
        test = file1.read()

        if y in test:
            messagebox.showwarning('title', 'number already exists')
        else:
            
            file.write(x + "--->" + y + "\n")
            print('\n')
            
            messagebox.showinfo('info', 'Data Saved Successfully')
    else:
        messagebox.showwarning('warning', 'enter the correct information')
    

def cleartext():
    display_text.delete('1.0', 'end')


def check():
    display_text.delete('1.0', END)
    data_file = open("geek.txt", "r")
    for val in data_file.readlines():
        display_text.insert(END, val + "\n")


def exit_btn():
    window.destroy()

name = StringVar()
phone = StringVar()

#INPUT FRAME

frame = Frame(width=400, height=450, bd=4, bg='white').place(x=60, y=60)

Label(window, text='ENTER INFORMATION HERE',fg='black',bg='green', font=('arial', 12, 'bold')).place(x=60, y=25)

name_label = Label(frame, text='NAME', fg='black', font=('arial', 12, 'bold'))
name_label.place(x=75, y=95)

name_entry = Entry(frame, textvar=name, bd=4)
name_entry.place(x=155, y=98)

phone_no_label = Label(frame, text='Mob No', fg='black', font=('arial', 12, 'bold'))
phone_no_label.place(x=75, y=142)

phone_no_entry = Entry(frame, textvar=phone, bd=4)
phone_no_entry.place(x=155, y=145)

button = Button(text='submit', command=add, activebackground='red', activeforeground='green').place(x=210, y=185)


#OUTPUT FRAME


display_frame = Frame(bd=4, width=500, height=450).place(x=30, y=245)

Label(window, text='VIEW INFORMATION HERE',fg='black', bg='green', font=('arial', 12, 'bold')).place(x=50, y=250)

display_text = Text(display_frame, width=50, height=20)
display_text.place(x=60, y=280)

clear_button = Button(text='Clear', bd=4, command=cleartext)
clear_button.place(x=350, y=620)

check_button = Button(text='check', bd=4, command=check)
check_button.place(x=300, y=620)

exit_button = Button(text='EXIT', bd=4,bg='red', command=exit_btn)
exit_button.place(x=200, y=620)


window.mainloop()