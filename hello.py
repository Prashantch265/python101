#print is used as function in v3 unlike a statement in v2
#print "Hello World"
print("Hello World")


# scope in python
if(5>2):
    print("It is true")

#scope begins with colun unlike braces in other programming language
#space count should be same for all line inside a block


#there's no keyword in variable decaration we can declare variable as follows
a = 5
b = "a"
print(a)
print(b)


#It just replaces the previous value
a = "a"
print(a)


#Type Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#type() can be used to get the data type of a varible 
print(type(x))
print(type(y))


#assign multiple values to multiple variables
var1, var2, var3 = "string", 1, 5.5
print(var1, var2, var3)


#Unpacking a collection (Destructuring in JS)
fruits = ["Banana", "Apple", "Grape"]
f1, f2, f3 = fruits
print(f1)


#Global Variable

#Global Variables are varaibles declared outside of a function. It can be used inside and outside of a function
def myFun():
    print(f3)

myFun()
#Here we use f3 inside myFun but it is declared outside of myFun so it is a global variable

#We can create a global variable inside a function with the help of global keyword
def createGlobalVar():
    global globalVar
    globalVar = "This is inside a local scope"
    print(globalVar)

createGlobalVar()

globalVar = "Thi is outside a local scope"

print(globalVar)


#Boolean type
x = True
if(x):
    print(type(x))
# unlike other programming language boolean value are True and False in python where in other programming language it's true and false

#bool() evaluate any given value and return true or false
#false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Python Numbers
#Python provides us an additional number type called Complex 
#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Python Operators
#We got additional operators like
#Identity Operators
# x is y      #returns true if two objects are same
# x is not y      #returns false if two objects are same

#Membership Operators
# x in y      #returns true if a phrase or character is in string
# x not in y      #returns false if a phrase or ccharacter is in string