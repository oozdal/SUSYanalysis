projectname = "examplemodel"

#########################################################

execfile("/Users/oozdal/readclass/packages.py")
execfile("/Users/oozdal/readclass/functions.py")
execfile("/Users/oozdal/ExpDATA/ExDATA.py")
execfile("/Users/oozdal/readclass/classes.py")

########################################################

examplemodel = createproject()

########################################################

#neutLHC=parameterset("neutralinolsp.dat")

neutrelic=parameterset("neutralinorelic.dat")

#sneutrinoLHC=parameterset("sneutrinolsp.dat")

#sneutrinorelic=parameterset("sneutrinorelic.dat")

########################################################

BBRlike = BBRlikecontent(neutrelic)

#HRlike = HRlikecontent()
#HRlike.dataload(neutrelic)
