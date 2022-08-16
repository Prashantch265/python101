# Sort() will sort list alphanumerically asc by default

#Alphabetical sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("\n")

#Numerical Sorting
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print("\n")

# Sort desc
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print("\n")

# costumize sort function
# sort(key = function) 

# sort list based on how close the number is to 50
def myFun(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 32, 23]
thislist.sort(key = myFun)
print(thislist)

print("\n")

# case insensitive sorting
# by default sort() is case sensitive for case insensitive we can pass string functions to key
thislist = ["banana", "Orange", "Kiwi", "cherry", "Pineapple"]
thislist.sort(key = str.lower)
print(thislist)

print("\n")

# Reverse the list
thislist.reverse()
print(thislist)