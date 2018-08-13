from classSLHAtoMG import *

#######################################################################

SLHAfilePath = "/Users/oozdal/hepwork/SPheno-3.3.8/LRSM_Outputs"
FullCardsPath = "/Users/oozdal/hepwork/MG5_aMC_v2_6_0/WrightExclusion/Cards/param_card.dat"
MGrunFile = "/Users/oozdal/hepwork/MG5_aMC_v2_6_0/runWrightExclusion"
newMGrunFile = "/Users/oozdal/hepwork/MG5_aMC_v2_6_0/runWrightExclusion_new"

########################################################################

newSLHA = CopySLHAtoMG()

for i in range(0,75):
    FullSLHAfilePath = SLHAfilePath + "/LRSM." + str(i)
    if newSLHA.CheckSLHA(FullSLHAfilePath) == True:
        try:
            newSLHA.CopySLHAtoCards(FullSLHAfilePath,FullCardsPath)
            with open(MGrunFile, 'r') as file:
                newSLHA.filedata = file.read()

                newSLHA.filedata = newSLHA.filedata.replace("variable", "LRSM."+str(i))
            
            with open(newMGrunFile, 'w') as newfile:
                newfile.write(newSLHA.filedata)
            
            os.system("./../../hepwork/MG5_aMC_v2_6_0/bin/mg5_aMC ../../hepwork/MG5_aMC_v2_6_0/runWrightExclusion_new")

        except:
            print "This is an error message!"
    else:
        continue
