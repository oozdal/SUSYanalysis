import pyslha
import os
import shutil

class CreateNewSLHA():
    def __init__(self):

        pass

    def readSLHA(self,ordering):
        SLHA = pyslha.read( SLHAfilesPath + str(order))

        self.m0              = SLHA.blocks["MINPAR"][1]
        self.m12             = SLHA.blocks["MINPAR"][2]
        self.SignumMu        = SLHA.blocks["MINPAR"][4]
        self.Azero           = SLHA.blocks["MINPAR"][5]
        self.TanBeta         = SLHA.blocks["MINPAR"][7]
        self.TanBetaR        = SLHA.blocks["MINPAR"][9]
        self.mARinput        = SLHA.blocks["MINPAR"][10]
        self.vR              = SLHA.blocks["MINPAR"][11]
        self.MuRinput        = SLHA.blocks["MINPAR"][12]
        self.mBino           = SLHA.blocks["MINPAR"][13]
        self.mBinop          = SLHA.blocks["MINPAR"][14]
        self.mGluino         = SLHA.blocks["MINPAR"][15]

        self.Yv11            = SLHA.blocks["YV"][1,1]
        self.Yv22            = SLHA.blocks["YV"][2,2]
        self.Yv33            = SLHA.blocks["YV"][3,3]

        self.Ys11            = SLHA.blocks["YS"][1,1]
        self.Ys22            = SLHA.blocks["YS"][2,2]
        self.Ys33            = SLHA.blocks["YS"][3,3]

    def AssignValues(self, LesHouchesFile, NewLesHouchesFile):
        with open(LesHouchesFile, 'r') as file:
            self.filedata = file.read()

        # Replace the target string
        self.filedata = self.filedata.replace('m0input', str("{:.6E}".format(self.m0)))
        self.filedata = self.filedata.replace('mhfinput', str('%.6E' % self.m12))
        self.filedata = self.filedata.replace('SGNmuinput', str("{:6E}".format(self.SignumMu)))
        self.filedata = self.filedata.replace('A0input', str('%.6E' % self.Azero))
        self.filedata = self.filedata.replace('tanbinput', str('%.6E' % self.TanBeta))
        self.filedata = self.filedata.replace('tanbRinput', str('%.6E' % self.TanBetaR))
        self.filedata = self.filedata.replace('mARinput', str('%.6E' % self.mARinput))
        self.filedata = self.filedata.replace('vevRinput', str('%.6E' % self.vR))
        self.filedata = self.filedata.replace('SGNmuRinput', str('%.6E' % self.MuRinput))
        self.filedata = self.filedata.replace('M1input', str('%.6E' % self.mBino))
        self.filedata = self.filedata.replace('M4input', str('%.6E' % self.mBinop))
        self.filedata = self.filedata.replace('M3input', str('%.6E' % self.mGluino))
    
        self.filedata = self.filedata.replace('YVlowin11', str('%.6E' % self.Yv11))
        self.filedata = self.filedata.replace('YVlowin22', str('%.6E' % self.Yv22))
        self.filedata = self.filedata.replace('YVlowin33', str('%.6E' % self.Yv33))

        self.filedata = self.filedata.replace('YSlowin11', str('%.6E' % self.Ys11))
        self.filedata = self.filedata.replace('YSlowin22', str('%.6E' % self.Ys22))
        self.filedata = self.filedata.replace('YSlowin33', str('%.6E' % self.Ys33))

        # Write the file out again
        with open(NewLesHouchesFile, 'w') as newfile:
            newfile.write(self.filedata)


    def StartSPheno(self, SPhenoPath, LesHouchesFile, ordernum):
#        string = "./" + SPhenoPath + " " + LesHouchesFile
#        os.system(string)
	os.system("./../SPhenoNaturalNonUniGauginoBLRinvSeesaw LesHouches.in.NewNaturalNonUniGauginoBLRinvSeesaw")
	if os.path.exists("SPheno.spc.NaturalNonUniGauginoBLRinvSeesaw") == True:
        	new_file = os.path.join("../out_files", "stem." + str(ordernum))
        	os.rename("SPheno.spc.NaturalNonUniGauginoBLRinvSeesaw", new_file )

##########################################################

SLHAfilesPath = "/gs/scratch/oozdal/mBLRISS/NonunigauginomchiBLR/out_files/" + "stem."
SPhenoExecPath = "../SPhenoNaturalNonUniGauginoBLRinvSeesaw/"
LesHouchesFilePath = "../LesHouches.in.NaturalNonUniGauginoBLRinvSeesaw"
NewLesHouchesFilePath = "LesHouches.in.NewNaturalNonUniGauginoBLRinvSeesaw"

initial = startpoint
final = endpoint

newset = CreateNewSLHA()

for order in range(initial,final):
	if os.path.exists("/gs/scratch/oozdal/mBLRISS/NaturalNonUniGauginoBLRinvSeesaw/out_files/" + "stem." + str(order)) == False:
		newset.readSLHA(order)
		newset.AssignValues(LesHouchesFilePath, NewLesHouchesFilePath)
		newset.StartSPheno(SPhenoExecPath, NewLesHouchesFilePath, order) 
    



