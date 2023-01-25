##Class Notes##

#Loops - each time a loop runs a loop, it is known as an iteration

#For Loop
#EX: for loopVariable in sequence: 
#       'Do something with loopvariable'
#EX: languages = ["C", "C++", "Python", "Delphi"]
#print(languages[0])
#print(languages[1])
#print(languages[2])
#print(languages[3])

#->

languages = ["C", "C++", "Python", "Delphi"]
for language in languages:
    print(language)

#While Loop - similar to a for loop, however only runs until a certain condition is met
#EX: while booleanExpression:
    #Do something
magicNumber = "16"
UserInput = input("Guess The Magic Number:")

while UserInput != magicNumber:
    UserInput = input("Guess The Magic Number:")

#Adding a counter
#counter = 0 
#while counter < 5 :
#    counter += 1


##Functions## - != methods

def say_hello():
    print("Hello There")
say_hello() #Calls function 

#Return
def basic_addition():
    return 1 + 2
result = basic_addition()
print(result)
#print(basic_addition()) -> another way to print result

#Define the function to allow it to accept variables, variables passed into a function are known as parameters. Once values are passed through a function, they are considered arguments
#Arguments are used to do whatever is inside the function
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

def basic_addition(firstNum, secondNum): #Arguments
    return firstNum + secondNum

result = basic_addition(num1, num2) #Parameters

print(result) #num1 and num2 are parameters that we passed, however we rename them in the function. Outside of function, variables are still num1 and num2. firstnum will error out

#Defualt Parameters and Ignored Defaults
def portuguese_speaking_countries(country = "Brazil"):
    print(country + " is a portuguese speaking country")
print(portuguese_speaking_countries())  # prints "Brazil"
print(portuguese_speaking_countries("Angola"))  # prints "Angola"

def add(x,y):
    return x + y
x = 1
y = 2
print(add(x,y))
#Scope - Determining and delegating variables for global scope or local scope is critical

##Fibonacci Sequence##

def print_vertically(a, b, c, n):
    count = 3
    print(a)
    print(b)
    while count <= n:
        print(c)
        a = b
        b = c
        c = (a + b)
        count += 1

a = 1
b = 1
c = (a+b)
n = int(input("Choose a nth number in the sequence: "))
print_vertically(a, b, c, n)

#alt

def print_horizontally(a, b, c, n):
    count = 3
    fib_seq = []
    fib_seq.append(a)
    fib_seq.append(b)

    while count <= n:
        fib_seq.append(c)
        a = b
        b = c
        c = (a + b)
        count += 1

    print(fib_seq)

#breaks - can be used to breakout of the innermost loop such as a for or while loop. Whenever a break is encountered, python will go back up a level
z = [1, 2, 2, 4, 3, 5]
total = 0
for num in z: 
    if num == 3:
        break
    else:
        total += num

print(total)

#continue - prevenets a loop from executing, but only stops the current iteration of the loop
x = [1, 2, 3, 4, 5]
total = 0
for num in x:
    if num == 3:
        continue
    else:
        total += num

print(total)

#pass - does nothing, used when you need to have code syntactically but do not want to provide any
class Truck:
    def __init__(self):
        pass #remove the 'pass' and add real code to our __init__() whenever we want
