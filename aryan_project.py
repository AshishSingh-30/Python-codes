from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Billing")
window.geometry("1100x450")
window.configure(bg="light grey")


# ----Functions---

def getdata():
    number_1 = product_id_value.get()
    name = product_name_value.get()
    number_2 = selling_price_value.get()
    number_3 = quantity_value.get()

    check = open("num.txt", "a")
    check.write("\n")
    check = open("num.txt", "r")
    check2 = open("num.txt", "r")
    test = check2.read()

    count = 1
    content = check.read()
    List = content.split("\n")
    for i in List:
        if i:
            count += 1
    check = open("num.txt", "a")
    Item_no = str(count)

    if len(number_1) == 0:
        messagebox.showwarning("warning", "Enter Correct Product id")
    elif number_1 in test:
        messagebox.showwarning("title", "Numbers already existed")
    elif len(name) == 0:
        messagebox.showwarning("warning", "Enter Correct Product Name")
    elif (number_2.isnumeric() == False):
        messagebox.showwarning("warning", "Enter Correct Selling Price")
    elif (number_3.isnumeric() == False):
        messagebox.showwarning("warning", "Enter Correct Quantity")
    else:
        check.write(
            "    " + Item_no + "\t\t\t" + number_1 + "\t\t   " + name + "\t\t\t " + number_2 + "/-\t\t\t" + number_3 + "\n")

        messagebox.showinfo("title", " Data saved successfully. ")


def showing():
    product_id_entry.delete(0, END)
    product_name_entry.delete(0, END)
    selling_price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    text_1.delete(1.0, END)
    rest = open("num.txt", "r")
    for a in rest.readlines():
        text_1.insert(END, a)


# -----Labels--->Variable--->Entries--->Buttons--->Frame---

label_0 = Label(window, text="[ Inventory management ]", fg="black", bg="white", font="arial,20,bold")
label_0.place(x=30, y=25)

product_id = Label(window, text="Product id:", font="arial,15")
product_name = Label(window, text="Product name:", font="arial,15")
selling_price = Label(window, text="Selling price:", font="arial,15")
quantity = Label(window, text="Quantity:", font="arial,15")

product_id.place(x=60, y=80)
product_name.place(x=60, y=155)
selling_price.place(x=60, y=230)
quantity.place(x=60, y=305)

product_id_value = StringVar()
product_name_value = StringVar()
selling_price_value = StringVar()
quantity_value = StringVar()
product_id_entry = Entry(window, textvar=product_id_value)
product_name_entry = Entry(window, textvar=product_name_value)
selling_price_entry = Entry(window, textvar=selling_price_value)
quantity_entry = Entry(window, textvar=quantity_value)

product_id_entry.place(x=60, y=100)
product_name_entry.place(x=60, y=175)
selling_price_entry.place(x=60, y=250)
quantity_entry.place(x=60, y=325)

insert = Button(text="  Insert  ", fg="black", bg="light blue", font="arial,15,bold", command=getdata)
insert.place(x=40, y=400)

frame = Frame(bd=4, bg="light grey", width=790, height=950)
frame.place(x=260, y=25)

label_1 = Label(window, text="[ Product list ]", fg="black", bg="white", font="arial,20,bold")
label_1.place(x=260, y=25)

text_1 = Text(frame, width=260, height=30)
text_1.place(x=0, y=60)

label_2 = Label(frame, text="[    Item No.            ]", font="arial,15")
label_2.place(x=5, y=33)

label_3 = Label(frame, text="[    Product id            ]", font="arial,15")
label_3.place(x=145, y=33)

label_4 = Label(frame, text="[    Product name            ]", font="arial,15")
label_4.place(x=295, y=33)

label_5 = Label(frame, text="[    Selling price            ]", font="arial,15")
label_5.place(x=475, y=33)

label_6 = Label(frame, text="[    Quantity            ]", font="arial,15")
label_6.place(x=645, y=33)

show = Button(text="  Show  ", fg="black", bg="light blue", font="arial,15,bold", command=showing)
show.place(x=130, y=400)
window.mainloop()