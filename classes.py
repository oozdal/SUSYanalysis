class createproject:
    def __init__(self):
         self.projectdirpath = '/Users/oozdal/projects/'+ projectname
         self.projectdatapath = self.projectdirpath + '/data/'
         self.plotdirpath = self.projectdirpath + '/plot/'
         self.parameterspath = self.projectdirpath + '/parameters.py'
    
class parameterset(createproject):
    def __init__(self,data):
         createproject.__init__(self)
         self.data = np.genfromtxt(self.projectdatapath + data)
         self.param = {}
         self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
         for i in range(0, len(self.pdata)):
              self.param[self.pdata["parameters"][i]]=self.data[:,self.pdata["index"][i]]

    def neutralino_content(self):
         self.mchi1content = []

         self.Bcontent = self.param["NMIX11"]**2
         self.Wcontent = self.param["NMIX12"]**2
         self.BRcontent = self.param["NMIX15"]**2
         self.HRcontent = (self.param["NMIX16"]**2)+(self.param["NMIX17"]**2)
         self.Hcontent = (self.param["NMIX13"]**2)+(self.param["NMIX14"]**2)

         for i in range(len(self.data)):
             if self.BRcontent[i] + self.Bcontent[i] > .80:
                 self.mchi1content.append("BBRlike")

             elif self.HRcontent[i] > .80:
                  self.mchi1content.append("HRlike")

             elif self.Wcontent[i] > .80:
                  self.mchi1content.append("Winolike")

             elif self.Hcontent[i] > .80:
                  self.mchi1content.append("Higgsinolike")

             else:
                  self.mchi1content.append("Mixed")
                  
    def CreateSv1Content(self):
         self.Sv1Content = []

         self.LeftSv1 = {}
         self.RightSv1 = {}
         self.ScalarSv1 = {}
         self.MixedSv1 = {}

         self.Sv1LeftContent=(self.param["SNUMIX11"]**2)+(self.param["SNUMIX12"]**2)+(self.param["SNUMIX13"]**2)
         self.Sv1RightContent=(self.param["SNUMIX14"]**2)+(self.param["SNUMIX15"]**2)+(self.param["SNUMIX16"]**2)
         self.Sv1ScalarContent=(self.param["SNUMIX17"]**2)+(self.param["SNUMIX18"]**2)+(self.param["SNUMIX19"]**2)
         
         for i in range(len(self.pdata)):
             self.LeftSv1[self.pdata["parameters"][i]] = []
             self.RightSv1[self.pdata["parameters"][i]] = []
             self.ScalarSv1[self.pdata["parameters"][i]] = []
             self.MixedSv1[self.pdata["parameters"][i]] = []

             for j in range(len(self.data)):
                 if self.Sv1LeftContent[j] > .70:
                     self.Sv1Content.append("Left-Handed-like")
                     self.LeftSv1[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
            
                 elif self.Sv1RightContent[j] > .70:
                     self.Sv1Content.append("Right-Handed-like")
                     self.RightSv1[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 elif self.Sv1ScalarContent[j] > 70:
                     self.Sv1Content.append("Scalar-like")
                     self.ScalarSv1[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 else:
                     self.Sv1Content.append("Mixed")
                     self.MixedSv1[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])


class BBRlikeContent(createproject):
    def __init__(self,paramclass):
        createproject.__init__(self)
        self.param = {}
        self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
        for i in range(0, len(self.pdata)):
             self.param[self.pdata["parameters"][i]] = []
             for j in range(len(paramclass.data)):
                  if paramclass.BRcontent[j] + paramclass.Bcontent[j] > .80:
                       self.param[self.pdata["parameters"][i]].append(paramclass.param[paramclass.pdata["parameters"][i]][j])

class HRlikeContent(createproject):
    def __init__(self,paramclass):
        createproject.__init__(self)
        self.param = {}
        self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
        for i in range(0, len(self.pdata)):
             self.param[self.pdata["parameters"][i]] = []
             for j in range(len(paramclass.data)):
                  if paramclass.HRcontent[j] > .80:
                       self.param[self.pdata["parameters"][i]].append(paramclass.param[paramclass.pdata["parameters"][i]][j])

class HlikeContent(createproject):
    def __init__(self,paramclass):
        createproject.__init__(self)
        self.param = {}
        self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
        for i in range(0, len(self.pdata)):
             self.param[self.pdata["parameters"][i]] = []
             for j in range(len(paramclass.data)):
                  if paramclass.Hcontent[j] > .80:
                       self.param[self.pdata["parameters"][i]].append(paramclass.param[paramclass.pdata["parameters"][i]][j])

class WlikeContent(createproject):
    def __init__(self,paramclass):
        createproject.__init__(self)
        self.param = {}
        self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
        for i in range(0, len(self.pdata)):
             self.param[self.pdata["parameters"][i]] = []
             for j in range(len(paramclass.data)):
                  if paramclass.Wcontent[j] > .80:
                       self.param[self.pdata["parameters"][i]].append(paramclass.param[paramclass.pdata["parameters"][i]][j])

class MixedContent(createproject):
    def __init__(self,paramclass):
        createproject.__init__(self)
        self.param = {}
        self.pdata = pd.read_csv(self.parameterspath, sep=" ", header=None, names= ["index","parameters"])
        for i in range(0, len(self.pdata)):
             self.param[self.pdata["parameters"][i]] = []
             for j in range(len(paramclass.data)):
                  if paramclass.mchi1content[j] == "Mixed":
                       self.param[self.pdata["parameters"][i]].append(paramclass.param[paramclass.pdata["parameters"][i]][j])

