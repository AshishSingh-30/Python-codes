from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os

balance = 99999
atm = Tk()
atm.geometry("700x490")
atm.title(" -/ATM MACHINE/- ")
atm.resizable(0,0)

def reg_details():
    global reg_full_name
    global reg_gender
    global reg_age
    global reg_password
    global notifi

    reg_full_name = StringVar()
    reg_gender = StringVar()
    reg_age = StringVar()
    reg_password = StringVar()

    register = Toplevel(atm)
    register.geometry('480x450')
    register.title("Registration Form")
    register.configure(bg="#008be0")

    def finish_reg():
        name = reg_full_name.get()
        gender = reg_gender.get()
        age = reg_age.get()
        password = reg_password.get()
        accounts = os.listdir()

        if name == "" or gender == "" or age == "" or password == "":
            messagebox.showerror("Error","Fill all the Details")
            return
        elif (name.isnumeric() == True) or (gender.isnumeric() == True):
            messagebox.showwarning("Warning","Fill the correct Details")
            return
        elif (age.isnumeric() == False) or (password.isnumeric() == False):
            messagebox.showwarning("Warning","Fill the correct Details")
            return
        elif len(password) !=4 :
            messagebox.showwarning("Warning","Password should be in 4 digit")
            return
        for name_check in accounts:
            if name == name_check:
                notifi.config(bg="#008be0",fg="red",text="Accounts already exists")
                return
            else:
                new_file = open(name,"w")
                new_file.write(name+"\n")
                new_file.write(gender+"\n")
                new_file.write(age+"\n")
                new_file.write(password+"\n")
                new_file.write("0")
                new_file.close()
                notifi.config(bg="#008be0",fg="green",text=" Accounts has been created ! \n Now your Pin is your Password.")



    lab_0 = Label(register, text="Registration form",width=23,height=1,font="times 20 bold")
    lab_0.place(x=70,y=53)

    lab_1 = Label(register, text="Full Name",width=20,font="times 13 bold")
    lab_1.place(x=40,y=130)

    lab_2 = Label(register, text="Gender",width=20,font="times 13 bold")
    lab_2.place(x=40,y=180)

    lab_3 = Label(register, text="Age",width=20,font="times 13 bold")
    lab_3.place(x=40,y=230)

    lab_4 = Label(register, text="Password",width=20,font="times 13 bold")
    lab_4.place(x=40,y=280)

    notifi = Label(register,text="",font="Italic 15 bold")
    notifi.place(x=100,y=390) 

    entry_1 = Entry(register,font="times 13 bold",textvar=reg_full_name)
    entry_1.place(x=260,y=130)

    entry_2 = Entry(register,font="times 13 bold",textvar=reg_gender)
    entry_2.place(x=260,y=180)

    entry_3 = Entry(register,font="times 13 bold",textvar=reg_age)
    entry_3.place(x=260,y=230)

    entry_4 = Entry(register,font="times 13 bold",textvar=reg_password)
    entry_4.place(x=260,y=280)
    entry_4.config(show="*")

    Button(register, text='Finish',width=20,bg='brown',fg='white',font="times 15 bold",command=finish_reg).place(x=130,y=330)

def window():
    global pin_value
    global name

    window = Toplevel(atm)
    window.geometry("500x400")
    window.title(" -/ATM MACHINE/- ")
    window.resizable(0,0)
    window.configure(bg="#008be0")

    def cancel():
        quit()

    def values():
        global pin_value
        accounts = os.listdir()
        pin_no = (pin_value.get())

        if len(pin_no) == 0:
            messagebox.showerror("Error","Please enter the pin")
            return
        elif len(pin_no) != 4:
            messagebox.showwarning("Warning","Your pin should in 4 Digit")
            return
        elif (pin_no.isnumeric() == False):
            messagebox.showwarning("Warning","Enter the pin in Digit.")
            return
        for name in accounts:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            if  pin_no == password:

                transcation(window)
                return       
            else:
                messagebox.showwarning("Warning","You have entered wrong pin no !")
        messagebox.showerror("Error","Acounts not founded !!")               
    def transcation(t):
        t.destroy()

        root = Tk()
        root.geometry("450x460")
        root.title(" -/ATM MACHINE/- ")
        root.configure(bg="blue")
        root.resizable(0,0)

        def Deposit():
            global acc
            global amo
            global balance

            root1 = Toplevel(atm)
            root1.geometry("450x500")
            root1.title(" -/ATM MACHINE/- ")
            root1.configure(bg="blue")
            root1.resizable(0,0)

            def dep_values(acc,amo,balance):
                account_no = acc.get()
                amount_no = amo.get()

                if len(account_no) == 0:
                    messagebox.showerror("Error","Blanked account no. not accpeted.")
                elif len(account_no) != 11:
                    messagebox.showwarning("Warning","Account no should be in 11 digit")
                elif (account_no.isnumeric() == False):
                    messagebox.showwarning("Warning","Please enter account no. in digit !")
                elif len(amount_no) == 0:
                    messagebox.showerror("Error","Blanked amount not accpeted.")    
                elif amount_no.isalpha():
                    messagebox.showwarning("Warning","Please enter amount in digit !")
                else:
                    balance = balance + int(amount_no)
                    load(amount_no,balance)                
            def load(amount_no,balance):
                load_1 = Tk()
                load_1.geometry("400x250")
                load_1.title("Transcation")
                load_1.configure(bg="black")

                def Start():
                    for i in range(11):
                        label.config(text=my['value'])
                        my['value'] += 10
                        load_1.update_idletasks()
                        time.sleep(0.5)   

                def Done():
                    messagebox.showinfo("INFO","In your acc : XXXXXXX1234 \n  Rs. has been Credited : "+str(amount_no))
                    messagebox.showinfo("INFO","Your Current Balance :"+str(balance)) 
                
                label = Label(load_1,text="")
                label.pack(pady=20)

                my_label = Label(load_1,text="Processing....",bg="black",fg="white",font="times 15 bold")
                my_label.place(x=8,y=15)

                my = ttk.Progressbar(load_1,orient=HORIZONTAL,length=300,mode='determinate')
                my.pack(pady=20)

                b = Button(load_1,text=" Start ",bg="white",fg="black",font="times 12 bold",command=Start)
                b.pack(pady=20)

                b2 = Button(load_1,text=" Done ",bg="white",fg="black",font="times 12 bold",command=Done)
                b2.pack(pady=10)
    
            lable_5 = Label(root1,text=" DEPOSIT-- ",fg="white",bg="red",font="times 22 bold",width=23,height=3)
            lable_5.place(x=30,y=10)

            account = Label(root1,text=" Enter the account no. :",fg="black",font="lucida 15 bold",width=30,height=2)
            account.place(x=30,y=150)

            amount = Label(root1,text=" Enter the amount \n  you want to deposit : ",fg="black",font="lucida 15 bold",width=30,height=2)
            amount.place(x=30,y=280)

            acc = StringVar()
            amo = StringVar()

            account_entry = Entry(root1,font="lucida 15 bold",width=18,textvar=acc)
            account_entry.place(x=30,y=210)

            amount_entry = Entry(root1,font="lucida 15 bold",width=18,textvar=amo)
            amount_entry.place(x=30,y=340)

            but_5 = Button(root1,text=" CONFIRM ",fg="white",bg="red",width=10,height=2,font="lucida 15 bold",command=lambda:(dep_values(acc,amo,balance)))
            but_5.place(x=150,y=410)

        def Balance_Enquery():
            global balance
            root3 = Toplevel(atm)
            root3.geometry("450x340")
            root3.title(" -/ATM MACHINE/- ")
            root3.configure(bg="blue")
            root3.resizable(0,0)

            def Check():
                empty_label.config(text=" Balance : Rs "+str(balance)+"/-")
                root3.after(1000)

            lable_7 = Label(root3,text=" BALANCE ENQUERY-- ",fg="white",bg="red",font="times 22 bold",width=23,height=3)
            lable_7.place(x=30,y=10)

            current = Label(root3,text=" Your current balance : ",fg="black",font="lucida 15 bold",width=22,height=1)
            current.place(x=30,y=150)

            empty_label = Label(root3,fg="red",bg="white",font="arial 15 bold")
            empty_label.place(x=30,y=190)

            but_7 = Button(root3,text=" CHECK ",fg="white",bg="red",width=8,height=2,font="lucida 15 bold",command=Check)
            but_7.place(x=170,y=250)

        def Widthdraw_cash():
            global cash
            global balance

            root4 = Toplevel(atm)
            root4.geometry("450x460")
            root4.title(" -/ATM MACHINE/- ")
            root4.configure(bg="blue")
            root4.resizable(0,0)

            def width_values(cash,balance):
                money = cash.get()
                
                if len(money) == 0:
                    messagebox.showerror("Error","Blanked amount not accpted .")
                elif len(money) > 4:
                    messagebox.showerror("Error","Not sufficent balance !")
                elif money.isalpha():
                    messagebox.showwarning("Warning","Please enter the amount in digit.")
                else:    
                    balance = balance - int(money)
                    loading(money,balance)    
            def loading(money,balance):
                load_2 = Tk()
                load_2.geometry("400x250")
                load_2.title("Transcation")
                load_2.configure(bg="black")

                def Start():
                    for i in range(11):
                        label.config(text=my['value'])
                        my['value'] += 10
                        load_2.update_idletasks()
                        time.sleep(0.5)
                def Done():
                    messagebox.showinfo("INFO","From your acc : XXXXXXX1234 \n Rs. has been Debited : "+str(money))
                    messagebox.showinfo("INFO","Your Current Balance is : "+str(balance))
                    cancel()

                label = Label(load_2,text="")
                label.pack(pady=20)

                my_label = Label(load_2,text="Processing....",bg="black",fg="white",font="times 15 bold")
                my_label.place(x=8,y=15)

                my = ttk.Progressbar(load_2,orient=HORIZONTAL,length=300,mode='determinate')
                my.pack(pady=20)

                b = Button(load_2,text=" Start ",bg="white",fg="black",font="times 12 bold",command=Start)
                b.pack(pady=20)

                b2 = Button(load_2,text=" Done ",bg="white",fg="black",font="times 12 bold",command=Done)
                b2.pack(pady=10)

            lable_8 = Label(root4,text=" WIDTHDRAW CASH-- ",fg="white",bg="red",font="times 22 bold",width=23,height=3)
            lable_8.place(x=30,y=10)
            
            width = Label(root4,text=" Enter the amount \n you want to widthdraw --",fg="black",font="lucida 15 bold",width=30,height=2)
            width.place(x=30,y=150)

            cash = StringVar()

            width_entry = Entry(root4,font="lucida 15 bold",width=18,textvar=cash)
            width_entry.place(x=30,y=230)

            but_8 = Button(root4,text=" Saving ",fg="white",bg="red",width=10,height=2,font="lucida 15 bold",command=lambda:(width_values(cash,balance)))
            but_8.place(x=50,y=290)

            but_9 = Button(root4,text=" Current ",fg="white",bg="red",width=10,height=2,font="lucida 15 bold",command=lambda:(width_values(cash,balance)))
            but_9.place(x=270,y=290)

        lable_2 = Label(root,text=" Select Your Transaction ",fg="blue",font="times 20 bold",width=23,height=3)
        lable_2.place(x=30,y=30)

        but_1 = Button(root,text=" Deposit ",fg="white",bg="red",width=14,height=2,font="lucida 15 bold",command=Deposit)
        but_1.place(x=20,y=180)

        but_2 = Button(root,text=" Balance Enquery ",fg="white",bg="red",width=14,height=2,font="lucida 15 bold",command=Balance_Enquery)
        but_2.place(x=250,y=180)

        but_3 = Button(root,text=" Widthdraw Cash ",fg="white",bg="red",width=14,height=2,font="lucida 15 bold",command=Widthdraw_cash)
        but_3.place(x=130,y=270)

        but_4 = Button(root,text=" Cancel ",fg="black",bg="light grey",width=12,height=2,font="lucida 15 bold",command=cancel)
        but_4.place(x=145,y=365)

    lable_0 = Label(window,text="  WELCOME TO SBI  ",fg="blue",font="lucida 20 bold",width=23,height=3)
    lable_0.place(x=50,y=50)

    pin = Label(window,text=" ENTER YOUR PIN :",fg="black",font="arial 15 bold",width=18,height=1)
    pin.place(x=40,y=190)

    pin_value = StringVar()

    pin_entry = Entry(window,font="arial 15 bold",width=18,textvar=pin_value)
    pin_entry.place(x=275,y=190)
    pin_entry.config(show="*")

    but_0 = Button(window,text=" OK ",fg="white",bg="red",width=10,height=2,font="arial 15 bold",command=values)
    but_0.place(x=285,y=260)

banking = PhotoImage(file="Tkinter images\\banking.png")
banking_img = Label(atm,image=banking)
banking_img.place(x=0,y=0)

reg = Button(atm,text=" Register ",fg="#dceffe",bg="#008be0",width=10,height=2,font="arial 13 bold",command=reg_details)
reg.place(x=300,y=350)

login = Button(atm,text=" Login ",fg="#dceffe",bg="#008be0",width=10,height=2,font="arial 13 bold",command=window)
login.place(x=500,y=350) 

atm.mainloop()