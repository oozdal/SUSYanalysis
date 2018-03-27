projectname = "NonunigauginomchiBLR"

########################################################

execfile("/Users/oozdal/readclass/packages.py")
execfile("/Users/oozdal/projects/" +  projectname + "/filepaths.py")
execfile("/Users/oozdal/ExpDATA/ExDATA.py")
execfile("/Users/oozdal/readclass/classes.py")

########################################################

SM = Standard_Model()

#######################################################

#neutLHC=parameterset("neutralinolsp.dat")
#neutLHC.Create_mchi1_Content()

#neutrelic=parameterset("neutralinorelic.dat")
#neutrelic.Create_mchi1_Content()

sneutrinoLHC=parameterset("sneutrinolsp.dat")
sneutrinoLHC.CreateSv1Content()

sneutrinorelic=parameterset("sneutrinorelic.dat")
sneutrinorelic.CreateSv1Content()
#sneutrinorelic.xSectionSignalStrength()
########################################################

execfile("makegraph.py")
