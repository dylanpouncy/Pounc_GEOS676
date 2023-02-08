#Building Tools
#Tools will appear inside the geoprocessing pane of ArcGIS Pro like others

#Hanlde User Inputs
import arcpy
arcpy.env.workspace = "C:\Users\Dylan\OneDrive\GEOS_676"

#Define our geodatabase - campus variable holds a ref to the gdb containing our data layers from campus
campus = r"C:\Users\Dylan\OneDrive\GEOS_676_Content_Clone\Content-1\data\modules\17\Campus.gdb"

#Setup our user input variables
buildingNumber_input = input("Please enter a building number: ") #leave as str due to data style
bufferSize_input = int(input("Please enter a buffer size: ")) #cast to an int

#Data Checks:

#Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input #returns values in '/Structures' that match the provided building number

#Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
#searchcursor takes two argumenmts: an input layer and a where clause

#loop to iterate and ensure if we should proceeed - if a row in cursor contains a row who's value for field bldg equals buildingNumber_input then we proceed
for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

#Opearations

#If we shouldProceed, do so
if shouldProceed:
    
 

#Generate the name for our output buffer layer
    buildingBuff = "/buidling_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
#Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)

#Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
#Clip the structures to ou buffered feature
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
#remove the featur class we just created
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input)) #Be careful using, not prompt will warn you and features will be removed w/o question

else:
    print("Seems we couldn't find the building you entered")

######################################################################################################################################################################
#Creating a Python Toolbox with our tool
#tool box - single text file that acts as the glue that groups several individual tools under a single group name

#Parameter Inputs -

#Multivariate - used to handle multiple values
#EX1:
"""ef getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName="Building Number",
        name="buildingNumber",
        datatype="GPString",
        parameterType="Required",
        direction="Input",
        multiValue=True
    )"""

#Filers - used to limit the type of data users will provide an input
#EX1
"""def getParameterInfo(self):
    param1 = arcpy.Parameter(
        displayName="Buffer radius",
        name="bufferRadius",
        datatype="GPDouble",
        parameterType="Required",
        direction="Input"
    )
    param1.filter.type = "Range"
    param1.filter.list = [10, 100]"""