from tkinter import *
from tkinter import messagebox
from tkinter import font

root = Tk()
root.title("INVENTORY MANAGEMENT")
root.geometry("1000x380")
root.configure(bg="white")
frame_1=Frame(root,width=1050,height=400,bg="yellow")

def insert_but():
    txt1=text_1.get()
    txt2=text_2.get()
    txt3=text_3.get()
    txt4=text_4.get()

    txt3_check=txt3.isnumeric()
    txt4_check=txt4.isnumeric()
    check = open('Inventory_Record.txt','a')
    check1 = open('Inventory_Record.txt','r')
    test = check1.read()

    if len(txt1)==0:
        messagebox.showwarning("title","Please Enter Product ID!!")

    elif len(txt2)==0:
        messagebox.showwarning("title","Please Enter Product Name!!")

    elif txt3_check==False:
       messagebox.showerror("Error","Enter valid Selling Price!!")
       
    elif txt4_check==False:
        messagebox.showerror("Error","Enter valid Quantity!!")
   
    elif txt1 in test:
        messagebox.showwarning("title","Product ID already exist!!")      

    else:
        file=open("Inventory_Record.txt","a")
        file.write("\n")
        file=open("Inventory_Record.txt","r")
       
        counter=1
        content= file.read()
        coList=content.split("\n")
        for i in coList:
            if i:
                counter+=1
        file = open("Inventory_Record.txt","a")
        Num=str(counter)

        file.write("  ")
        file.write(Num)
        file.write(".")
        file.write("\t      ")
        file.write(txt1)
        file.write("\t\t")
        file.write(txt2)
        file.write("\t\t")
        file.write(txt3)
        file.write("\t\t")
        file.write(txt4)
        file.close()
        text_1.delete(0,END)
        text_2.delete(0,END)
        text_3.delete(0,END)
        text_4.delete(0,END)
        messagebox.showinfo("info","Entry Successful !!")
       
def clear_but():
    text_1.delete(0,END)
    text_2.delete(0,END)
    text_3.delete(0,END)
    text_4.delete(0,END)
    textA_1.delete(1.0,END)
   
def show_but():
    textA_1.delete(1.0,END)
    with open("Inventory_Record.txt","r") as f:
        textA_1.insert(INSERT,f.read())

lab_1=Label(root,text=" INVENTORY MANAGEMENT ",font=("times 12 bold"),width=25,height=3,bg="grey")
lab_1.place(x=8,y=6)
lab_2=Label(root,text=" Product ID ",font=("Albertus 10 bold"),width=16,bg="Blue")
lab_2.place(x=8,y=86)
lab_3=Label(root,text=" Product Name ",font=("Albertus 10 bold"),width=16,bg="Blue")
lab_3.place(x=8,y=151)
lab_4=Label(root,text=" Selling Price ",font=("Albertus 10 bold"),width=16,bg="Blue")
lab_4.place(x=8,y=213)
lab_5=Label(root,text=" Quantity ",font=("Albertus 10 bold"),width=16,bg="Blue")
lab_5.place(x=8,y=277)
lab_6=Label(root,text=" PRODUCT LIST ",font=("times 12 bold"),width=88,height=1,bg="grey")
lab_6.place(x=244,y=6)
lab_7=Label(root,text="  ",font=("times 19 bold"),width=53,height=1,bg="grey")
lab_7.place(x=244,y=35)
lab_8=Label(root,text=" Item No ",font=("Albertus 10 bold"),width=8,bg="grey")
lab_8.place(x=257,y=42)
lab_9=Label(root,text=" Product ID ",font=("Albertus 10 bold"),width=20,bg="grey")
lab_9.place(x=335,y=42)
lab_10=Label(root,text=" Product Name ",font=("Albertus 10 bold"),width=20,bg="grey")
lab_10.place(x=510,y=42)
lab_11=Label(root,text=" Selling Price ",font=("Albertus 10 bold"),width=20,bg="grey")
lab_11.place(x=684,y=42)
lab_12=Label(root,text=" Quantity ",font=("Albertus 10 bold"),width=20,bg="grey")
lab_12.place(x=858,y=42)

text_1=Entry(root,width=28,font="Courier 10 bold italic")
text_1.place(x=8,y=116)
text_2=Entry(root,width=28,font="Courier 10 bold italic")
text_2.place(x=8,y=179)
text_3=Entry(root,width=28,font="Courier 10 bold italic")
text_3.place(x=8,y=240)
text_4=Entry(root,width=28,font="Courier 10 bold italic")
text_4.place(x=8,y=304)

textA_1=Text(root,width=78,height=17,bg="grey",font="Courier 12 bold ")
textA_1.place(x=244,y=80)

frame_1.pack(side=LEFT)

but_1=Button(root,text="Insert",width=6,height=1,bg="red",font=("Albertus 10 bold"),command=insert_but)
but_1.place(x=19,y=355)
but_2=Button(root,text="Show",width=6,height=1,bg="red",font=("Albertus 10 bold"),command=show_but)
but_2.place(x=90,y=355)
but_3=Button(root,text="Clear",width=6,height=1,bg="red",font=("Albertus 10 bold"),command=clear_but)
but_3.place(x=162,y=355)

root.mainloop()