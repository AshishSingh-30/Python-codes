import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
win = tk.Tk()
win.resizable(False, False)
win.title("MOBILE NUMBERS")
# message
Information = ttk.Label(win, text="ENTER YOUR INFORMATION HERE", background="lightblue")
Information.grid(row=0, columnspan=2, padx=20)
# labels
enter_name = ttk.Label(win, text="Enter Name")
enter_name.grid(row=1, column=0, padx=20, pady=20)
entry1 = ttk.Entry(win, width=16)
entry1.grid(row=1, column=1, padx=20, pady=20)
# lables
enter_number = ttk.Label(win, text="Enter Number")
enter_number.grid(row=2, column=0, padx=20, pady=20)
entry2 = ttk.Entry(win, width=16)
entry2.grid(row=2, column=1, padx=20, pady=20)
# text
text1 = tk.Text(win, height=10, width=50)
text1.grid(row=5, columnspan=4)
# message
sentence = tk.Label(win, text="View Your Information", background="lightblue")
sentence.grid(row=4, columnspan=2, padx=20, pady=20)
# function
def process():
 name = str(entry1.get())
 number = str(entry2.get())
 if len(number) == 10:
     check = open('numbers.txt', 'a')
     check1 = open('numbers.txt', 'r')
     test = check1.read()
 
 if number in test:
     messagebox.showwarning("title", "number already exists")
 
 else:
     check.write(f"{name}\t\t{number}\n")
     messagebox.showinfo("Info", "number is executed")
     
 elif number == str(number):
     messagebox.showwarning("Warning","Enter the correct Information")
     entry1.delete(0, tk.END)
     entry2.delete(0, tk.END)
 
def checking():
 check = open('numbers.txt', 'r')
 rest = check.read()
 for a in rest[::-1]:
 text1.insert(0.0, a)
def clear():
 text1.delete(0.0, tk.END)
# button
submit = ttk.Button(win, text="Insert", command=process)
submit.grid(row=3, columnspan=2)
gg
check = ttk.Button(win, text="Check", command=checking)
check.grid(row=6, column=2)
clear = ttk.Button(win, text="Clear", command=clear)
clear.grid(row=6, column=3)
win.mainloop()