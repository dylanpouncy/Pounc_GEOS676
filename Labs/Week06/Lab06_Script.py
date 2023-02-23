"""
# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox" 
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]

#below are the 6 methods that need to be completed
class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "GraduatedColor" #Toolbox name that is displayed
        self.description = "create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools" #heirarchy

    def getParameterInfo(self):
        """Define parameter definitions"""
        #original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name", #name you will see in arcgis pro
            name="aprxInputName", #wont be displayed once imported to arcgis
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        
        #which layer you want to classify to create a color map
        param1 = arcpy.Parameter(
            displayName="Layer to Classify",
            name="LayertoClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )

        #output folder location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputProjectName",
            datatype="DEFolder",
            direction="Input"
        )

        #output project name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        params = [param0,param1,param2,param3]
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

    def execute(self, parameters, messages): #does the geoprocessing tasks
        """The source code of the tool."""
        readTime = 2.5 #time for users to read the progress
        start = 0 #beginning position of progressor
        max = 100 #end position
        step = 33 #the progress interval to move the progessor along

        #setup progressor
        arcpy.SetProgressor("step","Validating Project File...",start,max,step)
        time.sleep(readTime) #pause the execution for 2.5 sec, built-in python method
        #add message to the results pane
        arcpy.AddMessage("Validating Project File...")

        #Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueastext)

        #grabs the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0] #User navigates to the specified folder

        #increment progressor
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        #Loop through the layers of the map
        for layer in campus.listLayers():
            #check if the layer is a feature layer
            if layer.isFeatureLayer:
                #copy the layer symbology
                symbology = layer.symbology
                #make sure the symbology has renderer attribute
                if hasattr(symbology, 'renderer'):
                    #check layer name
                    if layer.name == parameters[1].valueastext: #check if the layer name matches the input

                        #increment progressor
                        arcpy.SetProgressorPosition(start + step) #now tool is 33% complete
                        arcpy.SetProgressorLabel("Calculating and Classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and Classifying...")

                        #Update the Copy's Renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        #Tell arcpy which field we want to base our chloropeth off of
                        symbology.renderer.classificationField = "Shape_Area"

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #tool is now 66% complete
                        arcpy.SetProgressorLabel("Cleaning Up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning Up...")

                        #set how many classes for map
                        symbology.renderer.breakCount = 5

                        #Set Color Ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        #set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("No Layers Found")
                        
        #Increment Progressor
        arcpy.SetProgressorPosition(start + step*3) #tool is now 99% complete
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        #param 2 is the folder location and param 3 is the name of the new project
                    
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

"""