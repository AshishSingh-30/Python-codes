for i in range(0,7):
    if i==0:
        print(" *** ")
    elif i==3:
        print("*****")
    else:
        print("*   *")
for i in range(0,7):
    for j in range(0,5):
        if (i==2 or i==4):
            if (j==1 or j==3) :
                print("*",end=" ")
            else:
                print(" ",end=" ") 
        elif (i==3):
            if (j==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if(j==0 or j==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print("\n")
num=5
for i in range(0,7):
    for j in range(0,7):
        if (i==0 or i==6):
            print("*",end=" ")
        else:
            if j==num:
                print("*",end=" ")
                num-=1
            else:
                print(" ",end=" ")
    print("\n")
