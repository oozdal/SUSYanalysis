projectname = "examplemodel"

#########################################################

execfile("/Users/oozdal/readclass/packages.py")
execfile("/Users/oozdal/readclass/functions.py")
execfile("/Users/oozdal/ExpDATA/ExDATA.py")
execfile("/Users/oozdal/readclass/classes.py")

########################################################

examplemodel = createproject()

########################################################

neutLHC=parameterset("neutralinolsp.dat")
neutLHC.Create_mchi1_Content()


neutrelic=parameterset("neutralinorelic.dat")
neutrelic.Create_mchi1_Content()

sneutrinoLHC=parameterset("sneutrinolsp.dat")
sneutrinoLHC.CreateSv1Content()

#sneutrinorelic=parameterset("sneutrinorelic.dat")

########################################################

#relicBBRlike = BBRlikeContent(neutrelic)
#relicHRlike = HRlikeContent(neutrelic)
#relicWinolike = WlikeContent(neutrelic)
#relicMixedNeut = MixedContent(neutrelic)
