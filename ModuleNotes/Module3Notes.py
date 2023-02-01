##Class Notes##
###################################################################################################################################
#Input/Output  - function "open()" is used to open a file: Two parameters - file path/file name and the open mode#

#file = open("C:\FakeExample\Path1","X")

#|Parameter Abbreviation | Mode | Function |
#|r | read mode | allows you to read contents |
#| r+ | read and write mode | does not create a file if doesnt already exist |
#| w | write mode | allow you to read and modift the contents of a file |
#| w+ | write mode | same as w, but will create a file if it doesnt exist |
#| a | append mode | allows you to read and add to the contents of a file |
#| a+ | append mode | same as a, but will create a file if it doesnt exist |

#Opening a non-empty file using w mode, the file will be wiped clean (Utilize 'a' instead)
#Put 'r' in the beginning of the file = open() function to utilize verbatim raw string

#File - variable allowing you to use several file specific functions (methods) that do file operations

#Read() and Readlines() are specific to python file objects

#Read() - reads the entire conents of the filel into a string variable 
#Upon establishing a variable referencing the value returned by read(), we can print the contents using a print statment and our variable

#Readlines() - grabs every line and puts each line into a list, useful for processing and searching data
#Upon establishing a variable referencing the value returned by read(), we can print the contents using a print statment and our variable

#try/except block - utilized to handle errors when trying to open or create a file w/o causing python to break
#EX:
try: 
    file = open('tile.text','r')
    data = file.read()
    file.clos()
except IOError:
    print("An Error Has Occured")

#close() - must close files opened in programming environments programmatically. Not required when reading a file, but is good practice

#write() - utlize 'w' in file methods if starting from scratch. Name in file path will be the fresh files name.
#\n is the new line equivalent to enter in excel, vbanewline in VBA
#EX:
#newFile = open('newFile.txt', 'w')
#newFile.write("Hello world/n")
#newFile.write("Hello world 2/n")
#newFile.write("Hello world 3/n")
#newFile.close()

#|Common Errors | Error | Solution |
#| 1 | FileNotFoundError" [Errno 2] No such file or directory | Try using an absolute path to file instead of name |
#| 2 | PermissionError: [Errno 13] Permission denied | check if opening a directory or file |

###################################################################################################################################
#Regular Expressions - sometimes written 're' or 'regex' - allow you to create tet patterns that can be used for searching strings, files, etc

#find() or replace() can search text blocks of code but have shortcomings

#Basic Patterns#
#| RegEx Expression | Matches |
#| [aeiou] | any vowel |
#| junk | the string "junk" |
#| . | a single char |
#| \w | a singl alphanumeric char |
#| \W | a single non alphanumeric char |
#| \b | a boundary between words |
#| \s | a single whitespace char |
#| \t | a tab |
#| \n | a new line |
#| \r | a return |
#| \d | a digit |
#| \D | s asingle non-digit char |
#| * | any number of what comes before * |
#| + | one or more of what comes before + |
#| ^ | the start of a string |
#| $ | the end of a string |
#| x{n,m} | char x at least n times, but less than m times |

#RegEx Methods - must import using 'import re' line

#Match() - look for a match at the beginning of a line, will return a matchobject
#EX:
#import re
#result = re.match("c", "cat")
#print(result) # Prints <_sre.SRE_Match object; span=(0, 1), match='c'>
#result = re.match("a", "cat") # Prints None since "a" is not at the beginning of our string
#print(result)

#Search() - method that attempts to match throughout the string until it finds a match, returns a matchobject
#EX:
#import re
#result = re.search("i", "abcdefghijklmnopqrstuvwxyz")
#print(result) # Prints <_sre.SRE_Match object; span=(8, 9), match='i'>

#sub() - search the entire input for the specified pattern and replace with a given value
#EX:
#import re
#s = '100 NORTH BROAD ROAD'
#result = re.sub('ROAD$', 'RD.', s)
#print(result) # Prints 100 NORTH BROAD RD

#Findall() - method will return an arrary of all non-overlapping matches
#EX: 
#x = "6 geese a-layin' 51 golden rings 4 calling birds 33 French hens 2 turtle doves 91 partridge in a pear tree"
#result = re.findall(r"\d+", x)
#print(result) # Prints ['6', '51', '4', '33', '2', '91']

#add an additional comma and s: ',s)' to have regex remember your replacements

###################################################################################################################################
#Object Oriented Programming (OPP)

#Classes - Core of OOP, groups similar functions and objects
#EX:
class car: #the class is called car, and has two functions 'setcolor()' and 'honkhorn' - known as methods
    def __init__(): #notice two underscores on either side of 'init' - is the initializer 
        pass #each method must take at least one argument
    def setcolor(self, newcolor): #referencing this istance of class using 'self'
        self.color = newcolor
    def honkhorn(self): #if calling a method outside of the class, 'self' parameter is supplied automatically and not needed
        print("Beep Beep")

#class truck:
#    def __init__(self,value):
#        self.mpg = value
#x = truck(17)

#Objects - individual instances of a class created using the class as a blueprint - you can have multiple instances of the same class
#Ex1
class Car:
    def setColor(self, newColor):
        self.color = newColor
    def honkHorn(self):
        print("Beep beep")

chevy = Car()
chevy.setColor('red') # Method that sets a new color for the chevy instance
chevy.honkHorn() # Method that prints 'Beep beep'

class Car:
    def setColor(self, newColor):
        self.color = newColor
    def honkHorn(self):
        print("Beep beep")
#EX2
chevy = Car()
ford = Car()
if chevy == ford:
    print("TRUE")
else:
    print("FALSE")

chevy.setColor('Red')
ford.setColor('Blue')
print(chevy.color)
print(ford.color)
#When wanting to call a function specific to a method, use the object name, a period, and the name of the method we want to all. EX: chevy.setcolor()

#Attributes - defined by an assignment statement, data types that are grouped together into a single package
#Two types of attributes: class and instance
#Class Attributes - defined like normal variables but are at the same id level as class methods - exist for each and every instance of an object
#Instance Attributes - inside of a method and are asigned using self or defined outside of a class usinga  normal assignment statement

#EX1
class Truck:
    numOfWheels = 4 # This is an example of a class attribute; all instances of Truck have 4 wheels
    def __init__(self, color):
        self.color = color # This is an example of an instance attribute; only some instances will have a color attribute (that is, if it was created like so `chevy = Truck('green')`

chevy = Truck()
chevy.color = 'Green' # This is another example of an instance attribute
chevy.tinted = True # This is an example of an instance variable defined outside the class
print(chevy.numOfWheels) # This prints our class attribute numOfWheels

#Subclass - includes any class attributes of the parent class (inheritance)
#EX2
class Vehicle:
    numOfWheels = 4
    def __init__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        pass

ford = Truck()
print(ford.numOfWheels) #Object Ford is a type of truck which does not have a class attribute of numofwheels declared, but it will still print 4 becasue truck is a subclass of vehicle

#Encapsulation - object behavior and object data are combined in a single entity - meaning the objecs interface defiens the interaction with the object
#Note - write to the interface not the implementation, so to limit the function and allow free manipulation of internal data w/o error
#EX1 - an encapsulated class
class Atom:
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.__position = (x, y, z) #__position is private
    def getPosition(self):
        return self.__position
    def setPosition(self, x, y, z):
        self.__position = (x, y, z)
    def translate(self, x, y, z):
        x0, y0, z0 = self.__position
        self.__position = (x0 + x, y0 + y, z0 + z)

atom = Atom(14, 1, 1, 2)
atom.translate(2, 3, 8)

#Inheritance - the hierarchy in which attributes and methods can be established. Not necessary to build every class from scratch
#EX2
class Molecule:
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addAtom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' %self.name
        str = str + 'It has %d atoms\n' %len(self.atomlist)
        for atom in self.atomlist:
            str = str + 'atom' + '\n'
        return str

class Better_Molecule(Molecule):
    def __init__(self, name = 'Generic', basis = '6-31G**'):
        self.basis = basis
        Molecule.__init__(self, name) # Calls the constructor for the parent function
    def addBasis(self):
        self.basis = []
        for atom in self.atomlist:
            self.basis.append(atom)

newMolecule = Better_Molecule('dihydrogen monoxide', '5-18Q**')
newMolecule.addAtom('H') # Object uses method defined in Molecule instead of Better_Molecule
newMolecule.addBasis() # Object can also use methods of Better_Molecule

#Polymorphism - programming feature that allows values of diff data typesto be handled using a uniform interface
#EX1
class Shape():
    def __init__(self, color):
        self.color = color
    
    def getArea(): # We cannot calculate area if we do not know the shape
        pass

class Rectangle(Shape):
    
    def __init__(self, color):
        self.color = color
        Shape.__init__(self, color) 

    def setLength(self, length)
        self.l = length

    def setWidth(self, width)
        self.w = width
    
    def getArea():
        return l * w

class Circle(Shape):
    
    def __init__(self, color):
        self.color = color
        Shape.__init__(self, color) 
        
    def __init__(self, color, radius):
        self.color = color
        self.r = radius
        Shape.__init__(self, color) 

    def setRadius(self, radius)
        self.r = length
    
    def getArea():
        return math.pi * self.r * self.r
        

shape1 = new Shape("blue")

shape2 = new Rectangle("red")
shape2.setLength(3)
shape2.setWidth(4)
print(shape.getArea()) #Prints 12

shape3 = new Circle("orange")
shape3.setRadius(5)
print(shape.getArea()) #Prints 78.5398163397

shape4 = new Circle("orange", 2) # Calls second constructor of circle
print(shape.getArea()) #Prints 12.5663706144

#In above, rectangle is an instance of shape but shape is not an instance of rectangle, the super class shape sets the methods while rectangle defines how to operate the methods