#-------------------------------------------------------------------------------
# Name: Billians.py
# Author: Philip
# Date Modified: 02/11/2016
# Notes: This python script is written in 2.7.8
# Download Billians CSV from Website.
# Uses ArcPy to convert CSV into Point Feature class in GeoDatabase
#-------------------------------------------------------------------------------

import arcpy, os, time, shutil

workspace1 = arcpy.env.workspace = 'X:\\GIS\\GIS_Projects\\_Updates\\Billians\\monthlyDownloads'
workspace = arcpy.env.workspace = 'Y:\\Data_Files\\Dynamic\\Billians\\HealthInfrastructure'

arcpy.env.overwriteOutput = True

# CSV file name that Feature Class will be created from
# the double \\ is needed because there are literals in the csv files
hospitalCSV = workspace + '\\hospital.csv'
bloodbankCSV = workspace + '\\bloodbank.csv'
burncenterCSV = workspace + '\\burncenter.csv'
nursinghomeCSV = workspace + '\\nursinghome.csv'
traumacenterCSV = workspace + '\\traumacenter.csv'

# Output Name into GDB
hospitalOut = 'hospital'
bloodbankOut = 'bloodbank'
burncenterOut = 'burncenter'
nursinghomeOut = 'nursinghome'
traumacenterOut = 'traumacenter'

# Output location of feature Class
outputLOC = 'X:\\GIS\\GIS_Projects\\_Updates\\Billians\\Billians.gdb'

# Projection file Feature Class is based from
sr = arcpy.SpatialReference(4326)

try:
    print "Running Hospitals"
    if os.path.exists(hospitalCSV):
        # Creates a Temporary Feature
        arcpy.MakeXYEventLayer_management(hospitalCSV, 'Longitude', 'Latitude', hospitalOut, sr)
        print "Temp Feature Complete"
        # Copies the temp feature and outputs to Geodatabase with FeatureClass Name
        arcpy.CopyFeatures_management(hospitalOut, outputLOC + '\\hospital')
        print 'Completed Hospitals'
    else:
        print "Wrong name"

    print "Running Blood Banks"
    if os.path.exists(bloodbankCSV):
        # Creates a Temporary Feature
        arcpy.MakeXYEventLayer_management(bloodbankCSV, 'Longitude', 'Latitude', bloodbankOut, sr)
        print "Temp Feature Complete"
        # Copies the temp feature and outputs to Geodatabase with FeatureClass Name
        arcpy.CopyFeatures_management(bloodbankOut, outputLOC + '\\bloodbank')
        print 'Completed Blood Banks'
    else:
        print "Wrong name"

    print "Running Burn Centers"
    if os.path.exists(burncenterCSV):
        # Creates a Temporary Feature
        arcpy.MakeXYEventLayer_management(burncenterCSV, 'Longitude', 'Latitude', burncenterOut, sr)
        print "Temp Feature Complete"
        # Copies the temp feature and outputs to Geodatabase with FeatureClass Name
        arcpy.CopyFeatures_management(burncenterOut, outputLOC + '\\burncenter')
        print 'Completed Burn Centers'
    else:
        print "Wrong name"

    print "Running Nursing Homes"
    if os.path.exists(nursinghomeCSV):
        # Creates a Temporary Feature
        arcpy.MakeXYEventLayer_management(nursinghomeCSV, 'Longitude', 'Latitude', nursinghomeOut, sr)
        print "Temp Feature Complete"
        # Copies the temp feature and outputs to Geodatabase with FeatureClass Name
        arcpy.CopyFeatures_management(nursinghomeOut, outputLOC + '\\nursinghome')
        print 'Completed Nursing Homes'
    else:
       print "Wrong name"

    print "Running Trauma Centers"
    if os.path.exists(traumacenterCSV):
        # Creates a Temporary Feature
        arcpy.MakeXYEventLayer_management(traumacenterCSV, 'Longitude', 'Latitude', traumacenterOut, sr)
        print "Temp Feature Complete"
        # Copies the temp feature and outputs to Geodatabase with FeatureClass Name
        arcpy.CopyFeatures_management(traumacenterOut, outputLOC + '\\traumacenter')
        print 'Completed Trauma Centers'
    else:
        print "Wrong name"
except Exception as err:
    print(err.args[0])

print "Feature Classes Finished"

# Time that displays the current Year and Month
time = time.strftime('%Y_%m')

# Makes the directory the CSV file location
os.chdir('X:\\GIS\\GIS_Projects\\_Updates\\Billians\\monthlyDownloads')

# Takes the downloaded CSV file
hospitalFile = 'hospital.csv'
bloodbankFile = 'bloodbank.csv'
burncenterFile = 'burncenter.csv'
nursinghomeFile = 'nursinghome.csv'
traumacenterFile = 'traumacenter.csv'

# Downloads Archive Location
archive = 'X:\\GIS\\GIS_Projects\\_Updates\\Billians\\archive\\csv'

hospitalArchive = (archive + '\\hospital_%s.csv' %time)
bloodbankArchive = (archive + '\\bloodbank_%s.csv' %time)
burncenterArchive = (archive + '\\burncenter_%s.csv' %time)
nursinghomeArchive = (archive + '\\nursinghome_%s.csv' %time)
traumacenterArchive = (archive + '\\traumacenter_%s.csv' %time)

try:
    shutil.copyfile(hospitalFile, hospitalArchive)
    print 'Hospitals archived'
    shutil.copyfile(bloodbankFile, bloodbankArchive)
    print 'Blood Banks archived'
    shutil.copyfile(burncenterFile, burncenterArchive)
    print 'Burn Centers archived'
    shutil.copyfile(nursinghomeFile, nursinghomeArchive)
    print 'Nursing Homes archived'
    shutil.copyfile(traumacenterFile, traumacenterArchive)
    print 'Trauma Centers archived'

except ValueError, Argument:
    print "The error occured \n", Argument

# except Exception as er:
#   print (er.arg[0])

