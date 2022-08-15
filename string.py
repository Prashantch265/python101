#Python String
#String are arrays same as in JS
#Single quote and Double quote both are same as in JS

#Multiline String in python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#we can use single quote instead of double quote
print(a)

#Check whether a certain phrase or character is in string or not
txt = "The best things in life are free!"
print("free" in txt)

print("free" not in txt)

#Slicing 
#same as php return range of characters from specific position
print(txt[2:7])
print(txt[:7])
print(txt[2:])

#Uppercase
print(txt.upper())

#Lowercase
print(txt.lower())

#Remove whitespace
#In other programming language we got trim method but in python we have strip()
txt = "       Tsttta stet    teterere    "
print(txt.strip())

#Replace String
txt = "Hello I'm Prashant"
print(txt.replace("Prashant", "Ashim"))

#Split
#It splits a string into array of strings same as php explode
txt = "Hello, World"
print(txt.split(","))

#format()
#We cannot combine string and numbers by concatination
# print("My age is " + 21)          #Uncomment it and run you will see an error

#that's why we have format() that takes an argument place where the placeholders {} are and construct a string
txt = "My age is {}"
print(txt.format(21))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
