# ========================================================{Problems on array}====================================================

# 1) Find the smallest no. & the largest no. in the array------------------------------------------------------------

# mylist = [100, 34, 79, 2, 327, 99, 200]

# Method 1:---------------{ Using sorting method }
# mylist.sort()
# print("No. of list is: ", mylist)
# print("Smallest no. is: ", mylist[0])
# print("Largest no. is: ", mylist[-1])

# Method 2:--------------{ Using min-max method }
# print("No. of list is: ", mylist)
# print("Smallest no. is: ", min(mylist))
# print("Largest no. is: ", max(mylist))


# 2) Second smallest & Second largest element in the array------------------------------------------------------------

# mylist = [60, 11, 4, 80, 78, 90]

# Method 1:---------------{ Using sorting method }
# mylist.sort()
# print("No. of list is: ", mylist)
# print("Second smallest no. is: ", mylist[1])
# print("Second largest no. is: ", mylist[-2])

# Method 2:--------------{ Using set & min-max method }
# print("No. of list is: ", mylist)

# newlist = set(mylist)
# newlist.remove(min(newlist))
# newlist.remove(max(newlist))

# print("New no. list is: ",newlist)
# print("Second smallest no. is: ", min(newlist))
# print("Second largest no. is: ", max(newlist))


# 3) Reverse a given array-------------------------------------------------------------------------------------------

# mylist = [10, 11, 12, 13, 14, 15]

# Method 1:------------{ Using Reverse method }
# print("MyList before reverse: ", mylist)
# mylist.reverse()
# print("MyList after reverse: ", mylist)