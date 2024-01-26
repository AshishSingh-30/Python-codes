print("Enter 15 numbers:")
b = []
for i in range (15):
    a = int(input())
    b.append(a)
#print(b)
b.sort()
print("Sorted list:")
print(b)
evenlist = [] 
oddlist = [] 
for i in b: 
  if (i % 2 == 0): 
     evenlist.append(i) 
  else: 
     oddlist.append(i) 
print("Even lists:", evenlist) 
print("Odd lists:", oddlist)