import os, sys

fname= input("Enter File Name : ")
if os.path.isfile(fname):
    f=open(fname,"r")
    print("Before:")
    str_ing=f.read()

    print(str_ing)
    f=open(fname,"a")
    text=input("Enter your text : ")
    f.write(text)

    f=open(fname,"r")
    str_ing=f.read()
    print("After:")
    print(str_ing)

    f.close()
