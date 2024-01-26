from tkinter import *

class STRMS:
    def __init__(self,window):
        self.window =  window
        self.window.title("Student Result Management System")
        self.window.geometry("1350x680+0+0")
        self.window.config(bg="#eeeee4")

        #========Icons==============================
        self.logo = PhotoImage(file="C:\\Users\\amar singh\\Desktop\\python\\Tkinter images\\student result logo.png")
        #==========Title==================================
        title = Label(self.window,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo,font="lucida 30 bold",bg="#154c79",fg="white",relief=GROOVE,bd=10)
        title.pack(side=TOP,fill=X)
        #==========Menu=================================
        Menu = LabelFrame(self.window,text="Menus",font="times 15 bold",bg="#eeeee4",fg="black")
        Menu.place(x=10,y=80,width=1330,height=80)

        bt1 = Button(Menu,text="Courses",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt1.place(x=20,y=4,width=200,height=40)

        bt2 = Button(Menu,text="Students",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt2.place(x=240,y=4,width=200,height=40)

        bt3 = Button(Menu,text="Result",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt3.place(x=460,y=4,width=200,height=40)

        bt4 = Button(Menu,text="View Student Result",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt4.place(x=680,y=4,width=220,height=40)

        bt5 = Button(Menu,text="Logout",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt5.place(x=920,y=4,width=190,height=40)

        bt6 = Button(Menu,text="Exit",font="goudy 15 bold",bg="#154c79",fg="white",cursor="hand2")
        bt6.place(x=1130,y=4,width=190,height=40)


        #==========content window================
        self.dashboard =  PhotoImage(file="C:\\Users\\amar singh\\Desktop\\python\\Tkinter images\\dashboardstrms.png")
        self.lbl = Label(self.window,image=self.dashboard)
        self.lbl.place(x=400,y=180,width=920,height=350)

        #============footer=====================
        footer = Label(self.window,text=" STRMS -- Student Result Management  System \n Contact us for any Technical issue: 90xxxxxx09",font="goudy 12",bg="#080d11",fg="white")
        footer.pack(side=BOTTOM,fill=X)



if __name__ == "__main__":
    window = Tk()
    obj = STRMS(window)
    window.mainloop()
