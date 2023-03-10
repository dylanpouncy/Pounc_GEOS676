import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""


        self.tools = [GarageBuildingIntersection]


class GarageBuildingIntersection(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Lab 05 Toolbox"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False #only used in ArcMap
        self.category = "Building Tools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="GDB Folder",
            name="GDBFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="GDB Name",
            name="GDBName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param3 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="GarageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="CampusGDB",
            datatype="DEType",
            parameterType="Required",
            direction="Input"
        )
        param5 = arcpy.Parameter(
            displayName="Buffer Distance",
            name="BufferDistance",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3, param4, param5]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        campus = r"C:\Users\Dylan\OneDrive\GEOS_676_Content_Clone\Content-1\data\modules\17\Campus.gdb"

        # Setup our user input variables
        folder_path = parameters[0].valueAsText
        gdb_name = parameters[1].valueAsText
        gdb_path = folder_path + '\\' + gdb_name
        arcpy.CreateFileGDB_management(folder_path, gdb_name)

        csv_path = parameters[2].valueAsText
        garage_layer_name = parameters[3].valueAsText
        garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

        input_layer = garages
        arcpy.FeatureClassToFeatureClass_conversion(input_layer, gdb_path, garage_layer_name)
        garage_points = gdb_path + '\\' + garage_layer_name

        #Open campus gdb, copy building feature to our gdb
        campus = parameters[4].valueAsText
        buildings_campus = campus + '\Structures'
        buildings = gdb_path + '\\' + 'Buildings'

        arcpy.Copy_management(buildings_campus, buildings)

        #Reprojection
        spatial_ref = arcpy.Describe(buildings_campus, buildings)
        arcpy.Project_management(garage_points, gdb_path + '\Garage_points_reprojected', spatial_ref)

        #buffer garages
        buffer_distance = int(parameters[5].value)
        garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garagae_points_reprojected', gdb_path + '\Garage_Points_buffered')

        #intersect buffer and buildings
        arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection','ALL')

        arcpy.TableToTable_conversion(gdb_path + '\Garage_Builidng_Intersection.dbf', 'C:\\Users\\Dylan\\OneDrive\\GEOS_676')

        return None