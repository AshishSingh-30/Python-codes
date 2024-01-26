import time
start=time.time()
def insertionSort(arr):

	for i in range(1, n):
	    key = arr[i]
		j = i-1
		while j >=0 and key < arr[j]:
			arr[j+1] = arr[j]			
            j -= 1
		arr[j+1] = key

arr = []
r=25
n=2500
for i in range(0,n):
	r=((r*7621)+1)%32768	
    arr.append(r)

insertionSort(arr)
print ("Your sorted array is: ")
for i in range(len(arr)):	
    print ("%d" %arr[i])
end=time.time()
print(f"Runtime of program {end-start}")  #micro sec or 10^-6 sec
