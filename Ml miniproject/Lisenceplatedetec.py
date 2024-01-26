import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
# import easyocr

def showImage():
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(('PNG files','*.png'), ('JPG files','*.jpg'), ('All Files','*')))
    # img1 = Image.open(file)
    # img.thumbnail((500,350))
    # img = ImageTk.PhotoImage(img)
    img2 = cv2.imread("C:\Users\Admin\Desktop\Ashish\Python\ANPRwithPython-main\image4.jpg")
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))       
    lbl.configure(image=gray)
    lbl.image = gray


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
root.geometry("600x600")
root.mainloop()