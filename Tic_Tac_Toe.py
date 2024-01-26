# Two player game.....

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("410x420")
window.title("Tic Tac Toe")

def callback(r,c):
    global player

    if player == "X" and check[r][c] == 0 and stop_game == False:
        zero[r][c].configure(text="X",fg="blue",bg="white")
        check[r][c] ="X"
        player = "O"
    if player == "O" and check[r][c] == 0 and stop_game == False:
        zero[r][c].configure(text="O",fg="red",bg="black")
        check[r][c] ="O"
        player = "X"
    winner()

def winner():
    global stop_game

    for i in range(3):
        if check[i][0] == check[i][1] == check[i][2]!=0:
            zero[i][0].configure(bg="grey")
            zero[i][1].configure(bg="grey")
            zero[i][2].configure(bg="grey")
            stop_game = True
            end()
        
    for i in range(3):
        if check[0][i] == check[1][i] == check[2][i]!=0:
            zero[0][i].configure(bg="grey")
            zero[1][i].configure(bg="grey")
            zero[2][i].configure(bg="grey")
            end()
        
    
    for i in range(3):
        if check[0][0] == check[1][1] == check[2][2]!=0:
            zero[0][0].configure(bg="grey")
            zero[1][1].configure(bg="grey")
            zero[2][2].configure(bg="grey")
            stop_game = True
            end()
        

    for i in range(3):    
        if check[2][0] == check[1][1] == check[0][2]!=0:
            zero[2][0].configure(bg="grey")
            zero[1][1].configure(bg="grey")
            zero[0][2].configure(bg="grey") 
            stop_game = True
            end()
    
def end():
    messagebox.showinfo("info","Thank You")
    window.quit()


zero = [[0,0,0],
        [0,0,0],
        [0,0,0,]]

check = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(3):
    for j in range(3):
        zero[i][j] = Button(font="arial,70,bold",width=14,height=7,bg="light blue",command = lambda r=i,c=j: callback(r,c))
        zero[i][j].grid(row=i,column=j)
file = messagebox.askyesno("Info","Do u want  [X]")
if file == True:
    player = "X"
else:
    player = "O"
 
stop_game = False

window.mainloop()