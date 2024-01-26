from tkinter import*
from tkinter import messagebox

#-----------------------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("1350x315")
window.title("Product Details")
window.configure(bg = "lightgrey")

#---------------------------------------------------FUNCTIONS-----------------------------------------------------------

def insert():
    product_id = entry1.get()
    name = entry2.get()
    selling_price = entry3.get()
    quantity = entry4.get()
   
    check1 = product_id.isnumeric()
    check2 = name.isnumeric()
    check3 = selling_price.isnumeric()
    check4 = quantity.isnumeric()

    if(check1 == False):
       pop2()
       entry1.delete(0,END)
    elif(check2 == True):
       pop3()
       entry2.delete(0,END)
    elif(check3 == False):
       pop4()
       entry3.delete(0,END)
    elif(check4 == False):
       pop5()
       entry4.delete(0,END)
    else:
       save_file()
       pop1()

def save_file():
   
    product_id = entry1.get()
    name = entry2.get()
    selling_price = entry3.get()
    quantity = entry4.get()
    file=open("Details.txt","a")
    file.write("\n")
    file=open("Details.txt","r")
    counter=1
    content= file.read()
    coList=content.split("\n")
    for i in coList:
        if i:
            counter+=1
    file = open("Details.txt","a")
    cou_t=str(counter)
   
    file.write(cou_t)
    file.write("\t\t\t\t")
    file.write(product_id)
    file.write("\t\t\t  ")
    file.write(name)
    file.write("\t\t\t      ")
    file.write(selling_price)
    file.write("\t\t\t\t  ")
    file.write(quantity)

def show():
    clear1()
    with open("Details.txt","r") as f:
        text1.insert(INSERT,f.read())

def clear1():
    text1.delete(1.0, END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

def clear2():
    text1.delete(1.0,END)

def pop1():
    messagebox.showinfo("Information", "Insertion successful")

def pop2():
    messagebox.showwarning("Warning", "Invalid id, Characters not allowed")

def pop3():
    messagebox.showwarning("Warning", "Invalid Name, Numbers not allowed")

def pop4():
    messagebox.showwarning("Warning", "Invalid Price, characters not allowed")

def pop5():
    messagebox.showwarning("Warning", "Invalid Quantity, characters not allowed")

#---------------------------------------------------LABELS--------------------------------------------------------------

label0 = Label(width=28, height=19, bg="lightgrey", relief="groove")
label0.place(x = 15,y=22)

label1 = Label(text="Inventory management", fg="black", bg="lightgrey",font=("arial",12))
label1.place(x=25,y=10)

label2 = Label(text="product id:", fg="black",  bg="lightgrey",font=("arial",12))
label2.place(x=25,y=40)

label3 = Label(text = "product name:", fg="black",  bg="lightgrey", font=("arial",12))
label3.place(x=25,y=95)

label4 = Label(text = "Selling price:", fg = "black", bg="lightgrey", font = ("arial",12))
label4.place(x=25,y=150)

label4 = Label(text = "Quantity:", fg = "black", bg="lightgrey", font = ("arial",12))
label4.place(x=25,y=205)

label5 = Label(width=161, height=19, bg="lightgrey", relief="groove")
label5.place(x = 215,y=22)

label6 = Label(text="Product List", fg="black", bg="lightgrey", font=("arial",12))
label6.place(x=220,y=10)

text1 = Text(bg ="white",width=140, height=13, relief="flat")
text1.place(x=220,y=53)

label7 = Label(text=" item no",width=28, height=1, fg="black", bg="lightgrey",relief="groove",anchor='w', font=("arial",12))
label7.place(x=220,y=30)

label8 = Label(text="Product id",width=23, height=1, fg="black", bg="lightgrey",anchor='w' ,relief="groove", font=("arial",12))
label8.place(x=475,y=30)

label9 = Label(text="Name",width=25, height=1, fg="black", bg="lightgrey",relief="groove",anchor='w', font=("arial",12))
label9.place(x=679,y=30)

label10 = Label(text="Selling Price",width=25, height=1, fg="black", bg="lightgrey",anchor='w', relief="groove", font=("arial",12))
label10.place(x=907,y=30)

label11 = Label(text="Quantity",width=23, height=1, fg="black", bg="lightgrey",anchor='w', relief="groove", font=("arial",12))
label11.place(x=1128,y=30)

#---------------------------------------------------BUTTONS-------------------------------------------------------------

button1 = Button(text = "Insert",width = 8,fg = "black", bg = "lightblue", font=("arial",12), command=insert)
button1.place(x=25, y=270)

button2 = Button(text = "Show",width = 8,fg = "black", bg = "lightblue", font=("arial",12), command=show)
button2.place(x=110, y=270)

button3 = Button(text = "Clear",width = 8,fg = "black", bg = "lightblue", font=("arial",11,"bold"), command=clear2, relief="ridge")
button3.place(x=1250, y=270)

#---------------------------------------------------ENTRY-BOX-----------------------------------------------------------

entry1 = Entry(width = 25)
entry1.place(x=25, y=70)

entry2 = Entry(width = 25)
entry2.place(x=25, y=125)

entry3 = Entry(width = 25)
entry3.place(x=25, y=180)

entry4 = Entry(width = 25)
entry4.place(x=25, y=235)

#-----------------------------------------------------------------------------------------------------------------------
window.mainloop()