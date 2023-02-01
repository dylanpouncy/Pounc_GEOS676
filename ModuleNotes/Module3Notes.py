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
