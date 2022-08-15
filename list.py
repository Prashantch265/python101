#Python Lists
# List is an array in python
# List is a collection which is ordered and changeable. Allows duplicate members.

#Ordered list
# the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

#Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Length
print(len(thislist))

# A python list can contain multiple data types
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# lists are defined as objects with the data type 'list'
print(type(thislist))

#List constructor list()
#same as array method in PHP
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Since list is an array we can access elements through index
print(thislist[2])
print(thislist[-1])     #-ve indexing counts from backward
print(thislist[:2])     #range same as above in string
print(thislist[-1:])

#change values
thislist[1] = "grape"
print(thislist)

thislist[1:2] = ["banana", "grape"]
print(thislist)

#insert() inserts an item into specified position
thislist.insert(2, "orange")
print(thislist)

#append() appends an item into list
thislist.append("mango")
print(thislist)

#extend() append elements from another list to the current list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove() remove specified item
tropical.remove("mango")
print(tropical)

#pop() remove if index is passed remove specified index else remove last index
print(thislist)
thislist.pop(2)
print(thislist)

thislist.pop()
print(thislist)

#del removes specified index
del thislist[1]
print(thislist)

#delete entire list
del thislist

#clear() method empties the list
# tropical.clear()