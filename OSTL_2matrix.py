import numpy as np 
# creating first matrix
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line (separated by space): ") 
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
# For printing the matrix
A = np.array(entries).reshape(R1, C1)
print("The first matrix is:",A)
# creating second matrix
R2 = int(input("Enter the number of rows:"))
C2 = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line (separated by space): ")  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))  
# For printing the matrix
B = np.array(entries).reshape(R2, C2)
print("The first matrix is:",B)
# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))
#subtracting two matrix
print("Subtraction of two matrix")
