##Class Notes##

#Data Types

#Boolean - yes = true, no = false
#Numbers - can be whole, fractions, decimal, or complex
#Strings - any sequence of characters
#byes and byte arrays - could be binary representation of a file
#lists - ordered sequences of other data types, detoned by square brackets
#tuples - sequence of immutable python objects, cannot remove values, start at an index of 0, are denoted by paranthesis
#dictionary - collections of key-value pairs

#Variable Reassignment
name = "Dylan Pouncy"
print(name)
name = "Dylan S Pouncy"
print(name)

#Abbreviated Assignment
count = 0
count += 1 
print(count) #Yields the response '1'

#Operators
count = 99
count -= 5
print(count) #Yeilds 94

count = 1
count*= 8
print(count) #Yeilds 8

count = 81
count /=9
print(count) #Yeilds 9 

#Are the two values equal?
x = 1
y = 2
print(x == y) #Yields False

#Are the two values not equal?
x = 1
y = 2
print(x!=y) #Yields True

#Modulus - Operator used to get the remainder from the division of two numbers
count = 9
count %= 4
print(count) #Yeilds 1

#Greater than, less than, and equals
x = 1 
y = 2
print( x > y) #Yields False
print( x <= y) #Yields True

#Logical Operators
x = 1
y = 2
print(x > y and x == y) #False since both expressions are false
print(x < y and x != y) #True since both expressions are true

x = 1
y = 2
print(x > y or x == y) #False since both expressions are false
print(x < y or x != y) #True since both expressions are true
print(x > y or x != y) #True since one expressions is ture

#Not - returns the opposite of a resolved expression
x = 1
y = 2
print(not(x != y)) #False, (x != y) resolves to tre, then we flip it to false
print(not(x > y)) #True, (X>Y) resolves to false, then we flip it to true

#cast - shorthand way of converting a data type returned by the input method and turning it into another data type
i = 5
print(int(i)) #converts I to an integer

#Conditionals
#IF
i = 5
k = input("Please Provide a Number: ")

if int(k) < i: 
    print("The Number You Have Provided Is Less Than Our Value.")

#IF with ELSE
i = 5
k = input("Please Provide a Number: ")

if int(k) < i: 
    print("The Number You Have Provided Is Less Than Our Value.")
else: 
    if int(k) < 10:
        print("The number you have provided is greater than our value but less than 10.")
    else:
        print("The number you have provided is greater than our value and greater than or equal to 10.")

#Chained Conditionals - used to eliminate massively long IF/ELSE conditional statements - Evaluates first code block then progresses if false
month = int(input("Please input a numeric month (1 - 12): ")) #Cast our input into a numeric so we can compare it

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("You didn't enter a valid number")
