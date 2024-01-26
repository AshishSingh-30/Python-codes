from tkinter import *
from tkinter import Text
from tkinter import messagebox

window = Tk()

window.title('MOBILE NUMBER')
window.geometry('525x700')


#FUNCTIONS
def process():
    x = name.get()
    y = phone.get()


    if len(y) == 10:
        file = open('number.txt', 'a')
        file1 = open('number.txt', 'r')
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
    display_text.delete("1.0", "end")


def check():
    display_text.delete('1.0', END)
    data_file = open("number.txt", "r")
    for val in data_file.readlines():
        display_text.insert(END, val + "\n")


name = StringVar()
phone = StringVar()

#INPUT FRAME

frame =Frame(width=400, height=450, bd=4, bg='white').place(x=60, y=60)

#MESSAGE
Label(window, text='ENTER INFORMATION HERE',fg='black',bg='grey', font=('calibri', 12, 'bold')).place(x=160, y=25)

#LABELS
name_label = Label(frame, text='NAME', fg='black', font=('calibri', 12, 'bold'))
name_label.place(x=95, y=95)

name_entry = Entry(frame, textvar=name, bd=4)
name_entry.place(x=200, y=98)

phone_no_label = Label(frame, text='PHONE NO', fg='black', font=('calibri', 12, 'bold'))
phone_no_label.place(x=85, y=142)

phone_no_entry = Entry(frame, textvar=phone, bd=4)
phone_no_entry.place(x=200, y=145)

#BUTTON
button = Button(text='INSERT', command=process, activebackground='red', activeforeground='green' ,bd = 8, width = 10).place(x=210, y=185)


#OUTPUT FRAME


display_frame = Frame(bd=4, width=500, height=450).place(x=30, y=245)

Label(window, text='VIEW INFORMATION HERE',fg='black', bg='grey', font=('arial', 12, 'bold')).place(x=160, y=250)

#TEXT 
display_text = Text(display_frame, width=50, height=20)
display_text.place(x=60, y=280)

#BUTTONS
clear_button = Button(text='CLEAR', width=10 ,bd=8, command=cleartext)
clear_button.place(x=150, y=620)

check_button = Button(text='CHECK',width=10, bd=8, command=check)
check_button.place(x=300, y=620)

window.mainloop()