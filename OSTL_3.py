all_list=[]
even_list=[]
odd_list=[]
print("Enter elements in list: ")
for i in range (0,15):
    no=int(input())
    if no%2==0:
        even_list.append(no)
    else:
        odd_list.append(no)
    all_list.append(no)
print("Your list: ",all_list)
even_list.sort()
odd_list.sort()
all_list.sort()
print("Minimum no: ",all_list[0])
print("Maximum no: ",all_list[14])
print("Your sorted list: ",all_list)
print("Even number sorted list: ",even_list)
print("Odd number sorted list: ",odd_list)
check=int(input("Enter a number: "))
a=all_list.count(check)
if a>= 1:
    if check%2==0:
        print("Your number exist in even list")
    else:
        print("Your number exist in odd list")
else:
    print("Your number does not exist in any list!!")
