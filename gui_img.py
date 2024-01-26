import tkinter as tk
from tkinter import *
from tkinter import filedialog
# from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import os

# my_win = tk.Tk()
# my_win.geometry("500x500")
# my_win.title("Lisence Number Plate Detection")
# my_font1=('times', 18, 'bold')
# l1 = tk.Label(my_win, text='Upload Files dispaly',width=40).grid(row=1,column=1,columnspan=4)
# b1 = tk.Button(my_win, text='Upload image',width=20, command=lambda:upload_file()).grid(row=1,column=1,columnspan=4)

# def upload_file():
#     f_types = [('PNG files','*.png'), ('Jpg files','*.jpg')]
#     filename = tk.filedialog.askopenfilename(filetypes=f_types)
#     img = Image.open(filename)
#     img = img.resize((100,100))
#     img = ImageTk.PhotoImage(img)
#     e1 = tk.Label(my_win).grid(row=3,column=1).image=img
#     e1['image'] = img

# my_win.mainloop()

def showImage():
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(('PNG files','*.png'), ('JPG files','*.jpg'), ('All Files','*')))
    img = Image.open(file)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


root = Tk()

frm  = Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="EXIT", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

root.title("Lisence Number Plate Detection")
root.geometry("500x500")
root.mainloop()

