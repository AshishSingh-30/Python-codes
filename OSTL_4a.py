from array import*
def mergeSort(main_arr):
    if len(main_arr) > 1:
        mid = len(main_arr) // 2
        left_arr = main_arr[:mid]
        right_arr = main_arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
              main_arr[k] = left_arr[i]
              i += 1
            else:
                main_arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            main_arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            main_arr[k]=right_arr[j]
            j += 1
            k += 1
main_arr=array("i",[])
n=int(input("How many numbers you want to enter:   "))
for i in range(0,n):
    main_arr.append(int(input("Enter the element: ")))
mergeSort(main_arr)
print("Your sorted array in ascending order: ")
for i in range(0,n):
    print(main_arr[i])
print("Your sorted array in descending order: ")
for i in range(n-1,-1,-1):
    print(main_arr[i])
