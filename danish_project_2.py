from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("PRODUCT DETAILS")
window.geometry("1100x550")
window.configure(bg="light grey")


#  MAINFUNCTIONS

def Get_data():
    
    identity = PRODUCT_ID.get()
    name = PRODUCT_NAME.get()
    price = SELLING_PRICE.get()
    Qty = QUANTITY.get()

    file1 = open("details.txt","a")
    file1.write("\n")
    file1 = open("details.txt","r")
    file2 = open("details.txt","r")
    test = file2.read()

    number = 1
    content= file1.read()
    List=content.split("\n")
    for i in List:
        if i:
            number +=1
    file1  = open("details.txt","a")
    Item_no=str(number)

    
    if len(identity) == 0:
        messagebox.showwarning("warning","Enter Correct Product id")
    elif identity in test:
        messagebox.showwarning("title","Numbers already available")
    elif len(name) == 0:
        messagebox.showwarning("warning","Enter Correct Product Name")
    elif (price.isnumeric() == False):
        messagebox.showwarning("warning","Enter Correct Selling Price")
    elif (Qty.isnumeric() == False):
        messagebox.showwarning("warning","Enter Correct Quantity")
    else:
        file1.write("    "+ Item_no + "\t\t\t" + identity +"\t\t   "+ name +"\t\t\t "+ price +"/-\t\t\t"+ Qty +"\n")
        
        messagebox.showinfo("title"," Data saved successfully. ")
    
def showing():
    PRODUCT_ID_entry.delete(0,END)
    PRODUCT_NAME_entry.delete(0,END)
    SELLING_PRICE_entry.delete(0,END)
    QUANTITY_entry.delete(0,END)
    text_1.delete(1.0, END)
    rest = open("details.txt","r")
    for a in rest.readlines():
        text_1.insert(END, a )


def clear():
        text_1.delete(1.0, END)


#Labels

label_0 = Label(window,text="INVENTORY MANAGEMENT ",relief="groove",fg="black",bg="light grey",font="calibri,20,bold")
label_0.place(x=45,y=30)

label_1 = Label(window,text="  Product list ",fg="black",bg="light grey",font="calibri,20,bold")
label_1.place(x=260,y=25)

product_id = Label(window,text="    Product id:       ",relief="sunken",anchor='n',bg ="light grey",font="calibri,15")
product_id.place(x=60,y=80)

product_name = Label(window,text="  Product name:  ",relief="sunken",anchor='n',bg ="light grey",font="calibri,15")
product_name.place(x=60,y=155)

selling_price = Label(window,text="   Selling price:    ",relief="sunken",anchor='n',bg ="light grey",font="calibri,15")
selling_price.place(x=60,y=230)

quantity = Label(window,text="      Quantity:        ",relief="sunken",anchor='n',bg ="light grey",font="calibri,15")
quantity.place(x=60,y=305) 

# VARIABLES
PRODUCT_ID = StringVar()
PRODUCT_NAME = StringVar()
SELLING_PRICE = StringVar()
QUANTITY = StringVar()

# ENTRY
PRODUCT_ID_entry = Entry(window,textvar=PRODUCT_ID)
PRODUCT_ID_entry.place(x=60,y=105)

PRODUCT_NAME_entry = Entry(window,textvar=PRODUCT_NAME)
PRODUCT_NAME_entry.place(x=60,y=180)

SELLING_PRICE_entry = Entry(window,textvar=SELLING_PRICE)
SELLING_PRICE_entry.place(x=60,y=255)

QUANTITY_entry = Entry(window,textvar=QUANTITY)
QUANTITY_entry.place(x=60,y=330)


frame = Frame(bd=4,bg="light grey",width=790,height=950)
frame.place(x=260,y=25)

# LABELS
label_1 = Label(window,text="  PRODUCT LIST ",relief="groove",width="86",fg="black",bg="light grey",font="calibri,20,bold")
label_1.place(x=270,y=30)

text_1 = Text(frame,width=260,height=25)
text_1.place(x=0,y=60)

label_2 = Label(frame,text="      Item No               ",relief="groove",anchor='n',bg ="light grey",font="calibri,15")
label_2.place(x=5,y=33)

label_3 = Label(frame,text="      Product id             ",relief="groove",anchor='n',bg ="light grey",font="calibri,15")
label_3.place(x=145,y=33)

label_4 = Label(frame,text="     Product name               ",relief="groove",anchor='n',bg ="light grey",font="calibri,15")
label_4.place(x=295,y=33)

label_5 = Label(frame,text="       Selling price              ",relief="groove",anchor='n',bg ="light grey",font="calibri,15")
label_5.place(x=475,y=33)

label_6 = Label(frame,text="      Quantity              ",relief="groove",anchor='n',bg ="light grey",font="calibri,15")
label_6.place(x=645,y=33)



# BUTTONS
insert = Button(text="  Insert  ",fg="black",bg="light blue",font="calibri,15,bold",command=Get_data)
insert.place(x=40,y=400)

Show = Button(text="  Show  ",fg="black",bg="light blue",font="calibri,15,bold",command=showing)
Show.place(x=130,y=400)

clear = Button(text="   clear  ", width= 16,fg="black",bg="light blue",font="calibri,15,bold",command= clear)
clear.place(x=42,y=450)


window.mainloop()