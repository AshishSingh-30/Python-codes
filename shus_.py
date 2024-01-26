from tkinter import *
from tkinter import Text
from tkinter import messagebox

root = Tk()

root.title("PRODUCT DETAILS")
root.geometry("1500x1500")

final_label = Label(text="INFORMATION OF PRODUCT", bg='green', font=('arial', 15, 'bold'))
final_label.pack(side='top', fill=X)



def insert():
    a = id.get()
    b = name1.get()
    c = price.get()
    d = quantity.get()
    
    

    file = open("hello.txt","a")
    file = open("hello.txt","r")
    file1 = open("hello.txt","r")
    test = file1.read()

    num = 1
    content= file.read()
    List=content.split("\n")
    for i in List:
        if i:
            num +=1
    file  = open("hello.txt","a")
    Item_no=str(num)


    if(a.isdigit() == False):
        messagebox.showwarning("warning","wrong")
    elif a in test:
        messagebox.showwarning("title","numbers already saved")
    elif(b.isalpha() == False):
        messagebox.showwarning("warning","name")
    elif(c.isdigit() == False):
        messagebox.showwarning("warning","selling")
    elif(d.isdigit() == False):
        messagebox.showwarning("warning","quantity")
    else:
        
        file.write(Item_no+"\t\t\t" +a+"\t\t   "+b+"\t\t\t "+c+"/-\t\t\t"+d+"\n")
        messagebox.showinfo("success","Data Saved successully")
        
        
       
def show():
    output_text.delete('1.0', END)
    res = open("hello.txt","r")
    for i in res.readlines():
        output_text.insert(END,i)
    

#input frame

name1 = StringVar()
id = StringVar()
quantity = StringVar()
price = StringVar()
result = StringVar()

input_frame = Frame(width=250, height=480, bg='pink')
input_frame.place(x=10, y=90)

input_label = Label(text = 'INVENTORY MANAGEMENT', font=('new times roman', 10, 'bold'))
input_label.place(x=50, y=55)

#Labels

pro_id = Label(input_frame, text='product ID :')
pro_id.place(x=20, y=40)

pro_name = Label(input_frame, text='Product Name')
pro_name.place(x=20, y=128)

selling_price = Label(input_frame, text='Selling Price : ')
selling_price.place(x=20, y=220)

Quantity = Label(input_frame, text='Quantity')
Quantity.place(x=20, y=312)

#text

pro_id = Entry(input_frame, textvar=id)
pro_id.place(x=20, y=67)

pro_name = Entry(input_frame, textvar=name1)
pro_name.place(x=20, y=156)

pro_price = Entry(input_frame, textvar=price)
pro_price.place(x=20, y=248)

pro_Quantity = Entry(input_frame, textvar=quantity)
pro_Quantity.place(x=20, y=341)

insert_button = Button(input_frame, text='INSERT', bg='green', command=insert)
insert_button.place(x=60, y=405)

show_button = Button(input_frame, text='SHOW', bg='green', command=show)
show_button.place(x=120, y=405)


#output frame

result_label = Label(text='PRODUCT LIST', font=('new times roman', 10, 'bold'))
result_label.place(x=280, y=55)

result_frame = Frame(width=1000, height=480, bg='white')
result_frame.place(x=280, y=90)

head_frame = Frame(width=1000, height=30, bg='purple')
head_frame.place(x=280, y=90)

text_frame = Frame(width=1000, height=450, bg='yellow')
text_frame.place(x=280,y=120)

item_no = Label(head_frame, text='Item no', font=('new times roman', 10, 'bold'), bg='red')
item_no.place(x=10, y=5)

product_id = Label(head_frame, text='Product Id', font=('new times roman', 10, 'bold'), bg='red')
product_id.place(x=220, y=5)

name = Label(head_frame, text='Name', font=('new times roman', 10, 'bold'), bg='red')
name.place(x=450, y=5)

selling_price = Label(head_frame, text='Selling Price', font=('new times roman', 10, 'bold'), bg='red')
selling_price.place(x=650, y=5)

Quantity = Label(head_frame, text='Quantity', font=('new times roman', 10, 'bold'), bg='red')
Quantity.place(x=900, y=5)

output_text = Text(text_frame, width=1000, height=450)
output_text.place(x=0, y=0)

root.mainloop()