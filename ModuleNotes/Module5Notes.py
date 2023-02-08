#Arcpy Operations#

#clip - tool used to "cut" a feature class witha geometry of another feature calss, known as the clip feature - only retains attributes from the input (vs. both using intersect)
#EX1:
import arcpy
arcpy.env.workspace = "C://tmp//ArcGISPython" #replace
# Define our geodatabase
campus = r"D://DevSource//Tamu//GeoInnovation//_GISProgramming//data//modules//17//Campus.gdb" #replace
# Perform a clip
arcpy.Clip_analysis(campus + "/Structures", campus + "/GaragePoints_buffered", campus + "/Clipped_structures")
#first parameter defines the input layer
#second parameter defines our clip feature
#third parameter defines the output layer

#Dissolvle - tool used to aggregate features in a feature class based on a specific attribute
#EX1:
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython" #replace
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb" #replace
# Dissolve the layer
arcpy.Dissolve_management(campus + "/Structures", campus + "/Dissolved_structures", "Type")
#first parameter defines the input layer
#second parameter defines the output layer
#third parameer defines which field in the input we want to dissolve our feature class with

#Union - tool used to combine attributes and features of two feature classes into a new feature class - resulting feature class will contain attributes from both feature classes 
#only works with polygons and can be specifiedto remove some attributes
#EX1:
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython" #replace
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb" #replace
# Define our layers
structures = campus + "/Structures"
landuse = campus + "/LandUse"
# Perform a union of two layers
arcpy.Union_analysis([structures, landuse], campus + "/Campus_union", "NO_FID")
#first parameter is a list defining all input layers
#second parameter defines the resulting layer created
#third paratemer defines how the union will operate

#select - a tool used to extract features from a class using a SQL expression - upon completion, the new layer contains features that satisfy the defined where clause
#EX1:
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython" #replace
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb" #replace
# Define our where clause
where = '"Type" = \'HOUSING TAMU\''
# Perform a select
arcpy.Select_analysis(campus + "/Structures", campus + "/housing", where)
#first parameter defines the input feature class
#second parameter defines the output feature class
#third parameter (where clause) is a SQL statement that limits the results of a query to definition
#################################################################################################################################################################
#Cursors - data access objects that let the programmer look for or update data in a table - 3 types

#InsertCursor() - used to generate a new cursor for writing data to a feature class or table
#EX1
"""import arcpy
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define our tower point location
towerLocation = ('Albritton Bell Tower', (30.61320, -96.34381))
# Create the insert cursor
insertCursor = arcpy.da.InsertCursor(campus + "/Albritton", ["BldgName", "SHAPE@XY"])
# Insert a new row into the feature class
insertCursor.insertRow(towerLocation)
# Delete insertCursor to free the data lock
del insertCursor"""

#SerachCursor() - used to look for a particular value in an input data set - often paired with a where clause to limit return values
#Search cursors can return more than one value so you will need to iterate through using a for loop or next() function
#EX1: Using a for loop
"""import arcpy
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
searchCursor = arcpy.da.SearchCursor(campus + "/GaragePoints", fields)
for row in searchCursor:
    print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
# Delete the cursor to free the data lock
del searchCursor"""

#EX2: Using the next() function
"""import arcpy
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
searchCursor = arcpy.da.SearchCursor(campus + "/GaragePoints", fields)
try:
    # Setup row variable with the first value 
    row = next(searchCursor)
    while row:
        print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        # Set row equal to the next row in the cursor
        row = next(searchCursor)
except StopIteration:
    print("No more records")
# Delete the cursor to free the data lock
del searchCursor"""

#UpdateCursor() - used to change the value of a row in an input or remove a row entirely from an input
#EX1 - finding feature class GaragePoints, grabbing the values, looping through to search for row that contains Garage as the v alue for field LotType, and changing using an equal sign
"""import arcpy
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
updateCursor = arcpy.da.UpdateCursor(campus + "/GaragePoints", field_names=fields)
# Loop through the cursor looking for the row that contains Garage as a LotType
for row in updateCursor:
    if row[1] == "Garage":
        row[1] = "Garage Visitor"
        updateCursor.updateRow(row)
# Delete the cursor to free the data lock   
del updateCursor"""

#EX2: Calling deleterow() on the updatecursor variable to remove the desired row. (Deleting when LotName equals century square)
"""import arcpy
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/20/Campus.gdb"
# Define the fields we want
fields = ['Name', 'LotType', 'LotName']
# Define our search cursor 
updateCursor = arcpy.da.UpdateCursor(campus + "/GaragePoints", field_names=fields)
# Loop through the cursor looking for the row that contains CENTURY SQUARE as a LotName
for row in updateCursor:
    if row[2] == "CENTURY SQUARE":
        updateCursor.deleteRow()
# Delete the cursor to free the data lock
del updateCursor"""