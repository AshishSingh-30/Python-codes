from tkinter import *
#from tkinter import messagebox
import random

global device_table,your_table,butlist
your_table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(your_table)
device_table = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(device_table)


window = Tk()
window.geometry("300x300")
window.title(" BINGO ")
window.configure(bg="light grey")
but_0 = Button(window,text="Random Board",width=17,height=2,bg="white",fg="black",font="lucida,10,bold",command=lambda:(randomboard(window)))
but_0.place(x=65,y=100)

def randomboard(t):
    global butlist,table
    t.destroy()

    root = Tk()
    root.geometry("500x250")
    root.title(" BINGO ")
    root.configure(bg="light grey")

    but_1=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_1))
    but_2=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_2))
    but_3=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_3))
    but_4=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_4))
    but_5=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_5))
    but_6=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_6))
    but_7=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_7))
    but_8=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_8))
    but_9=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_9))
    but_10=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_10))
    but_11=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_11))
    but_12=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_12))
    but_13=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_13))
    but_14=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_14))
    but_15=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_15))
    but_16=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_16))
    but_17=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_17))
    but_18=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_18))
    but_19=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_19))
    but_20=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_20))
    but_21=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_21))
    but_22=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_22))
    but_23=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_23))
    but_24=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_24))
    but_25=Button(root,text='',height=2,width=10,font="lucida,8,bold",command=lambda:game(root,but_25))
    butlist=[but_1,but_2,but_3,but_4,but_5,
             but_6,but_7,but_8,but_9,but_10,
             but_11,but_12,but_13,but_14,but_15,
             but_16,but_17,but_18,but_19,but_20,
             but_21,but_22,but_23,but_24,but_25]
    table=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    random.shuffle(table)
    for i in range(25):
        butlist[i]['text']=table[i]
    but_1.grid(row=1,column=1)
    but_2.grid(row=1,column=2)
    but_3.grid(row=1,column=3)
    but_4.grid(row=1,column=4)
    but_5.grid(row=1,column=5)
    but_6.grid(row=2,column=1)
    but_7.grid(row=2,column=2)
    but_8.grid(row=2,column=3)
    but_9.grid(row=2,column=4)
    but_10.grid(row=2,column=5)
    but_11.grid(row=3,column=1)
    but_12.grid(row=3,column=2)
    but_13.grid(row=3,column=3)
    but_14.grid(row=3,column=4)
    but_15.grid(row=3,column=5)
    but_16.grid(row=4,column=1)
    but_17.grid(row=4,column=2)
    but_18.grid(row=4,column=3)
    but_19.grid(row=4,column=4)
    but_20.grid(row=4,column=5)
    but_21.grid(row=5,column=1)
    but_22.grid(row=5,column=2)
    but_23.grid(row=5,column=3)
    but_24.grid(row=5,column=4)
    but_25.grid(row=5,column=5)
def game(t,b):
    n=b['text']
    if b['text']!='*':
        b['text']='*'
        compplay(t,n)
def compplay(t,n):
    global device_table,your_table,butlist,table
    table[table.index(int(n))]='*'
    device_table[device_table.index(int(n))]='*'
    your_table.pop(your_table.index(int(n)))
    if statement(t)== False:
        a=random.choice(your_table)
        your_table.pop(your_table.index(a))
        device_table[device_table.index(a)]='*'
        butlist[table.index(a)]['text']='*'
        table[table.index(a)]='*'
        statement(t)
def plcheck():
    global table
    s=0
    if table[0]==table[1]==table[2]==table[3]==table[4]:
        s+=1
    if table[5]==table[6]==table[7]==table[8]==table[9]:
        s+=1
    if table[10]==table[11]==table[12]==table[13]==table[14]:
        s+=1
    if table[15]==table[16]==table[17]==table[18]==table[19]:
        s+=1
    if table[20]==table[21]==table[22]==table[23]==table[24]:
        s+=1
    if table[0]==table[5]==table[10]==table[15]==table[20]:
        s+=1
    if table[1]==table[6]==table[11]==table[16]==table[21]:
        s+=1
    if table[2]==table[7]==table[12]==table[17]==table[22]:
        s+=1
    if table[3]==table[8]==table[13]==table[18]==table[23]:
        s+=1
    if table[4]==table[9]==table[14]==table[19]==table[24]:
        s+=1
    if table[0]==table[6]==table[12]==table[18]==table[24]:
        s+=1
    if table[4]==table[8]==table[12]==table[16]==table[20]:
        s+=1
    if s>=5:
        return True
    else:
        return False
def compcheck():
    global device_table
    s=0
    if device_table[0]==device_table[1]==device_table[2]==device_table[3]==device_table[4]:
        s+=1
    if device_table[5]==device_table[6]==device_table[7]==device_table[8]==device_table[9]:
        s+=1
    if device_table[10]==device_table[11]==device_table[12]==device_table[13]==device_table[14]:
        s+=1
    if device_table[15]==device_table[16]==device_table[17]==device_table[18]==device_table[19]:
        s+=1
    if device_table[20]==device_table[21]==device_table[22]==device_table[23]==device_table[24]:
        s+=1
    if device_table[0]==device_table[5]==device_table[10]==device_table[15]==device_table[20]:
        s+=1
    if device_table[1]==device_table[6]==device_table[11]==device_table[16]==device_table[21]:
        s+=1
    if device_table[2]==device_table[7]==device_table[12]==device_table[17]==device_table[22]:
        s+=1
    if device_table[3]==device_table[8]==device_table[13]==device_table[18]==device_table[23]:
        s+=1
    if device_table[4]==device_table[9]==device_table[14]==device_table[19]==device_table[24]:
        s+=1
    if device_table[0]==device_table[6]==device_table[12]==device_table[18]==device_table[24]:
        s+=1
    if device_table[4]==device_table[8]==device_table[12]==device_table[16]==device_table[20]:
        s+=1
    if s>=5:
        return True
    else:
        return False
def statement(t):

    if plcheck()==True and compcheck()==True:
        t.destroy()
        tk=Tk()
        tk.title(" Bingo ")
        tk.configure(bg="light grey")
        tk.geometry("300x300")
        Label(tk,text='[ Draw ]',font="arial,15,bold",fg="red").pack()
        print("\n")
        Label(tk,fg="black",text=compboard()).pack()
        Label(tk,fg="black",text=plboard()).pack()
    elif plcheck()==True and compcheck()==False:
        t.destroy() 
        tk=Tk()
        tk.title(" Bingo ")
        tk.configure(bg="light grey")
        tk.geometry("300x300")
        Label(tk,text='[ win ]',font="arial,15,bold",fg="red").pack()
        print("\n")
        Label(tk,fg="black",text=compboard()).pack()
        Label(tk,fg="black",text=plboard()).pack()
    elif plcheck()==False and compcheck()==True:
        t.destroy()
        tk=Tk()
        tk.title(" Bingo ")
        tk.configure(bg="light grey")
        tk.geometry("300x300")
        Label(tk,text='[ Lose ]',font="arial,15,bold",fg="red").pack()
        print("\n")
        Label(tk,fg="black",text=compboard()).pack()
        Label(tk,fg="black",text=plboard()).pack()
    else:
        return False
def compboard():
    global device_table
    x=0
    s='''com board
'''
    for i in range(5):
        s+='/ '
        for j in range(5):
            s+=str(device_table[x])+' / '
            x+=1
        s+='\n'
    return s
def plboard():
    global table
    x=0
    s='''player board
'''
    for i in range(5):
        s+='/ '
        for j in range(5):
            s+=str(table[x])+' / '
            x+=1
        s+='\n'
    return s  


window.mainloop()