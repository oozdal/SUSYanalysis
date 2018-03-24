class modelname:
    def __init__(self):
         self.projectdirpath = '/Users/oozdal/projects/'+ projectname
         self.projectdatapath = self.projectdirpath + '/data/'
         self.plotdirpath = self.projectdirpath + '/plot/'
 
class parameterset(modelname):
    execfile("initialparams.py")
    def dataload(self, data):
        self.data = np.genfromtxt(self.projectdatapath + data)
        execfile("parameters.py")        


    def content(self):
        self.mchi1content = []
        self.massSv1content = []

        self.BBRlike_mchi1 = []
        self.HRlike_mchi1 = []
        self.Wlike_mchi1 = []
        self.Hlike_mchi1 = []
        self.mixed_mchi1 = []

        self.BBRlike_relic = []
        self.HRlike_relic = []
        self.Wlike_relic = []
        self.Hlike_relic = []
        self.mixed_relic = []

        self.SvLeft_relic = []
        self.SvRight_relic = []
        self.SvScalar_relic = []
        self.SvMixed_relic = []

        self.BBRlike_fixedrelicnucleonSI = []
        self.HRlike_fixedrelicnucleonSI = []
        self.Wlike_fixedrelicnucleonSI = []
        self.Hlike_fixedrelicnucleonSI = []
        self.mixed_fixedrelicnucleonSI = []

        self.SvLeft_fixedrelicnucleonSI = []
        self.SvRight_fixedrelicnucleonSI = []
        self.SvScalar_fixedrelicnucleonSI = []
        self.SvMixed_fixedrelicnucleonSI = []

        for i in range(len(self.order)):
                if self.BRcontent[i] + self.Bcontent[i] > .80:
                    self.mchi1content.append("BBR-mixed")
                    self.BBRlike_mchi1.append(self.mchi1[i])
                    self.BBRlike_relic.append(self.relic[i])
                    self.m0.append

                elif self.HRcontent[i] > .80:
                    self.mchi1content.append("HR-like")
                    self.HRlike_mchi1.append(self.mchi1[i])
                    self.HRlike_relic.append(self.relic[i])

                elif self.Wcontent[i] > .80:
                    self.mchi1content.append("Wino-like")
                    self.Wlike_mchi1.append(self.mchi1[i])
                    self.Wlike_relic.append(self.relic[i])

                elif self.Hcontent[i] > .80:
                    self.mchi1content.append("Higgsino-like")
                    self.Hlike_mchi1.append(self.mchi1[i])
                    self.Hlike_relic.append(self.relic[i])
                else:
                    self.mchi1content.append("Mixed")
                    self.mixed_mchi1.append(self.mchi1[i])
                    self.mixed_relic.append(self.relic[i])

########## Scalar Neutrino Content ########################

                if self.SvLeft[i] > .70:    
                    self.massSv1content.append("Left-Handed-Like")
                    self.SvLeft_mchi1.append(self.mchi1[i])
                    self.SvLeft_relic.append(self.relic[i])

                elif self.SvRight[i] > .70:
                    self.massSv1content.append("Right-Handed-Like")
                    self.SvRight_mchi1.append(self.mchi1[i])
                    self.SvRight_relic.append(self.relic[i])

                elif self.Scalar[i] > .70:
                    self.massSv1content.append("S-Like")
                    self.SvScalar_mchi1.append(self.mchi1[i])
                    self.SvScalar_relic.append(self.relic[i])

                else:
                    self.massSv1content.append("Mixed")
                    self.SvMixed_mchi1.append(self.mchi1[i])
                    self.SvMixed_relic.append(self.relic[i])


