class Standard_Model():
    def __init__(self):

         self.Constants()

    def Constants(self):

         self.HiggsBosonMass=125.09
         self.ZBosonMass=80.385

class parameterset():
    def __init__(self,data):
         self.data = np.genfromtxt(projectdatapath + data)
         self.param = {}
         self.pdata = pd.read_csv(parameterspath, sep=" ", header=None, names= ["index","parameters"])
         for i in range(0, len(self.pdata)):
              self.param[self.pdata["parameters"][i]]=self.data[:,self.pdata["index"][i]]
                  
         self.AbsoluteParam()
         self.NormSIxsection()
         self.Indirect_Detection()
         self.Muong2()

    def Muong2(self):

         self.muong2_1sig = {}
         self.muong2_2sig = {}

         self.param["DAMU"] = self.param["DAMU"]*1e10

         for i in range(len(self.pdata)):
             self.muong2_1sig[self.pdata["parameters"][i]] = []
             self.muong2_2sig[self.pdata["parameters"][i]] = []

             for j in range(len(self.data)):
                 if self.param["DAMU"][j] > 20.7 and self.param["DAMU"][j] < 36.7:
                     self.muong2_1sig[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 elif self.param["DAMU"][j] > 12.7 and self.param["DAMU"][j] < 44.7:
                     self.muong2_2sig[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

    def Indirect_Detection(self):
                  
         RelicPlanckValue = 0.1184

         self.param["Microsigmav"] = self.param["Microsigmav"]*((self.param["RELIC"]/RelicPlanckValue)**2)


    def NormSIxsection(self):
         
         RelicPlanckValue = 0.1184

         self.param["ProtonSI"] = self.param["ProtonSI"]*(self.param["RELIC"]/RelicPlanckValue)        
         self.param["NeutronSI"] = self.param["NeutronSI"]*(self.param["RELIC"]/RelicPlanckValue)
 
    def AbsoluteParam(self):
         
         self.param["mchi1"] = abs(self.param["mchi1"])
 

    def LSPmass(self):
         
         self.LSPmass = []
         for i in range(len(self.data)):
             if self.param["LSP"][i] == 1000022:
                 self.LSPmass.append(self.param["mchi1"][i])
             elif self.param["LSP"][i] == 1000012:
                 self.LSPmass.append(self.param["MassSv1"][i])
     
    def Closest(self, list, Number):
         aux = []
         for valor in list:
             aux.append(abs(Number-valor))
         return aux.index(min(aux))


    def xSectionSignalStrength(self):

         self.LSPmass()

         self.nearestXENON1Txsection = []
         self.nearestXENONnTxsection = []
         self.nearestDARWINxsection = []

         for i in range(len(self.data)):
             self.nearestXENON1Txsection.append(XENON1TXSECTION[self.Closest(XENONWIMPMASS,self.LSPmass[i])])
             self.nearestXENONnTxsection.append(XENONnTXSECTION[self.Closest(XENONnTWIMPMASS,self.LSPmass[i])])
             self.nearestDARWINxsection.append(DARWINXSECTION[self.Closest(DARWINWIMPMASS,self.LSPmass[i])])

         self.Xenon1TProtonSIstrength = self.param["ProtonSI"]/self.nearestXENON1Txsection
         self.Xenon1TNeutronSIstrength = self.param["NeutronSI"]/self.nearestXENON1Txsection

         self.XenonNTProtonSIstrength = self.param["ProtonSI"]/self.nearestXENONnTxsection
         self.XenonNTNeutronSIstrength = self.param["NeutronSI"]/self.nearestXENONnTxsection

         self.DARWINProtonSIstrength = self.param["ProtonSI"]/self.nearestDARWINxsection
         self.DARWINNeutronSIstrength = self.param["NeutronSI"]/self.nearestDARWINxsection


    def Create_mchi1_Content(self):
         self.mchi1content = []

         self.BBRlike = {}
         self.HRlike = {}
         self.Winolike = {}
         self.Higgsinolike = {}
         self.Mixedmchi1 = {}

         self.Bcontent = self.param["NMIX11"]**2
         self.Wcontent = self.param["NMIX12"]**2
         self.BRcontent = self.param["NMIX15"]**2
         self.HRcontent = (self.param["NMIX16"]**2)+(self.param["NMIX17"]**2)
         self.Hcontent = (self.param["NMIX13"]**2)+(self.param["NMIX14"]**2)

         for i in range(len(self.pdata)):
             self.BBRlike[self.pdata["parameters"][i]] = []
             self.HRlike[self.pdata["parameters"][i]] = []
             self.Winolike[self.pdata["parameters"][i]] = []
             self.Higgsinolike[self.pdata["parameters"][i]] = []
             self.Mixedmchi1[self.pdata["parameters"][i]] = []

             for j in range(len(self.data)):
                 if self.BRcontent[j] + self.Bcontent[j] > .80:
                     self.mchi1content.append("BBRlike")
                     self.BBRlike[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 elif self.HRcontent[j] > .80:
                     self.mchi1content.append("HRlike")
                     self.HRlike[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 elif self.Wcontent[j] > .80:
                     self.mchi1content.append("Winolike")
                     self.Winolike[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 elif self.Hcontent[j] > .80:
                     self.mchi1content.append("Higgsinolike")
                     self.Higgsinolike[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                 else:
                     self.mchi1content.append("Mixed")
                     self.Mixedmchi1[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                  
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

