##Working with NumPy, PySAL, and R##

#Numpy - fundamental package for scientific computing in python, including support of n-dimensional array objects. Provides an evenue to perform complex operations and is included in ArcGIS
import numpy
import arcpy

#Working with tables and feature data - converting table and feature classes to and from Numpy array using functions in the data access (arcpy.da) module
#Numpy arrays must be structured arrays if they are to be converted to tables and feature classes

#Structured Arrays - is an n-dimensional array whose datatype is a composition of simplier datatypes organized as a sequence of named fields
#EX1
x = numpy.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)], 
    dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
#Two parameters - each one a list. First list contains data entries and are contained within a standard python tuple. Second parameter is called dtype, which we use to define teh structure of our data
#3 tuples in dtype whicch correspond to the three data parts of each tuple in the first parameter, these structure tuples have two parts: the field name and the field data type
#First structure tuple has two values: name an U10. Name is the name of the field: Rex and Fido are names. The value U10 means that the data type for the name field will be a string of up to 10 chars in length
#Next field is age and is a signed integer 32-bit integer. Last field is weight which contains a 32-bit floating-point number
"""
Character - datatype
? - boolean
b - signed byte
B - unsigned byte
i - signed integer
u - unsigned integer
f - floating-point
c - complex-floating point
m - time delta
M - datetime
O - python objects
U - unicode string
V - raw data
""" 

#Numpy array to geodatabase feature class - NumPyArrayToFeatureClass() method of arcpy
#providing a structured array, output feature class name, field the coordinates are located in, and the outputs spatial reference
#EX1
"""out_fc = 'C:/tmp/ArcGISPython/DC.gdb/pointlocations'

# Create a numpy array with an id field, and a field with a tuple 
#  of x,y coordinates
arr = numpy.array([(1, (471316.3835861763, 5000448.782036674)),
                   (2, (470402.49348005146, 5000049.216449278))],
                  numpy.dtype([('idfield', numpy.int32),('XY', '<f8', 2)]))

# Define a spatial reference for the output feature class
spatial_ref = arcpy.Describe('C:/tmp/ArcGISPython/DC.gdb/removed_trees').spatialReference

# Export the numpy array to a feature class using the XY field to
#  represent the output point feature
arcpy.da.NumPyArrayToFeatureClass(arr, out_fc, ['XY'], spatial_ref)"""
#File paths are not accurate and therefore the script will not execute

#Feature Class to Numpy Array - FeatureClassToNumPyArray()
#EX1
"""fc = 'C:/tmp/ArcGISPython/DC.gdb/pointlocations'
fields = ["idfield"]
arr = arcpy.da.FeatureClassToNumPyArray(fc, fields, skip_nulls=True)"""
#File paths are not accurate and therefore the script will not execute

#PySAL - python spatial analysis library is an open source library of spatial analysis functions written in python intended to support the development of high level applications. Has a while before it can replace arcpy, but can perform powerful spatial analysis in python
#import pysal - unresolved errors in downloading
#pysal packages and uses
"""
pysal.cg - computational geometry
pysal.core - core data structures and IO
pysal.esda - exploratory spatial data analysis
pysal.inequality - spatial inequality analysis
pysal.region - spatially constrained clustering
pysal.spatial_dynamics - spatial dynamics
pysal.spreg - regression and diagnostics
pysal.weights - spatial weights
pysal.network - network constrained analysis
pysal.contrib - contributed modules
"""

#PySAL is a very specific tool for research and spatial statistics while arcpy is a swiss army knife
#This code will create five diff maps each with a different classification method using pysal
#EX1
"""
import numpy as np
import pysal as ps
from pysal.contrib.viz import mapping as maps
shp = ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp")
dbf = ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.dbf")
values = np.array(ps.open(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.dbf").by_col("HR90"))
types = ["classless", "unique_values", "quantiles", "equal_interval","fisher_jenks"]
for typ in types:
    maps.plot_choropleth(r"D:\DevSource\Tamu\GeoInnovation\_GISProgramming\data\modules\30\texas.shp",values,typ,title=typ)
"""

#R - free, statistical computing and graphics programming language supported by the R foundation. Thanks to ESRI's R-ArcGIS bridge, R scripts can run directly from ArcGIS as a tool
#Follow instructions on github to install R and the R-ArcGIS bridge

#ESRI's python products (arcpy, arcgis api for python, and arcgis pro sdk)

#ArcPy - python site package that provides a rich and native python experience offering code completion and reference documentation 

#ArcGIS API for python - python library for working with maps and geodata powered by web GIS

#ArcGIS Pro SDK - does not utilize python, this is another way to expand upon the functionality of ArcGIS Pro. Software development kit that allows you to creat custom add-ins
"""
Allows for the following -
Framework - buidling add-ins to extend the Pro UI and leverage asynchronous programming
Editing - creating custom tools 
Map Exploration - create capabilities to naviagate and explore maps
Content - manage project content items
Utility Network - develop custom network traces 
Configurations - create custom solution configs with a custom start page
Map Authoring - creating content 
Geodatabase - edit and work w/ GDB feature data
etc
"""

#Debugging - a way to run through code line by line to investigate variables and pinpoint the order of operations to gain insight into error prone code

#Debugging python within VSCode - once python is installed, run the debugging widget
#Debug pane will have four categories: variables, watch, call stack, and breakpoints

#Breakpoints - tell the python interpreter to stop executing code once the breakpoint has been reached. Set it by clicking on the '+' sign to the right of the breakpoints category header or the space to the left of any line number. (represented by a red dot)
#Highlights the row in python yellow

#Variables - lists all the variables and their current values at the present part of the code (or at a breakpoint). Breaks variables into local and arguments, and will hold code until told to continue

#Watch - watches the value of specific variables without having to look through the variables category

#Call Stack - used to see where inside the call stack teh code currently is
#EX1
def add(a, b):
    print("x: ", x)
    print("y: ", y)
    return x + y
def subtract(i, k):
    print("x: ", x)
    print("y: ", y)
    return x - y
x = 6
y = 4
add(x, y)
subtract(x, y)
#If you set a breakpoint at the line of code labeler "subract(x,y)" you will see different outputs than if set elsewhere. Useful for when projects grow to span many modules

#Debugging arcpy - use arcpy.AddMessage() to print values to the screen to debug, no other great way

#REST - representational state transfer is a set of constraints used to interact with web services. These constraints allow users to interact with the web without knowledge as to details 
#requests.get() is used to get data from a web service
#Check the selected feature class supports query - typically found at the bottom of an individual layers page on ArcServer
import arcpy
import requests #allows us to make REST calls programmatically

#when making a GET call to an arcserver, we need to create a query string, this is passed to requests which in turn use the query string as a directory of where it should get data from and what data it will get
#EX1
"""
response_format = "pjson" #used to tell arcserver the format we want our data to be given to us in (default is XML)
where_clause = "objectid+>+0" #used to determine which data we want back (python cursor object)
query_url = "https://gis.tamu.edu/arcgis/rest/services/FCOR/BaseMap_051118/MapServer/9/query?where=%s&f=%s" % (where_clause, response_format) #URL to the arcserver feature layer and two parameters
response = requests.get(query_url)
print(response.json())
"""
#Convert JSON format into a feature layer to import into ArcGIS. Write JSON response to a file then convert using JSONToFeatures_conversion() method
"""
with open(r"C:/tmp/ArcGISPython/json_response.json", "w") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk) #prevents entire response from being loaded into memory at once
"""
#Put JSON into a feature class; first parameter is the path to the JSON file, the second is the path for the newly created feature class
"""
arcpy.JSONToFeatures_conversion(r"C:/tmp/ArcGISPython/json_response.json", r"C:/tmp/ArcGISPython/Test.gdb/trees")
"""
