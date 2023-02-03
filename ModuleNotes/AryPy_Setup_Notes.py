#Import ESRI's array of GIS tools and operations within python
import arcpy
#See what all our environment entails
#print(arcypy.ListEnvironments())

#set workspace directory by editing our environment - location inputs are taken and outputs are placed when running tools
arcpy.env.workspace = "C:\Users\Dylan\OneDrive\GEOS_676"

#set scratch workspace - tool outputs are placed if the default name is used, intended for output data you do not wish to maintain
arcpy.env.scratchWorkspace = "C:\Users\Dylan\OneDrive\GEOS_676\Scratch"

#Creating a geodatabase - function takes in two parameters: the path we want to create our .gdb and the name of the geodatabase
folder_path = "C:\Users\Dylan\OneDrive\GEOS_676"
arcpy.CreateFileGDB_management(folder_path, "Test.gdb")


#Basic Operations
