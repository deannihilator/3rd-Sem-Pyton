#WAP to perform List Operation
list=[1,2,3]    #created List..
print("Initial List")
print(list)
list.append(4)
list.append(5)
print("List after addition of 2 elements:")
print(list)
#Addition of elements into the List..
list.insert(2,7)
list.insert(3,9)
print("List after performing addition operation")
print(list)
#Removing elements from the list..
list.remove(1)
list.remove(2)
print("List after removing elements")
print(list)
#Print Element of a range using slice operation..
slice_list=list[2:4]
print("\n Slicing element in a range 2-4:")
print(slice_list)
#Addition of a list to a list using append() method..
list2=[8,10]
list.append(list2)
print("\n List after addition of a List:")
print(list)