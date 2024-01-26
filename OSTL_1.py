num_0 = input("Enter a number x: ")
num_1 = input("Enter a number y: ")

print("numbers before swapping x: "+num_0+" & y: "+num_1)
num_0,num_1 = num_1,num_0
print("numbers after swapping x: "+num_0+" & y: "+num_1)

if int(num_0) >= 0:
    if int (num_0) == 0:
        print(" x = "+ num_0 +" is Zero")
    else :
        print(" x = "+ num_0 +" is Positive number")
else :
    print(" x = "+ num_0 +" is Negative number")

if int(num_1) >= 0:
    if int (num_1) == 0:
        print(" y = "+ num_1 +" is Zero")
    else :
        print(" y = "+ num_1 +" is Positive number")
else :
    print(" y = "+ num_1 +" is Negative number")

