##Advanced Tool Parameters##
import arcpy
#Advanced Input Parameter Types

#Multivalue - allows your tool to take several values for the same input (ex: create several buffers or clipping several layers)
#EX1 - creating a multivalue input parameter
"""def getparameterinfo(self):
    #Define Parameter Definitions
    param0 = arcpy.Parameter(
        displayName= "Input Features",
        name="in_features",
        datatype="GPFeatureLayer",
        parameterType="Required"
        direction= "Input"
        multiValue = True)
    params = [param0]
    return params"""
#Multivalue parameters complicate the value grab
#If using param0.valueAsText, you will get a semi-colon seperated string containing all the values provided (You will haveto split the string to get actual values)
#EX2 - Seperating different values presented in the multivalue parameter
"""
def execute(self, parameters, messages):
    #The source code of the tool.
    # Iterate through all parameters
    for param in parameters:
        # Set a variable equal to the string value of the current parameter
        paramVal = param.valueAsText
        # Split the variable paramVal on semi-colons; this gives us a list of inputs provided to the multivalue param
        tokens = paramVal.split(";")
        # Iterate through all the inputs in the list (the tokens)
        for token in tokens:
            # Print out each token value
            arcpy.AddMessage(token)
    return
"""

#Value Table - type of input that allows you to specify multiple entries, which can be any standard parameter data types such as feature classes, fields, strings, etc
"""
def getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName ='Input Features',
        name ='in_features',
        datatype ="GPFeatureLayer",
        parameterType ='Required',
        direction ='Input')

    param1 = arcpy.Parameter(
        displayName='Statistics Field(s)',
        name='stat_fields',
        datatype='GPValueTable',
        parameterType='Required',
        direction='Input')

    param1.parameterDependencies = [param0.name]
    param1.columns = [['Field', 'Field'], ['String', 'Statistic Type']]
    param1.filters[1].type = 'ValueList'
    param1.values = [['NAME', 'SUM']]
    param1.filters[1].list = ['SUM', 'MIN', 'MAX', 'STDEV', 'MEAN']
    params = [param0, param1]
    return params

def execute(self, parameters, messages):
    #The source code of the tool
    for param in parameters:
        paramText = param.valueAsText
        tokens = paramText.split(" ")
        layer = tokens[0]
        field = tokens[1]
        stat_field = tokens[2]
    return
"""
#Get values from value table by splitting the parameter value with a single space character. This will return strings: the layer given as input, the field chosen, and the statistical field value selected

#Composite Parameters - a tool parameter that accepts a variety of different data types. These data types are defined as a list and set to the parameters datatype attribute
"""
 def getParameterInfo(self):
        #Define parameter definitions
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype=["GPFeatureLayer", "GPLayer", "GPRasterDataLayer", "GPLong"],
            parameterType="Required",
            direction="Input")
        params = [param0]
        return params

    def execute(self, parameters, messages):
        #The source code of the tool
        for param in parameters:
            # This will print out the value for each parameter, regardless of its datatype
            arcpy.AddMessage(param.valueAsText)
        return
"""
#Composite parameters such as the one above handles a variety of diff inputs without issue

#Derived - these parameters depend on a previous parameter being fulfilled before they activate
"""
def getParameterInfo(self):
    #Define parameter definitions
    param0 = arcpy.Parameter(
        displayName="Input Features",
        name="in_features",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")

    param1 = arcpy.Parameter(
        displayName="Output Features",
        name="out_features",
        datatype="GPFeatureLayer",
        parameterType="Derived",
        direction="Output")

    param1.parameterDependencies = [param0.name]

    params = [param0, param1]
    return params
def execute(self, parameters, messages):
    #The source code of the tool
    for param in parameters:
        arcpy.AddMessage(param.valueAsText)
    return
"""
#Param1 has a parameterType of Derived meaning it is dependent on some other parameter. The next line uses parameterDependencies attribute to set which parameter that param1 is dependent on (param0)
#Getting the value out of a derived parameter is the same as other parameter types (utilize value or valueAsText attributes)

#Default values - in addition to having the user input the value of a parameter, we can als set default values for the convenience of the user based off their env. settings
#To set a default value type, set the parameters value attribute within the getParameterInfo() method
#defaultEnvironmentName  - used for setting the default environment for the parameter, not a default value
#EX1
"""
def getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName="Input Workspace",
        name="in_workspace",
        datatype="DEWorkspace",
        parameterType="Required",
        direction="Input")

    param1 = arcpy.Parameter(
        displayName="Buffer radius",
        name="bufferRadius",
        datatype="GPLong",
        parameterType="Required",
        direction="Input")

    # In the tool's dialog box, the first parameter will show 
    #  the workspace environment's value (if set)
    param0.defaultEnvironmentName = "workspace"

    # The default value for the buffer will be 25.5. This will show every time the tool is run.
    param1.value = 25.5
    params = [param0, param1]
    return params

def execute(self, parameters, messages):
    #The source code of the tool
    for param in parameters:
        arcpy.AddMessage(param.valueAsText)
        
    return
"""
#The user can change the value whenever they run the tool, defaults are supposed to make the tool usage easier and less tedious but can be overridden


#Advanced Filters#

#Value List - useful for providing a set of values that the user can then choose from. Differs from a multiValue in that with a multiValue you are free to select as many options as you want. A value list limits your users options to whatever you have specified in the script
#Ex1
"""
def getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName="Input Features",
        name="in_features",
        datatype="GPLong",
        parameterType="Required",
        direction="Input")

    param0.filter.type = "ValueList"
    param0.filter.list = [10, 20, 40]

    params = [param0]
    return params

def execute(self, parameters, messages):
    #The source code of the tool
    for param in parameters:
        arcpy.AddMessage(param.valueAsText)
        
    return
"""
#to get the value out of a value list style parameter, we access the value or valueAsText attribute of the parameter

#Feature Class - we can use filters to limit the type of feature the user provides in the form of an input layer. Could have a check for situations, but can also use a filter
#EX1
"""
def getParameterInfo(self):
    param0 = arcpy.Parameter(
        displayName="Input Features",
        name="in_features",
        datatype="GPFeatureLayer",
        parameterType="Required",
        direction="Input")
    param0.filter.list = ["Polygon"]
    params = [param0]
    return params

def execute(self, parameters, messages):
    #The source code of the tool
    for param in parameters:
        arcpy.AddMessage(param.valueAsText)
        
    return
""" 
#Set the filter.list attribute of param0 equal to a list that contains those geometry types that will work with the tool. Limits the type of value accepted
#Access parameters value with value or valueAsText attributes

#Categories - a way to organize a large amount of inputs. Collapsible sections are formed, and you only need to set the category attribute on your parameter to a string value
#Parameters with the same value for category will appear in the same section
#EX1
"""
def getParameterInfo(self):
    Define parameter definitions
    param0 = arcpy.Parameter(
        displayName="Input Features",
        name="in_features",
        datatype="GPLong",
        parameterType="Required",
        direction="Input")

    param0.filter.type = "ValueList"
    param0.filter.list = [10, 20, 40]
    param0.category = "Test Tools"
    params = [param0]
    return params

def execute(self, parameters, messages):
    The source code of the tool
    for param in parameters:
        arcpy.AddMessage(param.valueAsText)
        
    return
"""
#categories do not alter parameters in any way so you can use value or valueAsText to access the properties value

##Raster Data## - Arcpy provides libraries of raster processing tools and techniques

#Raster data processing is integral in modern GIS so raster capabilities are found in Core ArcPy Raster Objects, 3D Analyst Toolbox, Spatial Analyst Toolbbox, and more
"""
Raster tasks commonly done in ArcPy:
converting rasters to other things
performing interpolation on raster data sets
creating a variety of output from a raster surface
classifying and reclassifying rasters
applying different types of global, local, and zonal functions
"""

#Raster to ASCII
#EX1
"""
import arcpy
gdb = r"c:\Users\aaron\documents\ArcGIS\Projects\Mod27\Mod27.gdb"
input_raster = gdb + "/tx_dem"
output_file = r"C:/tmp/ArcGISPython/texas_dem_ascii.txt"
arcpy.conversion.RasterToASCII(input_raster, output_file)
"""

#Raster to TIN
#EX1
"""
import arcpy
gdb = r"c:\Users\aaron\documents\ArcGIS\Projects\Mod27\Mod27.gdb"
z_tolerance = 250.3
max_points = 1500000
z_factor = 1
arcpy.ddd.RasterTin(gdb + "/tx_dem", gdb + "/tx_dem_tin", z_tolerance, max_points, z_factor)
"""

#Hillshade
#EX1
"""
import arcpy
gdb = r"c:\Users\aaron\documents\ArcGIS\Projects\Mod27\Mod27.gdb"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(gdb + "/tx_dem", gdb + "/tx_hillshade", azimuth, altitude, shadows, z_factor)
"""

#Slope
#EX1
"""
import arcpy
gdb = r"c:\Users\aaron\documents\ArcGIS\Projects\Mod27\Mod27.gdb"
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(gdb + "/tx_dem", gdb + "/tx_dem_slopes",output_measure, z_factor, method, z_unit)
"""

#Raster Calculator - tools not supported by arcpy

##Model Builder##

#Creating a New Builder - a way to visually create a tool for use in ArcGIS, first step is to create a new toolbox. After, right click on the new toolbox and create a new tool. 
#From here, you can either create a script-based tool as we have already done, or choose a model -> which will add the ModelBuilder toolbar

#Insert button on ModelBuilder toolbar - houses 6 components that make up our models. You can enter select mode and establish relationships between various components
#Tools Component - allows you to drag and drop a typical geoprocessing tool onto the ModelBuilder canvas. Shaped like ovals on the canvas. If the tool has an output, wherever you drag the tool onto the canvas it will also create a result variable shown as the oval component
#Variable Compenent - allows you to define inputs for various tools used in your model. Oval shaped and come in two types: parameters and non-parameters.
    #Parameter variable is simply a vraible that the user can define. You will see these tools and require you to input a layer or a value. Denoted by a large P
    #Non-Parameter variable is a variable that we define the value of within the modelbuilder interface. These are constants; we assign values and cannot be changed by the user

#Use "Save As..." option to save the tool else your changes may not be reflected in teh Catalog or Geoprocesssing panes

#Exporting a model as Python for editing/enhancing - no longer available due to an ESRI update

##Creating Composite Rasters with Arcpy and Creating NDVI Imagery with a Composite Raster###

#Composite Imagery - creating a composite raster that combines all four rasters downloaded on lecture tab
#First import arcpy, then reference our working directory either by setting it as your workspace or by using a simple path string
#After the source is set, create four variables for the four rasters
#sa.Raster() allows us to get a reference to each raster file and set that equal to a variable
"""
import arcpy
source = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/28/LS7/"
band1 = arcpy.sa.Raster(source + "B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "B2.TIF") # green
band3 = arcpy.sa.Raster(source + "B3.TIF") # red
band4 = arcpy.sa.Raster(source + "B4.TIF") # NIR
"""
#Call CompositeBands_management() method to create composite imagery. Takes in two parameters: a list of raster inputs and the output path and name
#ESRI documentation states you need to provide rasters in this order; red, blue, green
"""
import arcpy
source = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/28/LS7/"
band1 = arcpy.sa.Raster(source + "B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "B2.TIF") # green
band3 = arcpy.sa.Raster(source + "B3.TIF") # red
band4 = arcpy.sa.Raster(source + "B4.TIF") # NIR
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "combined.tif")
"""
#Once run, you should get an image with the colors layered in together
#Using the composite imagery, create the NDVI. This is a way of quantifying healthy vegetation using the red and infrared rasters
#Using simple raster math, we can create a raster representing the NDVI, but there are multiple ways to calculate an NDVI through ESRI
"""
ESRI_NDVI = ((IR - R) / (IR + R)) *100 + 100
NDVI = ((IR - R) / (IR +R))
"""
#Rasters can be treated as a single operand in raster arithmetic, so two rasters can be added together using the '+' symbol or other arithmetic symbols
#Create new variables (ESRI_NDVI and NDVI) and apply the formula with what we know about LandSat 7 imagery
#Then use save() method to save the raster, resulting in the a file in the system
"""
esri_ndvi = ((band4 - band3) / (band4 + band3)) * 100 + 100
esri_ndvi.save(source + "esri_ndvi.tif")
ndvi = ((band4 - band3) / (band4 + band3))
ndvi.save(source + "ndvi.tif")
"""