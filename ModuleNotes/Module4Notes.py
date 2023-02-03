##Iteration##

#Iterable object - any object we can loop through with a for loop
#__iter__() - method within a for loop, inside of __iter__() we setup our object w/ any setup we may need to loop through
#return self - how we make sure to return our object

#EX1:
class TriangularNums: #Class Creation
    # Calculate triangular numbers with x = t(t+1)/2
    def __init__(self, n): #takes on two arguments, the nth number in the sequence, used to terminate the iteration
        self.n = n #n is an instance variable

    def __iter__(self): #sets up object before we start the iteration
        self.t = 1 #created an instance variable, t, to track how many times we've iterated through
        return self

    def __next__(self): #defines our threshold and the conditional that can stop our iteration
        if self.t > n: #check that t doesnt exceed n, if so we raise the 'StopIteration' "error" and stop iterating
            raise StopIteration

        x = self.t * (self.t + 1) / 2 #generate our triangular number using t
        self.t += 1 #increment t by one to prevent an infinite loop

        return int(x) #return our triangular number x
                               
n = int(input("Enter the nth term: ")) #Input from user is cast as n
for x in TriangularNums(n): #we put our iterator calss after the in
    print(x)

#List Comprehensions - quick way to create lists from other lists, usually w/ some sort of math applied, appear to be for loops ramped up
#EX: used for transforming a list in a way and storing the resulting numbers in a sepearate list
#EX1:
numbers = [1,2,3,4,5,6]
raisedNums = [x ** 3 for x in numbers] #List Comprehension
print(raisedNums)
#Alternatively, we can use a conditional if statement to direct our list comprehension to only even numbers in this case
numbers = [1,2,3,4,5]
raisednums = [x ** 3 for x in numbers if x % 2 == 0]
print(raisednums)

##################################################################################################################################################

##Containers## - main workers of python, data types that contain several values

#Lists - variables that contain several other values between square brackets (array data type), lists can have multiple types of data types
#Lists - can contain duplicats and maintain order (order you put things in is the order you get things in iteration)
#Append() method adds elements to our lists
#EX1:
mylist = []
mylist.append(5)
mylist.append(.057)
mylist.append("Hello")
mylist.append(542525)
print(mylist)
print(mylist[3]) #prints 542525
mylist[2] #Equal to "Hello"

#count() - counts the number of times a certain value is contained within a list
#value() - checks to see if a certain value is within a list, will return a boolean value indicating if the value is found
#index() - return the index of the first instance of a value
#EX2:
myList = []
myList.append('a')
myList.append('b')
myList.append('c')
myList.append('d')
myList.append('a')
myList.append('1')
myList.append('2')
myList.append('3')
myList.append('4')

numOfa = myList.count('a') # Returns a value of 2
isEinList = 'e' in myList # Returns False as e is not in the list
isBinList = 'b' in myList # Returns True as b is in the list
indexOfA = myList.index('a') # Returns 0 as 0 is the first index with a
indexOfOne = myList.index('1') # Returns 5 as 1 is in index 5

#Tuples - variables that look like list, but use paranthesis and unlike lists are immutable and once they have been set, you cannot add or remove values (no append())
#You can only count the number of intances or index values, but are faster to traverse than lists and can be locked to make code more stable
#EX1:
myTuple = ('a', 'b', 'c', 'a') 
tuples = myTuple.count('a') # Returns a value of 2
indexOfB = myTuple.index('b') # Returns a value of 1

#Dictionaries - data type used to store information in a key-value manner (address bok in which names retrieve an address or value). 
#Use curly brackets to define, square brackets to retrieve. Do not maintain order, cannot contain duplicate keys, and do not care what data type elements are
#EX1: 
languages = {
    'Canada' : 'French',
    'United States' : 'English',
    'Mexico' : 'Spanish',
    'Brazil' : 'Portuguese'
}
languages['Haiti'] = 'French'
suriname = 'Suriname'
languages[suriname] = 'Dutch'
# Can also be written
# languages = { 'Canada': 'French', 'United States' : 'English', 'Mexico' : 'Spanish', 'Brazil' : 'Portuguese' }

print(languages[1]) # This causes Python to throw a 'KeyError' exception
print(languages['Brazil']) # This prints Portuguese
print(languages['Suriname']) # This prints Dutch

#Sets - are lists that cannot contain duplicate values, also use curly brackets
#set() to create an empty set
#set{} to create a non-empty set
#update() method adds values to our set, will ignore duplicate values
#EX1:
# mySet = {} Cannot create empty set like this
# mySet = {'a', 'b'} But you can create non-empty set like this
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet) # Prints {1, 2}
mySet.add(1)
print(mySet) # Still prints {1, 2}
otherSet = {5, 6, 7}
mySet.update(otherSet) # Adds {5, 6, 7} to the contents of mySet
print(mySet) # Prints {1, 2, 5, 6, 7}

#discard() - method that will remove a value from the set, wont error out if provided value isnt found
#remove() - method that will remove a provided value from the set, but will raise the 'KeyError' exception if value is not found
#pop() - removes a value at random (removes the beginning of the list but sets do not have an order causing pop to randomly return and remove a value)
#EX2:
mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
mySet.discard('a')
mySet.remove('b')
mySet.pop()

#Union() - method to create a new set composed of the values of two sets
#intersection() - method is used to create a new set from those values vetween the sets that match
#difference () - method used to create a new set from those values that are unique to provided set
#EX3:
mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
otherSet = {'z', 'y', 'x', 'w', 'v', 'u', 'b', 'a'}

union = mySet.union(otherSet)
intersection = mySet.intersection(otherSet)
difference = mySet.difference(otherSet)

print(union) # Prints {'c', 'v', 'd', 'w', 'z', 'u', 'y', 'x', 'a', 'b', 'f', 'g', 'e'}
print(intersection) # Prints {'a', 'b'}
print(difference) # Prints {'c', 'd', 'f', 'g', 'e'}
##################################################################################################################################################

##Error Handling##
#Two types of errors: syntax error and an exception
#Syntax Error - an error in the way you've written code, typically caught by your development environment (usually highlighted)
#Exception - errors that arise whenever you are executing code and something happens that shouldn't 
#Always read the error message

#try / except statements - way to deal with error causing code
#EX1:
try:
    file = open(r"/path/to/file/file.txt", "r")
except FileNotFoundError:
    print("file not found")

try:
    otherFile = open(r"/path/to/other/file/otherfile.txt", "r")
except:
    print("file not found")

#Be careful to identify the specific errors and dont disguise it using a try/except - utilize several except statements together to handle more
#EX2:
try:
    file = open(r"/path/to/file/file.txt", "r")
except EOFError:
    print("input / output error")
except FileNotFoundError:
    print("file not found error")
except:
    print("some other kind of error")

#finally - cleans up the end of try/except statemetns, used after the code inside the try or except has finished executing - this block executes no matter what
#EX3:
file = None
try:
    file = open(r"/path/to/real/file/realFile.txt", "r")
except FileNotFoundError:
    print("file not found error")
except EOFError:
    print("input / output error")
except:
    print("some other kind of error")
finally:
    file.close()
    print("Closing file")