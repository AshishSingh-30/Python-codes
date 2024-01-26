from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font="times 40 bold",bg="yellow")
        title.pack(side=TOP,fill=X)

#=========All Variables===============

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


#=============manage frame==============

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=90,width=450,height=600)

        manage_title=Label(manage_frame,text="Manage Student",font="times 30 bold",bg="crimson",fg="white")
        manage_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(manage_frame,text="Roll No.",font="times 20 bold",bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(manage_frame,textvar=self.Roll_No_var,font="times 16 bold",bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(manage_frame,text="Name",font="times 20 bold",bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(manage_frame,textvar=self.name_var,font="times 16 bold",bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(manage_frame,text="Email",font="times 20 bold",bg="crimson",fg="white")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(manage_frame,textvar=self.email_var,font="times 16 bold",bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(manage_frame,text="Gender",font="times 20 bold",bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvar=self.gender_var,font="times 15 bold",state="readonly")
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact=Label(manage_frame,text="Contact",font="times 20 bold",bg="crimson",fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(manage_frame,textvar=self.contact_var,font="times 16 bold",bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(manage_frame,text="D.O.B",font="times 20 bold",bg="crimson",fg="white")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(manage_frame,textvar=self.dob_var,font="times 16 bold",bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(manage_frame,text="Address",font="times 20 bold",bg="crimson",fg="white")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(manage_frame,width=22,height=3,font="times 15 bold",bd=5,relief=GROOVE)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#===========button frame============

        button_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="crimson")
        button_frame.place(x=10,y=535,width=420)

        but1=Button(button_frame,text="Add",width=10,command=self.add_students)
        but1.grid(row=0,column=0,padx=10,pady=10)

        but2=Button(button_frame,text="Update",width=10,command=self.update_data)
        but2.grid(row=0,column=1,padx=10,pady=10)

        but3=Button(button_frame,text="Delete",width=10,command=self.delete_data)
        but3.grid(row=0,column=2,padx=10,pady=10)

        but4=Button(button_frame,text="Clear",width=10,command=self.clear)
        but4.grid(row=0,column=3,padx=10,pady=10)

#=============deatil frame=============

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=90,width=830,height=600)

        lbl_search=Label(detail_frame,text="Search by",font="times 20 bold",bg="crimson",fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvar=self.search_by,width=12,font="times 15 bold",state="readonly")
        combo_search["values"]=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(detail_frame,textvar=self.search_txt,width=17,font="times 14 bold",bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

#=========button frame================

        search=Button(detail_frame,text="Search",width=15,pady=5,command=self.search_data)
        search.grid(row=0,column=3,padx=5,pady=10)

        show=Button(detail_frame,text="Show All",width=15,pady=5,command=self.fetch_data)
        show.grid(row=0,column=4,padx=5,pady=10)

#=========Table frame========================

        Table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="crimson")
        Table_frame.place(x=10,y=70,width=800,height=500)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.student_table.pack()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get("1.0",END)=="":
            messagebox.showerror("Error","All fields are required !!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get("1.0",END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Info","Record has been inserted.")
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents["values"]
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                            self.name_var.get(),
                                                                                                            self.email_var.get(),
                                                                                                            self.gender_var.get(),
                                                                                                            self.contact_var.get(),
                                                                                                            self.dob_var.get(),
                                                                                                            self.txt_address.get("1.0",END),
                                                                                                            self.Roll_No_var.get()
                                                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)
                con.commit()
        con.close()

    
root = Tk()
obj=student(root)
root.mainloop()