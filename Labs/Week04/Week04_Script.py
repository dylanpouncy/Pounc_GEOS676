
#Creating GDB and features
import arcpy

arcpy.env.workspace = r'C:\\Users\\Dylan\\OneDrive\\GEOS_676\\Lab04_wks'
folder_path = r'C:\\Users\\Dylan\\OneDrive\\GEOS_676'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
#arcpy.CreateFileGDB_management(folder_path, gdb_name, overwrite_existing=True) - utilize to overwrite existing file, if present, to prevent 'ERROR 000258'
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'C:\\Users\\Dylan\\OneDrive\\GEOS_676_Content_Clone\\Content-1\\data\\homework\\04\\garages.csv'
garage_layer_name = 'Garage Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X','Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

#Opening campus gdb, copy building feature to our gdb
campus = r'C:\\Users\\Dylan\\OneDrive\\GEOS_676_Content_Clone\\Content-1\\data\\homework\\04\\Campus.gdb'
building_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(building_campus, buildings)

#Reprojection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(input_layer, gdb_path + '\Garage_Points_reprojected', spatial_ref)
#arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

#buffer the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

#intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection','ALL')

arcpy.TableToTable_conversion(gdb_path + '\\Garage_Building_Intersection.dbf', 'C:\\Users\\Dylan\\OneDrive\\GEOS_676', 'nearbyBuildings.csv')