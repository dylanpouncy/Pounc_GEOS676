#Modules, Packages, Libraries, and Plugins - third party add-ons for time consuming and powerful functions

#Modules - are files that contain plain python code, definitions, and statements. Have a file extension of ".py". Everything completed o far is considered a module
#Used to organize code logically, useful to seperate similar functions and code into seperate modules

#Package - collection of special modules, modules that contain "__path__" attribute is considered a package. Popular packages includes numpy, scipy, math

#Library - is a term not synonymous with python typically, but commonly substituted for packages. Refers to a collection of modules

#Import - function used to 'import' new functionality, classes, data types, etc
#You can rename imported modules using the "as" keyword followed by the new name
#EX
import numpy as np
np.arange(15).reshape(3, 5)

#from blank import blank - used to specify specific moduels or functions from a package, time saver if importing several large packages
#EX1
from numpy import * #Using * will import all modules and functions from a package, similar to select * in SQL
from numpy import ndarray #Only imports ndarray from numpy

#Creating a module - previously written python scripts can be implemented into new projects w/o copy + paste, using import
#EX1
#addition.py
def addNums(numbers):
    return sum(numbers)
#test.py
"""
from addition import addNums #wont run as the file is not called 'addition.py', could sub with 'Module6Notes.py'
x = [1, 3, 5, 7, 9]
print(addnums(x))
"""
#In above example, two modules called addition.py and test.py, we import functionality from addition.py into test.py w/o having to copy and paste

#Lambdas - short-hand function we can write in a single line and assign to a variable, also called anonymous functions. Useful for short function w/o having to set up a new definition
#EX1
isOdd = lambda num: num % 2
print(isOdd(6)) #prints 0m which means num was even
#Longer alternative
def isOdd(num):
    return num % 2
print(isOdd(6))

#Map - a way to apply a function to all members of a list, tuple, or set quickly. Can replace a loop or other iteration technique with one line of code
#EX1
x = [2, 3 ,4, 5 ,6, 7, 8]
squareEM = lambda num: num ** 2
y = list(map(squareEM, x))
z = map(squareEM, x)
print(y) #prints [4, 9, 16, 25, 36, 49, 64]
print(z) #prints <map object at 0x000001EF315B2470> - this is the result of not turning our result into a list, which instead prints the location in memory of z

#Filter - type of map that only returns values that are true
#Boolean statements return False(0) or True(1)
#EX1 
x = [2, 3, 4, 5, 6, 7, 8]
y = list(filter(lambda num: num % 2 == 0, x)) #Serves as a conditional
z = list(filter(lambda num: num % 2, x))
print(y) #prints [2, 4, 6, 8]
print(z) #prints [3, 5, 7] #not conditional, cast as a boolean. Since an odd number has a remainder of 1 when divided by 2, the 1 triggers the 'True' option and returns those values

#Reduce - a function used to quickly calculate a single number given a list of values. Provided a function and input list, reduce will run each value and return you a result
#EX1
from functools import reduce
x = [2, 3, 4, 5, 6, 7, 8]
add = lambda total, num: total + num #function takes two arguments: one being the result that is calculated and second being the input numbers. This lambda adds numbers to total
summation = reduce(add, x) #contains the call to reduce, takes two parameters: function used to calc and the input list
print(summation) #prints 35, calls the function once for each item in the input list, processes it using lambda, and in this case adds it to the total

#Generators - not technically functions like above, but generate values whenever called. Can be identified using their keyword yield instead of return
#Typically used to generate large data sets without allocating memory for all of the values or creating any functin so that it may be used in a for loop
#fib() - used to generate the fibonacci sequence
#EX1
def fib(n): #takes a single value that determines how many digits in the fib seq to print out
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
for x in fib(6):
    print(x) #prints 1, 1, 2, 3, 5, 8 - This function yields the local variable a with every iteration, thereby printing out the sequence

#Arcpy Advanced Functions -

#Renderers - used by ArcGIS to determine how feature data gets drawn on the screen. Tells the program how the data should be presented to the user: 4 basic types. Not all layers support renderers, so check that the layer has a renderer attribute before trying
#Use supports() method of the 'layer' class to check if the layer supports renderers, will return a boolean value
#EX1
"""
if layer.supports("GRADUATED_COLORS"):
    print("The Layer Supports a Graduated Colors Renderer.")
"""

#SimpleRenderer - most basic and default, used to draw all features of a layer the same. Used when adding a feature class to a map, offers a plain all-one-color view

#UniqueValueRenderer - used to distinguish features in a feature layer based off of some classification, usually a data field. Given programmatic control over the type of field used in the classification of features as well as colors when drawing

#GraduatedColorsRenderer - used to render features in a feature layer based off of a specific field within the feature class. Can create chropleth maps programmatically, allows user to determine how many bins are present and colors

#GraduatedSymbolsRenderer - allows you to render features in a feature class depending on a number of bins. Used to create graduated symbol styled maps

#Making a Map with UniqueValueRenderer
"""
import arcpy
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:/tmp/ArcGISPython/" + r"\\Mod23.aprx")
# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check that the layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Makes sure symbology has an attribute "renderer"
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is "Structures"
            if layer.name == "Structures":
                # Update the copy's renderer to be "UniqueValueRenderer"
                symbology.updateRenderer('UniqueValueRenderer')
                # Tells arcpy that we want to use "Type" as our unique value
                symbology.renderer.fields = ["Type"]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT Structures")
project.saveACopy(r"C:/tmp/ArcGISPython/" + r"\\Mod23b.aprx")
"""

#Making a Map with GraduatedColorsRenderer
"""
import arcpy
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:/tmp/ArcGISPython/" + r"\\Mod23.aprx")
# Grab the first map in the .aprx
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
for layer in campus.listLayers():
    # Check if layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Check if it has a 'renderer' attribute
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is 'GarageParking'
            if layer.name == "GarageParking":
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                # Tell arcpy which field we want to base our choropleth off of
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have 
                symbology.renderer.breakCount = 5
                # Set the color ramp
                symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT GarageParking")
project.saveACopy(r"C:/tmp/ArcGISPython/" + r"\\Mod23c.aprx")
"""

#Arcpy Tool Messaging - why you should utilize updateMessages() and how to go about using it

#Adding a new input to the toolbox we created previously for seeing which buildings were near a particular building
#We want to be able to display a message to inform the user if they try to buffer a building that does not exist inside the campus 'Structures' feature clss
#Prior code needed for teh toolbox from previous lecture
"""
import arcpy


class Toolbox(object):
    def __init__(self):
        #Define the toolbox (the name of the toolbox is the name of the
        #.pyt file).
        self.label = "GEOG676_Tools"
        self.alias = "GEOG676_Tools"

        # List of tool classes associated with this toolbox
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        #Define the tool (tool name is the name of the class).
        self.label = "Building Proximity"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False # Only used in ArcMap
        self.category = "Building Tools"

    def getParameterInfo(self):
        #Define parameter definitions
        param0 = arcpy.Parameter(
            displayName="Building Number",
            name="buildingNumber",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="Buffer radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        param1.filter.type = "Range"
        param1.filter.list = [10, 100]
        params = [param0, param1]
        return params

    def isLicensed(self):
        #Set whether tool is licensed to execute.
        return True

    def updateParameters(self, parameters):
        #Modify the values and properties of parameters before internal
        #validation is performed.  This method is called whenever a parameter
        #has been changed.
        return

    def updateMessages(self, parameters):
        #Modify the messages created by internal validation for each tool
        #parameter.  This method is called after internal validation.
        return

    def execute(self, parameters, messages):
        #The source code of the tool
        campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True

        # If we shouldProceed do so
        if shouldProceed:
            # Generate the name for our generated buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
            # Get reference to building
            buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
            # Buffer the selected building
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Remove the feature class we just created
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
        else:
            print("Seems we couldn't find the building you entered")
        return None
"""
#Adding in an error message to above - adding code to the updateMessages() method inside our BuildingProximity class
"""def updateMessages(self, parameters): #two arguments, the parameters agrument passed in here are the parameters we defined in getParameterInfo() method
    #Modify the messages created by internal validation for each tool parameter. This method is called after internal validation
    return
"""
#loop through parameters to find the parameter with a name of buildingNumber (this is the name we gave the parameter that holds our building number input)
"""def updateMessages(self, parameters):
    for param in parameters:
        if param.name == "buildingNumber":
            #We've found the correct parameter
            buildingNum - param.value #wont run w/o previously defining buildingNum which isnt done in this notes module
    return
"""
#With the parameter found, we need to check if the value provided exists inside the 'Structures' layer - use a SearchCursor and count how many results we get back
#Redefine campus and where_clause variables so we can acess data layers, then create cursor variable that contains the results of the SearchCursor
"""def updateMessages(self, parameters):
    for param in parameters:
        if param.name == "buildingNumber":
            buildingNum = param.value
            campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/24/Campus.gdb"
            where_clause = "Bldg = '%s'" % buildingNum
            cursor = arcpy.SearchCursor(campus + "/Structures", where_clause=where_clause)
        return
"""
#Since you cannot use len() on cursors, you must determine how many rows are in the cursor. So iterate using a for loop and count how many times the loop executes, then check if count is greater than 0
"""
def updateMessages(self, parameters):
    for param in parameters:
        if param.name == "buildingNumber":
            buildingNum = param.value
            campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/24/Campus.gdb"
            where_clause = "Bldg = '%s'" % buildingNum
            cursor = arcpy.SearchCursor(campus + "/Structures", where_clause=where_clause)
            count = 0
            for row in cursor:
                count += 1
            if count == 0:
                param.setErrorMessage("Cannot find building %s in Structures" % buildingNum)
    return
"""
#Only interested if no rows are returned, as that would mean the building is not in the structures feature class. Utilize setErrorMessage() method on parameter to inform user

#Adding a progressor - little bar that lets you know the tool is currently working, tracks progress. Two types: default and step
#Adding one is fairly simple, set it and periodically change the position and label. Inside of the execute() method
"""
readTime - 1.5 #used to delay titels so user can read the text
start = 0 #defines the beginning position of our progressor
maximum = 100 #defines the absolute maximum value
step = 25 #used to move the progressor bar along
"""
#To set up the progressor, you must call arcpy.SetProgressor() and providing 5 paramets: type, label, start value, end value, and step value
"""
arcpy.SetProgressor("step", "Checking Building Proximity...", start, maximum, step)
"""
#Once set up, we can use method code to advance the progressor
"""
arcpy.SetProgressorPosition(start + step) #changes the percentage completed of the progressor
arcpy.SetProgressorLabel("Validating building number once more...") #changes the message displayed
time.sleep(readTime) #momentarily halting the execution of our tool to allow progressor labels to be read
"""

#Execute - entire execute method of newly imnproved tool below
"""
 def execute(self, parameters, messages):
        #The source code of the tool.
        # Define our progressor variables
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # Setup the progressor
        arcpy.SetProgressor("step", "Checking building proximity...", start, maximum, step)
        time.sleep(readTime)
        # Add message to the results pane
        arcpy.AddMessage("Checking building proximity...")

        campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"
        
        # Setup our user input variables
        buildingNumber_input = parameters[0].valueAsText
        bufferSize_input = int(parameters[1].value)

        # Generate our where_clause
        where_clause = "Bldg = '%s'" % buildingNumber_input

        # Check if building exists
        structures = campus + "/Structures"
        cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
        shouldProceed = False

        # Increment the progressor and change the label; add message to the results pane
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Validating building number once more...")
        time.sleep(readTime)
        arcpy.AddMessage("Validating building number once more...")

        for row in cursor:
            if row.getValue("Bldg") == buildingNumber_input:
                shouldProceed = True


        # If we shouldProceed do so
        if shouldProceed:
            # Generate the name for our generated buffer layer
            buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
            # Get reference to building
            buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
            # Buffer the selected building
            arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
            # Increment the progressor, change label, output message to results pane too
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Buffering....")
            time.sleep(readTime)
            arcpy.AddMessage("Buffering...")
            # Clip the structures to our buffered feature
            arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
            # Increment the progressor, change label, output message to results pane too
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Clipping....")
            time.sleep(readTime)
            arcpy.AddMessage("Clipping...")
            # Remove the feature class we just created
            arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
            # Increment the progressor, change label, output message to results pane too
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("Cleaning up files....")
            time.sleep(readTime)
            arcpy.AddMessage("Cleaning up files...")
        else:
            print("Seems we couldn't find the building you entered")
        return None
"""

#Arcpy data format conversion - data wrangling

#CSV Files - comma seperated values are a way to store data in a human readable structure. Typically have headers in first position. CSV's order does matter
"""
User,Email,State,Country
Bill,bill@aol.com,Texas,United States
Jim,jim@yahoo.com,Oklahoma,United States
"""

#CSV to GDB
"""
  import arcpy
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.csv" #variable 1, ref csv file, passed in
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb" #variable 2, ref desired output gdb
    arcpy.management.MakeXYEventLayer(stadiums, "lon", "lat", campus + "/Stadiums") #completes the conversion, states where coordinate fields are and the output location
"""

#GDB to CSV - example creates a csv using a feature class found inside the gdb
"""
 import arcpy
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    garages = campus + "/GaragePoints"
    garageFile = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/garagesFromGdb.csv"
    search = arcpy.da.SearchCursor(garages, field_names=["Name", "SHAPE@XY"]) #grabs all features in the feature class
    file = open(garageFile, "w")
    file.write("GarageName,lon,lat\n")
    for row in search:
        print(row)
        file.write("%s,%s,%s\n" % (row[0], row[1][0], row[1][1])) 
"""

#CSV to Table (simple table in gdb)
"""
    import arcpy
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.csv"
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.TableToTable_conversion(stadiums, campus, "StadiumsTable") #provdie the input, output location, and output name
"""

#CSV to GDB alternative
"""
 import arcpy
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    export_fields = [Number;BldgAbbr;BldgName]
    output_location = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/Structures.csv"
    arcpy.stats.ExportXYv(campus + "/Structures", export_fields, "COMMA", output_location, "ADD_FIELD_NAMES") #provide the input feature, fields included, delimiter, output location, and field names as a header (optional)
"""

#KML - key-hole markup language is a way to structure data ased off of markup language making it very similar to XML and HTML. Data is stored by tags that define the type of data

#KML to Layer
"""
  import arcpy
    stadiums = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/stadiums.kml"
    arcpy.KMLToLayer_conversion(stadiums, "C:/tmp/ArcGISPython/") #Use KML as first parameter, output location as second
"""

#Layer to KML - can only convert layers to KMZ (compressed KML files)
"""
  import arcpy
    stadiums = r"C:/tmp/ArcGISPython/stadiums.lyrx"
    kml = r"C:/tmp/ArcGISPython/stadiums.kmz"
    arcpy.LayerToKML_conversion(stadiums, kml)
"""

#JSON - javascript object notaion is a langauge agnostic data structure that organizes data in a compact and human readabe structure much like a csv. However, JSON uses a key-value strucure
"""
{
    "Will": "Will Smith", #Key-value pairs are sepearated by a colon, left side is key and right side is value
    "Uncle Phil": "James Avery",
    "Carlton": "Alfonso Ribeiro",
    "Aunt Viv": {
        "first": "Janet Hubert",
        "second": "Daphne Reid"
    },
    "Aunt Viv Array": ["Janet Hubert", "Daphne Reid"]
}
"""

#ESRI JSON - way of describing geographic data in a JSON format, however unlike GeoJSON, ESRI JSON is only used by ESRI and is limited in use only ArcGIS REST API functions
"""
{"x" : -118.15, "y" : 33.80, "spatialReference" : {"wkid" : 4326}}
"""

#ESRI JSON to GDB
"""
  import arcpy
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.JSONToFeatures_conversion(r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/testjson.json", campus + "/TestJSON")
"""

#GDB to ESRI JSON
"""
import arcpy
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    arcpy.FeaturesToJSON_conversion(campus + "/GarageParking", "C:/tmp/ArcGISPython/garage.json", format_json=True) #takes input feature class, output file name and path, and a special parameter called 'format_json'
#if format_json is set to true, the output will be in a human readable format, false removes white spaces and values
"""

#GeoJSON - encodes geographic data to a JSON object. Standard for GIS applications and websites everywhere
"""
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}
"""

#GDB to GeoJSON
"""
import arcpy
    campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/25/Campus.gdb"
    output = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/code/25/outputgeojson.json"
    arcpy.FeaturesToJSON_conversion(campus + "/GarageParking", output, format_json=False, geoJSON=True)
"""

#Shapefiles - 