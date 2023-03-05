<U>GEOG 676 ePortfolio - The Industry Problem - Dylan Pouncy</U>

Project Overview:
The goal of lab 8 is to culminate the knowledge learned in GIS Programming thrughout the semester and solve a pertinent industry related issue to demonstrate both knowledge of GIS aplications and creativity.

The Industry Problem:
You are asked to build a software tool that builds a Master Well Database from numerous different databases. 
Often companies have several databases of where they think their Wells are located.
These could be from CAD, ArcGIS, Decision Space Geographics, Petrel, OpenWells, COMPASS, Drilling Info, HSI, State Regulatory, etc. 
All these might not agree on the Well location.

Tool Description: 
1. Imports all data opinions of well location
2. Inverses between all the data and writes to a master well location trending position
3. Build a check that determines if the coordinate was NAD83 vs. NAD27
4. Build a tool that allows users to select the master well location from different aerial images

Fundamental Framework Questions:
1. Where will the software development be done - lab 1
2. How to load several data sets to project that represent well locations - lab 3
3. Inverse coordinates of the different well locations to determine accuracy - lab 2
4. Write to master well geodatabase - lab 4
5. Build a buffer to determine if the wells were put in NAD83 vs. NAD27 - lab 5
6. Build a graduated color well to indicate confidence of master well location - lab 6
7. Use aerial images to check master well database - lab 7

Additionnal Asks:
1. Justify the return on investment (ROI)
2. Interface with users
3. Gather requirements
4. Softwares, Databases, etc to be used
5. Code with usages of Numpy, SciPy, PySAL, Moderl Builder, and/or ArcPy
6. Approach commenting, testing, status updates, and reporting
7. Deploy, maintain, and archive your software

Industry Solution Step Overview:
1. Project Preface - Software requirements 
2. Data Collection - collect data from various databases that contains info about well locations. Use API calls, queries, and data connectors
3. Data Cleaning and Transformation - clean the collected data and integrate it into a single dataset. Check for duplicates, standardization, normalization, and validation
4. Geodatabase Creation - Create a geodatabase with accurate data to input into ArcGIS
5. Build Buffers - Create buffers in ArcGIS to determine well input data type
6. Build Graduated Color Layer - create in ArcGIS to indicate confidence of master well locations
7. Aeriel Image Selection Tool - build a tool to allow users to select the master well location from different aerial images
8. Testing and Deploymeny - test the software tool thoroughly and document its instructions and limitations, and deploy the software tool to the required environment


Step 1 - Project Preface 
This project will utilize many various software applications and packages that will need to be downloaded prior to work intiation. For this project, you will need working access and fundamental knowledge of:
1. Python - A powerful open-source programming langauge
2. Python Coding Environment - Although completion can be achieved utilizng a shell prompt, a code editor such as VSCode, Jupyter Notebook, or Atom will aid in the ease of debugging and implementation
3. ArcGIS Pro - A desktop-based geographic information system software utilized for the output of this project
4. Various Python Libraries - Installation and importation of various python libraries will be necessary to ease the completion of the project. These libraries include but are not limited to: ArcPy, NumPy, PySAL, Pandas, and Requests)
5. File Explorer - A software tool used to manage file folders and create new databases for implementation in the project
Additionall, you can download the Github extension into your coding environment and create a GitHub repository for collaboration and error checking amongst peers. This will be done through GitHub's desktop application.
Upon creation of a repository, you can clone the repository using widget in GitHub and begin syncing the repository with scripts and files created in your coding environment
A link to a lab displaying basic python calculations, as well as library importation is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week02/Lab02_Script.py


Step 2 - Data Collection 
The first step in this project will be the gathering of data provided through the various sources. The sources known to supply data to this project can range from the following:
- CAD
- ArcGIS
- Decision Space Geographics
- Petrel
- OpenWells
- COMPASS
- Drilling Info
- HSI
- State Regulatory Data Providers
- Others

There are many methodologies, ranging from API calls, REST/GET, SQL Queries, Data Connectors, and more, that can be utilized to complete this task. The methodology we will use is a data connector through python.
To complete this task, you can import libraries into you python environment to support the data reading. However, many methods native to python's base package can be utilized without importing any additional libraries.
The following documentation will assist in opening, reading, and closing files housing well location data.

```python
#To Open a file for reading:
file = open('computer\example_file_path.extension,'r')
```

In this line of code, we assign the file housing the data to the varialbe 'file', use the method 'open()' to open the file, and a second parameter 'r' to establish what we want to do with the file.

The second parameter has many options to utilize and are listed below for reference:

|Parameter Abbreviation | Mode | Function |
|:-------:|:----:|:-------:|
|r | read mode | allows you to read contents |
| r+ | read and write mode | does not create a file if doesnt already exist |
| w | write mode | allow you to read and modift the contents of a file |
| w+ | write mode | same as w, but will create a file if it doesnt exist |
| a | append mode | allows you to read and add to the contents of a file |
| a+ | append mode | same as a, but will create a file if it doesnt exist |

```python
#To Read the contents of the file:
contents = file.read()
```

In this line of code, we assign the data within the file to the variable 'contents', and use the method 'read()' to allow python to store the data into memory.
It is recommended to couple a loop with the readline() method to read large data files in smaller chunks to preserve memory. 
An example is provided below:

```python
with open('computer\example_file_path.extension,'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
```

In this script, we are opening a file and assigning it the variable 'file'. We then loop through lines, another variable, in file and read the data line by line. We use 'print()' as a placeholder, but you can replace this with a line of code to manipulate data line by line. Finally, we use 'line = file.readline()' to progress to the next line of data in the file.

```python
#To Close a file:
file.close()
```

In this line of code, we are interacting with our environment in a way that allows python to close the file in which we scraped data from. It is an important to close files after use to avoid errors and file corruption.

You will replicate this process for all given input datasets until you have succesfully collected all necessary data points.
A link displaying these techniques is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week03/Lab03_Script.py


Step 3 - Data Cleaning and Transformation
In this step, we will look to clean the collected data through standardization, duplication checking, and other techniques applicable. We then will consolidate the cleaned data into a master well location data set for use in the next steps.

It is important to understand the data you are interacting with, so the first step in data cleaning will be to check data types and convert to homogenous data forms for further analysis.
To accomplish this, we will utilize a python library called 'Pandas' which will need to be imported into your environment like below:

```python
import pandas as pd
```

In this line of code we are importing pandas into our environment and naming is 'pd' as an abbreviation.
Once imported, we will check the datatypes using the method 'df.dtypes', and 'astype()', a pandas method to convert data types to types we desire. An example of this using a CSV is below:

```python
#Import data from a CSV file

df = pd.read_csv('computer\well_locations.csv')

#Check data types of columns

print(df.dtypes)

#Converting a column to an integer type

df['x_coordinate'] = df['x_coordinate'].astype(int)


#After our data types are homogenous, the next step in data cleaning would be to address duplicate rows. To do this, you will need to analyze your data and establish a column to determine duplicates. In our hypothetical well location data set, we will use the column 'well_id'.

df.drop_duplicates(subset = 'well_id', keep = 'first', inplace=False)

#In this line of code we utilize the pandas method 'drop_duplicates()' to remove duplicates. We pass three parameters into the method:
#Parameter 1: 'subset' specifices the columns to use when identifying duplicate rows. The default will use all columns to remove perfect matches, or you can specify a given column as we do.
#Parameter 2: 'keep' specifices which duplicate rows to keep. The options are 'first', 'last', or 'false'. False will removes all duplicates
#Parameter 3: 'inplace' specifies whether to modify the data set in place or return a new data set with the duplicates removed. True indicates to modify the old data frame, false will create a new data frame
#For parameter 3, we will create a new file for the dataset so we do not lose the duplicated data points permanently. We will likely need to use these duplicates for data validation later.

#Finally, we will want to save the cleaned data set to a new master well location file using the following script:
df.to_csv('computer\master_well_location', index=False)
#The first parameter in the 'df.to_csv()' method specifies the new file path name and location of the file, and the second parameter we use is 'index' and is set to true to include the row index as the first column. False would remove the row index
```

We will iterate this same technique across all input data sets and combine the outputs into the master well location file. Once completed, we can check for duplicates once more to identify variances in well locations and determine accuracy.
There are many different file types and datatypes that are utilized in python, ArcGIS, and file explorer. It is important to get familiar with the various types.

A link to a lab displaying data manipulation is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week03/Lab03_Script.py

Step 4 - Geodatabase Creation
For step 4, we will be taking the collected and cleaned data and writing the data to a new file to create a geodatabase for use in our ArcGIS project.
There are many types of files that can be housed on your computer, and for this step we will be creating a GeoDataBase (GDB), which utilizes the extension '.gdb'
In this step, you will utilize many arcpy methods such as: 'arcpy.CreateFileGDB_management()', 'arcpy.MakeXYEventLayer_management()', and 'arcpy.Project_management()' among others.

The arcpy library enables you to convert file types into geodatabases for implementation into ArcGIS, and the below example walks through how you could take an example data file and convert it into a GDB.
In our industry problem, we would use the cleaned data output file to create our GDB

```python
import arcpy

arcpy.env.workspace = r'C:\\Users\\OneDr\\Master_Well_Locations\\Databasecreation' #Here we are establishing a python environment to work in
folder_path = r'C:\\Users\\OneDr\\Master_Well_Locations' #We have selected the folder path in which the database will be created from
gdb_name = 'Master_Well_Location.gdb' #Establishing a name for our new GDB, in the form of a string
gdb_path = folder_path + '\\' + gdb_name #Establishing the file path for our future GDB
arcpy.CreateFileGDB_management(folder_path, gdb_name, overwrite_existing=True) - #This arcpy method is used to create a GDB using the given input parameters. We utilize 'overwrite_existing=True' to overwrite an existing file, if present, to prevent 'ERROR 000258'
arcpy.CreateFileGDB_management(folder_path, gdb_name) #The method to create the new GDB

csv_path = r'C:\\Users\\OneDr\\Master_Well_Locations.csv' #Linking the cleaned and collected input data file for use in GDB creation
Well_Locations = 'Well Coordinates' #Establishing a variable for the well coordinates in the data
Wells = arcpy.MakeXYEventLayer_management(csv_path, 'X','Y', Well_Locations) #Utilizing arcpy method 'MakeXYEventLayer_management()', we create a layer within our GDB that contains well location coordinates

input_layer = Wells #Creating a variables for our wells
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path) #We are now converting our feature class layer into a geodatabase using arcpy method 'FeatureClassToGeodatabase_conversion()'
Well_Locations_Points = gdb_path + '\\' + well_layer_name #We are now creating a new file for use later that houses our well location data

spatial_ref = arcpy.Describe(wells).spatialReference #We now are reprojecting our wells using spatial reference methods within arcpy
arcpy.Project_management(input_layer, gdb_path + '\Well_Locations_Reprojected', spatial_ref) #Updating the project to reflect the spatial references
arcpy.Project_management(Well_Locations_Points, gdb_path + '\Well_Locations_reprojected', spatial_ref) #Creating a file to reflect the updates
```

A link to a lab demonstrating a case use of this in a different format can be found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week04/Week04_Script.py


Step 5 - Building a Buffer
In this step, we will learn how to build buffers and utilize them to filter or categorize input data. Picking up from the last example, we will utilize the previously created geodatabase.

```python
#buffer creation 
WellsBuffered = arcpy.Buffer_analysis(gdb_path + '\Well_Locations_reprojected', gdb_path + '\Well_Locations_buffered', 150)
```
In this arcpy method 'Buffer_analysis()', we can create buffers tailored to our desire. You must pass in 3 required parameters, with the option to pass in many more optional parameters:
1. Parameter 1 (Required): 'in_features' parameter specifies the input features that will be buffered. They can be either a feature class or a feature layer
2. Parameter 2 (Required): 'out_feature_class' parameter specifies the output feature class that will contain the buffered features. This can be a shapefile or GDB feature class
3. Parameter 3 (Required): 'buffer_distance_or_field' parameter specifies the distance or field used to calculate the buffer distance. Must be numeric and linear
There are many other optional parameters that can be passed through to further specify your buffer.
In our code, we are passing previously created feature class files into the method

A link to a lab displaying buffer analysis further can be found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week05/Lab05_Script.py


Step 6 - Building a Graduated Color Renderer
ArcGIS offers several methods for defining ranges and colors used in renderers, as well as many different types. These are used to display quantitative data and visually represent data by varying the color of the symbol based on data values associated with a feature class.
In this example, we will use the count of equivalent well locations as the guage to well location confidence, meaning well locations verified across various data sources will have a higer level of confidence, and therefore a different color scheme.
For this project we will build a graduated color but ArcGIS offers a range of renderers from Simple to Unique Value renderers. The following code can demonstrate how to build a graduated color renderer

```python
import arcpy #you will need to import the arcpy library into your environment

project = arcpy.mp.ArcGISProject(r"C:/OneDr/Master_Well_Locations/" + r"GDB\\.aprx") #Create a variable to establish a link to your ongoing project
Well_Locations = project.listMaps('Map')[0] #Grab the first map in the .aprx

#Create a loop to iterate through available layers in the map
for layer in Well_Locations.listLayers():
    # Check if layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Check if it has a 'renderer' attribute
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is 'Well_Coordinates'
            if layer.name == "Well_Coordinates":
                # Update the copy's renderer to be 'GraduatedColorsRenderer'
                symbology.updateRenderer('GraduatedColorsRenderer')
                # Tell arcpy which field we want to base our choropleth off of
                symbology.renderer.classificationField = "Shape_Area"
                # Set how many classes we'll have 
                symbology.renderer.breakCount = 5
                # Set the color ramp
                symbology.renderer.colorRamp = project.listColorRamps('Blues (5 Classes)')[0]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology 
            else:
                print("NOT WellLocation")
project.saveACopy(r"C:/OneDr/Master_Well_Locations/" + r"GDBv.2\\.aprx")
```

We will utilize many arcpy methods as well as iteration techniques in this step. The following reference material will help clarify:
A link to a lab showing renderer building can be found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week06/Lab06_Script.py
A link to module notes explaining loops and iteration can be found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/ModuleNotes/Module2Notes.py


Step 7 - Using Aerial Images to Check Master Well Database
In this step we will build a custom tool in ArcGIS to allow the user to select the Master Well Location from different aerial images.
To do this, you will need to create a custom tool within ArcGIS, which can be done either through the desktop application or imported from python via Custom Python Toolbox
To navigate and create a new custom python toolbox in ArcGIS, follow these steps:

1. Navigate to the contents pane
2. Right click the toolboxes icon
3. Select 'New Python Toolbox'
4. Select the file path in which you would like to save the toolbox

From there, you have the ability to open the file within your code editor of choice and begin creating your custom tool. This tool will have a data input required from users that allows them to elect an aerial image of choice to view the master well locations
When creating this tool, the data type can be one of hundreds of types. 
View ArcGIS's website for documentaion on which datatype to select here: https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

A link to a lab in which a custom tool box was created and implemented that allows users to select various layers is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week07/Lab07_Script.py


Tool Creation - For this project, a custom tool should be created to accomplish the goals of the industry problem. This tool should do the following:

1. Import all data opinions of well data
2. Inverse between all the data and write to master well location trending position
3. Build a check that determines if the coordinates were NAD83 or NAD27
4. Allow the user to select the master well location from different aerial images

To do this, you will need to navigate to the custom python toolbox previously created in step 7. Navigate to the "Add > Tool" button to create a new tool.
From here, in the dialog boxes you can name your tool, specify the input parameters, and specify the output parameters of your tool. You can then move the python tool box file (.pyt extension) to your code editor to begin writing the tool script.

See the below code to assist in creating the oil well location importation tool:
```python
import arcpy

#Specify the input and output data sources
input_csv = r"C:\data\wells.csv"
output_fc = r"C:\data\master_wells.gdb\WellLocations"

#Read the well location data from the input CSV file
fields = ["WellID", "X", "Y"]
data = [row for row in arcpy.da.SearchCursor(input_csv, fields)]

#Write the data to the output feature class
arcpy.management.CreateFeatureclass(
    arcpy.env.workspace,
    "WellLocations",
    "POINT",
    spatial_reference=arcpy.SpatialReference(4269)
)
with arcpy.da.InsertCursor(output_fc, fields) as cursor:
    for row in data:
        cursor.insertRow(row)
```

See the below code to assist in implementing the coordinate system check tool:

```python
import arcpy

#Specify the input feature class
input_fc = r"C:\data\master_wells.gdb\WellLocations"

#Get the spatial reference of the input feature class
desc = arcpy.Describe(input_fc)
sr = desc.spatialReference

#Check if the spatial reference is NAD83 or NAD27
if sr.name == "NAD_1983":
    print("The well locations are in NAD83")
elif sr.name == "NAD_1927":
    print("The well locations are in NAD27")
else:
    print("The well locations are in an unknown coordinate system")
```

See the below code to assist in implementing the master well location selection tool:

```python
import arcpy

class SelectMasterWellLocation(object):
    def __init__(self):
        self.label = "Select Master Well Location"
        self.description = "Allows the user to select the master well location from different aerial images."
        self.category = "Oil Well Location Toolbox"

    def getParameterInfo(self):
        #Define the input and output parameters
        params = []
        
        #Parameter 1: Input well location feature class
        param = arcpy.Parameter(
            displayName="Input Well Location Feature Class",
            name="input_fc",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input"
        )
        params.append(param)
        
        #Parameter 2: Aerial images directory
        param = arcpy.Parameter(
            displayName="Aerial Images Directory",
            name="images_dir",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        params.append(param)
        
        #Parameter 3: Output well location feature class
        param = arcpy.Parameter(
            displayName="Output Well Location Feature Class",
            name="output_fc",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )
        params.append(param)
        
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        #Get the input and output parameters
        input_fc = parameters[0].valueAsText
        images_dir = parameters[1].valueAsText
        output_fc = parameters[2].valueAsText
        
        #Get a list of all the aerial image files in the directory
        image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]
        
        #Add the aerial images to the map
        mxd = arcpy.mapping.MapDocument("CURRENT")
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        for image_file in image_files:
            image_path = os.path.join(images_dir, image_file)
            image_layer = arcpy.mapping.Layer(image_path)
            arcpy.mapping.AddLayer(df, image_layer)
        
        #Add the well location data to the map
        well_layer = arcpy.mapping.Layer(input_fc)
        arcpy.mapping.AddLayer(df, well_layer)
        
        #Allow the user to select the master well location from the map
        arcpy.AddMessage("Please select the master well location from the map.")
        master_location = arcpy.PointGeometry(arcpy.GetParameterAsText(0))
        
        #Create a new feature class with only the selected master well location
        arcpy.management.CreateFeatureclass(
            arcpy.env.workspace,
            arcpy.Describe(input_fc).name,
            "POINT",
            spatial_reference=arcpy.SpatialReference(4269)
        )
        fields = ["WellID", "X", "Y"]
        with arcpy.da.InsertCursor(output_fc, fields) as cursor:
            cursor.insertRow([1, master_location.centroid.X, master_location.centroid.Y])
        
        #Remove the temporary layers from the map
        arcpy.mapping.RemoveLayer(df, well_layer)
        for image_layer in arcpy.mapping.ListLayers(df):
            arcpy.mapping.RemoveLayer(df, image_layer)
        
        #Refresh the map
        arcpy.RefreshActiveView()
        arcpy.AddMessage("Master well location selected and written to output feature class.")
```

Additional Requirements - 

1. Justify the Return on Investment (ROI): This industry problem will have the given solution discussed which can be quantified from a return on investment (ROI) perspective. Businesses use this metric to justify their resource expenditures on worthy projects that warrant a sufficient return on resources expended.
The cost of software utilized by the in-house software development team and salaries of software developers will be considered a sunk cost, and therefore not attributable to the ROI of this project.
A generalized estimate of the ROI of this project will be 15%. The time and labor capital directed towards this project will have an opportunity cost upfront, but should be positive in later endeavors as the tools created will be archived and used throughout business operations into the future.
The ROI of this project will be lower than what might be expected as this tool is under construction and will need periodical review to ensure its accuracy and capabilities. Assuming it takes a team of 2 software developers two days to create the tool and two days per quarter to maintain the effectiveness of the tools, the ROI can be estimated to be 15%.
The creation of a master well location database that is accessible to all business units will pay dividends into perpetuity for the firm in the form of automated workflow and error reduction.

2. Interface with Users: Users will be able to interact with the final product in a multitude of ways. Accessing the master well location database, assuming it is saved and accessible company-wide, can be done using excel, SQL, Snowflake, API Keys, and other data querying methods.
The ArcGIS tool and maps will be accessible to users on the company subscription for use and manipulation as the differing business units see fit.

3. Gather Requirements: The final products that serve to solve the problem presented should be rolled out to a limited number of users across the firm. The users should intentionally stress the capabilities of the tools to ensure accuracy and test features.
Initial users should document errors, short comings, and other features desired for documentation and review. The software development team should then review the suggestions, implement suggestions, and fix any errors.
The limitations and requirements users should test for are software requirements, authorization access barriers, flexibility of inputs, desired output capabilities, and sharability of the tools.

4. Softwares, DB's, etc that will be used: Although previously mentioned, the requirements for this project from a creation and usage perspective are:
4.1. A Working Computer
4.2. Python
4.3. Python Coding Environment
4.4. Various Python Libraries
4.5. ArcGIS Desktop Software
4.6 Query Capabilites (SQL, Data Connectors, etc)
4.7 File Explorer
4.8 Data Sources

5. Code with usages of Numpy, Model Builder, Arcpy, etc: The script, process flow, and implementation of code and the software used is listed throughout the "steps" of the industry problem

6. Approach commenting, testing, status updates, and reporting: Periodic review and updates will likely need to be completed on the software and tools created. Input from users should be encouraged and expanded upon to ensure capabilities reflect the goals of the tools.
Testing of the software should be done initially before rolling out the tools company-wide, and periodic testing should be done to ensure accuracy.

7. Deploy, maintain, and archive your software: Saving all of the ouputs, including coding scripts, master well databases, and ArcGIS custom maps should be done in robust files tailored to the users preference.
Maintanence of the tools can be acheived through building out error-debugging code, AddMessage() methods, and input filters to ensure proper use of tools and databases.