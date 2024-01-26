import os, sys

cl=cw=cc=0

fname = input("Enter the file name : ")
if os.path.isfile(fname): 
    f=open(fname, 'r')
    
    for line in f:
        words=line.split()
        cl += 1
        cw += len(words)
        cc += len(line) 
    f.close()

print("\nNo of lines: ",cl, "\nNo of words: ", cw, "\nNo of characters: ", cc)