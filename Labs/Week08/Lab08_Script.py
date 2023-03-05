##Version 1##
"""
GEOG 676 ePortfolio - The Industry Problem - Dylan Pouncy

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

Steps:
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

#To Open a file for reading:
file = open('computer\example_file_path.extension,'r')
In this line of code, we assign the file housing the data to the varialbe 'file', use the method 'open()' to open the file, and a second parameter 'r' to establish what we want to do with the file.
The second parameter has many options to utilize and are listed below for reference:
|Parameter Abbreviation | Mode | Function |
|r | read mode | allows you to read contents |
| r+ | read and write mode | does not create a file if doesnt already exist |
| w | write mode | allow you to read and modift the contents of a file |
| w+ | write mode | same as w, but will create a file if it doesnt exist |
| a | append mode | allows you to read and add to the contents of a file |
| a+ | append mode | same as a, but will create a file if it doesnt exist |

#To Read the contents of the file:
contents = file.read()
In this line of code, we assign the data within the file to the variable 'contents', and use the method 'read()' to allow python to store the data into memory.
It is recommended to couple a loop with the readline() method to read large data files in smaller chunks to preserve memory. An example is provided below:
with open('computer\example_file_path.extension,'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
In this script, we are opening a file and assigning it the variable 'file'. We then loop through lines, another variable, in file and read the data line by line. We use 'print()' as a placeholder, but you can replace this with a line of code to manipulate data line by line. Finally, we use 'line = file.readline()' to progress to the next line of data in the file.

#To Close a file:
file.close()
In this line of code, we are interacting with our environment in a way that allows python to close the file in which we scraped data from. It is an important to close files after use to avoid errors and file corruption.

You will replicate this process for all given input datasets until you have succesfully collected all necessary data points.
A link displaying these techniques is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week03/Lab03_Script.py


Step 3 - Data Cleaning and Transformation
In this step, we will look to clean the collected data through standardization, duplication checking, and other techniques applicable. We then will consolidate the cleaned data into a master well location data set for use in the next steps.

It is important to understand the data you are interacting with, so the first step in data cleaning will be to check data types and convert to homogenous data forms for further analysis.
To accomplish this, we will utilize a python library called 'Pandas' which will need to be imported into your environment like below:

import pandas as pd
In this line of code we are importing pandas into our environment and naming is 'pd' as an abbreviation.
Once imported, we will check the datatypes using the method 'df.dtypes', and 'astype()', a pandas method to convert data types to types we desire. An example of this using a CSV is below:

#Import data from a CSV file
df = pd.read_csv('computer\well_locations.csv')

#Check data types of columns
print(df.dtypes)

#Converting a column to an integer type
df['x_coordinate'] = df['x_coordinate'].astype(int)

After our data types are homogenous, the next step in data cleaning would be to address duplicate rows. To do this, you will need to analyze your data and establish a column to determine duplicates. In our hypothetical well location data set, we will use the column 'well_id'.

df.drop_duplicates(subset = 'well_id', keep = 'first', inplace=False)
In this line of code we utilize the pandas method 'drop_duplicates()' to remove duplicates. We pass three parameters into the method:
Parameter 1: 'subset' specifices the columns to use when identifying duplicate rows. The default will use all columns to remove perfect matches, or you can specify a given column as we do.
Parameter 2: 'keep' specifices which duplicate rows to keep. The options are 'first', 'last', or 'false'. False will removes all duplicates
Parameter 3: 'inplace' specifies whether to modify the data set in place or return a new data set with the duplicates removed. True indicates to modify the old data frame, false will create a new data frame
For parameter 3, we will create a new file for the dataset so we do not lose the duplicated data points permanently. We will likely need to use these duplicates for data validation later.

Finally, we will want to save the cleaned data set to a new master well location file using the following script:
df.to_csv('computer\master_well_location', index=False)
The first parameter in the 'df.to_csv()' method specifies the new file path name and location of the file, and the second parameter we use is 'index' and is set to true to include the row index as the first column. False would remove the row index

We will iterate this same technique across all input data sets and combine the outputs into the master well location file. Once completed, we can check for duplicates once more to identify variances in well locations and determine accuracy.
There are many different file types and datatypes that are utilized in python, ArcGIS, and file explorer. It is important to get familiar with the various types.
A link to a lab displaying data manipulation is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week03/Lab03_Script.py

Step 4 - Geodatabase Creation
For step 4, we will be taking the collected and cleaned data and writing the data to a new file to create a geodatabase for use in our ArcGIS project.
There are many types of files that can be housed on your computer, and for this step we will be creating a GeoDataBase (GDB), which utilizes the extension '.gdb'
In this step, you will utilize many arcpy methods such as: 'arcpy.CreateFileGDB_management()', 'arcpy.MakeXYEventLayer_management()', and 'arcpy.Project_management()' among others.

The arcpy library enables you to convert file types into geodatabases for implementation into ArcGIS, and the below example walks through how you could take an example data file and convert it into a GDB.
In our industry problem, we would use the cleaned data output file to create our GDB

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

A link to a lab demonstrating a case use of this in a different format can be found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week04/Week04_Script.py


Step 5 - Building a Buffer
In this step, we will learn how to build buffers and utilize them to filter or categorize input data. Picking up from the last example, we will utilize the previously created geodatabase.

#buffer creation 
WellsBuffered = arcpy.Buffer_analysis(gdb_path + '\Well_Locations_reprojected', gdb_path + '\Well_Locations_buffered', 150)
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
When creating this tool, the data type can be one of hundreds of types. View ArcGIS's website for documentaion on which datatype to select here: https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm
The data type we will need to set the input parameter to is: 'DEImageServer' which allows for an input from an image service provided

A link to a lab in which a custom tool box was created and implemented that allows users to select various layers is found here: https://github.com/dylanpouncy/Pounc_GEOS676/blob/main/Labs/Week07/Lab07_Script.py

"""