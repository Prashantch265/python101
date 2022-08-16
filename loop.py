thislist = ['apple', 'banana', 'orange', 'grape', 'cherry', 'mango', 'mango', 'pineapple', 'papaya']


# for in loop
print("\n for in loop \n")

for element in thislist:
    print(element)


#break
print("\n break statement \n")
# we can stop the loop before it has looped through all the items
for element in thislist:
    print(element)
    if(element == "grape"):
        break


# continue
print("\n continue statement \n")
# we can stop the current iteration of the loop, and continue with the next 
# or we can say that it skips matched condition or element
for element in thislist:
    if(element == "grape"):
        continue
    print(element)


# range()
# To loop through a set of code a specified number of times, we can use the range() function 
# or we can say it generates a numbered array of specified length
print("\n range() \n")
print(range(5))

print("\n")

for index in range(5):
    print(index)

print("\n")

for index in range(2, 6):
    print(index)

print("\n")

for i in range(len(thislist)):
  print(thislist[i])

# Else in for loop
# else block is executed when the loop stops
print("\n Else in for loop \n")

for element in thislist:
    print(element)
else:
    print("loop is finished")

print("\n")

for element in thislist:
    if(element == "mango"):
        break
    print(element)
else:
    print("loop is stopped")


# nested loop
print("\n nested for loop \n")

for i in range(3):
    for j in range(3):
        print(i, j)


# While loop
print("\n while loop \n")

i = 1
while i<=5:
    print(i)
    i+=1


# List comprehension
# List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list.
print("\n List comprehension \n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print("\n")

newlist = [x for x in range(10)]

print(newlist)