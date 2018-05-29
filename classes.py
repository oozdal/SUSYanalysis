
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
         self.param["mchi2"] = abs(self.param["mchi2"]) 

    def FixedParam(self):

         for i in range(len(self.data)):
            if self.param["SUSYFT"][i] < 0.:
                self.param["SUSYFT"][i] = 1e40
            else:
                continue

    def LSPmass(self):
         
         self.LSPmass = []
         for i in range(len(self.data)):
             if self.param["LSP"][i] == 1000022:
                 self.LSPmass.append(self.param["mchi1"][i])
             elif self.param["LSP"][i] == 1000012:
                 self.LSPmass.append(self.param["MassSv1"][i])
     
         self.LSPmass = abs(np.array(self.LSPmass))

    def NLSPmass(self):
          
         self.NLSPmass = []
         for i in range(len(self.data)):
             if self.param["NLSP"][i] == 1000012:
                 self.NLSPmass.append(self.param["MassSv1"][i])
             elif self.param["NLSP"][i] == 1000023:
                 self.NLSPmass.append(self.param["mchi2"][i])
             elif self.param["NLSP"][i] == 1000024:
                 self.NLSPmass.append(self.param["mcha1"][i])
             elif self.param["NLSP"][i] == 1000011:
                 self.NLSPmass.append(self.param["stau1"][i])
             elif self.param["NLSP"][i] == 1000021:
                 self.NLSPmass.append(self.param["gluino"][i])
             elif self.param["NLSP"][i] == 1000022:
                 self.NLSPmass.append(self.param["mchi1"][i])
             else:
                 self.NLSPmass.append(1e40)
    
         self.NLSPmass = abs(np.array(self.NLSPmass))


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
    

    def BLRSSMFineTuning(self):
         
         self.A = self.param["gLSUSY"]**2 + self.param["gRSUSY"]**2 + self.param["gRBL"]**2
         self.B = self.param["gBLSUSY"]**2 + self.param["gRSUSY"]**2 + self.param["gBLR"]**2 + self.param["gRBL"]**2 - 2*self.param["gBLR"]*self.param["gRSUSY"] - 2*self.param["gRBL"]*self.param["gBLSUSY"]
         self.C = (self.param["gLSUSY"]**2)*(self.param["gRSUSY"] - self.param["gBLR"])**2 + (self.param["gBLSUSY"]**2)*(self.param["gLSUSY"]**2 + self.param["gRSUSY"]**2) - 2*self.param["gBLSUSY"]*(self.param["gLSUSY"]**2 + self.param["gBLR"]*self.param["gRSUSY"])*self.param["gRBL"] + (self.param["gBLR"]**2 + self.param["gLSUSY"]**2)*self.param["gRBL"]**2
         
         self.ALR1 = self.param["gBLSUSY"]**2 + self.param["gRSUSY"]**2 + self.param["gBLR"]**2 + self.param["gRBL"]**2 - 2*self.param["gRSUSY"]*self.param["gBLR"] - 2*self.param["gBLSUSY"]*self.param["gRBL"]

         self.ALR2 = self.param["gRSUSY"]**2 + self.param["gRBL"]**2 - (self.param["gRSUSY"]*self.param["gBLR"]) - (self.param["gBLSUSY"]*self.param["gRBL"])
         self.ALR3 = self.param["gLSUSY"]**2 + self.param["gRSUSY"]**2 + self.param["gRBL"]**2

############################################## Checking masses ##############################################
         self.Zboson = np.sqrt((self.C*self.param["vev"]**2)/(4*self.B))

         self.ExprForZpSquared = ((self.A*self.B - self.C)*self.param["vev"]**2 + ((self.B**2)*(self.param["vR"]**2))) / (4*self.B)
         self.Zprime = np.sqrt(self.ExprForZpSquared)

         self.ApproxExprForZpSquared = (1/4.)*self.ALR1*self.param["vR"]**2
         self.ApproxZprime = np.sqrt(self.ApproxExprForZpSquared)

###################################### Checking FT Expressions #############################################

         self.Beta = np.arctan(self.param["tanb"])
         self.BetaPrime = np.arctan(self.param["tanbp"])

         self.Coeff1 = self.C/(self.ALR3*self.B)
         self.Coeff2 = self.ALR2/self.ALR1

         self.AngleCoeff = np.cos(2*self.BetaPrime)/np.cos(2*self.Beta)

         self.MSSMFirstTerm = (self.param["mHd2SUSY"])/((self.param["tanb"]**2)-1.)
         self.MSSMSecondTerm = ((self.param["mHu2SUSY"])*(self.param["tanb"]**2))/((self.param["tanb"]**2)-1.)
         self.MSSMThirdTerm = (abs(self.param["MuSUSY"])**2)

         self.TermForZp = self.Coeff2*((self.param["massVZR"]**2)/2.)*self.AngleCoeff

         self.MSSMPart = self.MSSMFirstTerm - self.MSSMSecondTerm - self.MSSMThirdTerm

         self.MZ2DivBy2 = self.Coeff1*(self.MSSMPart - self.TermForZp)

         self.CheckforZboson = np.sqrt(abs(2.*self.MZ2DivBy2))

##################################### Calculate FT #########################################################

         CoeffmHd2 = abs(self.Coeff1*self.MSSMFirstTerm)
         CoeffmHu2 = abs(self.Coeff1*self.MSSMSecondTerm)
         CoeffMu   = abs(self.Coeff1*self.MSSMThirdTerm)
         CoeffZp   = abs(self.Coeff1*self.TermForZp)
    
         self.EWFT = []

         for i in range(len(self.data)):
             ChooseMaxSeries = {"CoeffmHd2":CoeffmHd2[i],"CoeffmHu2":CoeffmHu2[i],"CoeffMu":CoeffMu[i],"CoeffZp":CoeffZp[i]}
             ChooseMaxSeries = pd.Series(ChooseMaxSeries) 
             
             MaxCoeff = ChooseMaxSeries.values.max()
             EWFT_list = ChooseMaxSeries.values.max()/((self.Zboson[i]**2)/2)

             self.EWFT.append(EWFT_list)

         
         self.EWFTlt500 = {}
         self.EWFT500_1000 = {}
         self.EWFT1000_5000 = {}
         self.EWFTbt5000 = {}

         for i in range(len(self.pdata)):
             self.EWFTlt500[self.pdata["parameters"][i]] = []
             self.EWFT500_1000[self.pdata["parameters"][i]] = []
             self.EWFT1000_5000[self.pdata["parameters"][i]] = []
             self.EWFTbt5000[self.pdata["parameters"][i]] = []

             for j in range(len(self.data)):
                 if self.EWFT[j] <= 500.:
                     self.EWFTlt500[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                 if self.EWFT[j] > 500. and self.EWFT[j] <= 1000.:
                     self.EWFT500_1000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                 if self.EWFT[j] > 1000. and self.EWFT[j] <= 5000.:
                     self.EWFT1000_5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                 if self.EWFT[j] > 5000.:
                     self.EWFTbt5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

    def FineTuning(self,FTScale):
        
         self.FTScale = FTScale

         self.FixedParam()

         if self.FTScale == "GUT":

            for i in range(len(self.param["GUTFT"])):
                if self.param["GUTFT"][i] < 0:
                    self.param["GUTFT"][i] = 1e40
                else:
                    continue


            self.GUTFT_LT500 = {}
            self.GUTFT_500_1000 = {}
            self.GUTFT_1000_5000 = {}
            self.GUTFT_GT5000 = {}

            for i in range(len(self.pdata)):
                self.GUTFT_LT500[self.pdata["parameters"][i]] = []
                self.GUTFT_500_1000[self.pdata["parameters"][i]] = []
                self.GUTFT_1000_5000[self.pdata["parameters"][i]] = []
                self.GUTFT_GT5000[self.pdata["parameters"][i]] = []

                for j in range(len(self.data)):
                    if self.param["GUTFT"][j] <= 500.:
                        self.GUTFT_LT500[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                    elif self.param["GUTFT"][j] > 500. and self.param["GUTFT"][j] <= 1000.:
                        self.GUTFT_500_1000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                    elif self.param["GUTFT"][j] > 1000. and self.param["GUTFT"][j] <= 5000.:
                        self.GUTFT_1000_5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
    
                    elif self.param["GUTFT"][j] >= 5000. and self.param["GUTFT"][j] <= 20000:
                        self.GUTFT_GT5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                    else:
                        continue

         if self.FTScale == "SUSY":

            for i in range(len(self.param["SUSYFT"])):
                if self.param["SUSYFT"][i] < 0:
                    self.param["SUSYFT"][i] = 1e40
                else:
                    continue

            self.SUSYFT_LT500 = {}
            self.SUSYFT_500_1000 = {}
            self.SUSYFT_1000_5000 = {}
            self.SUSYFT_GT5000 = {}

            for i in range(len(self.pdata)):
                self.SUSYFT_LT500[self.pdata["parameters"][i]] = []
                self.SUSYFT_500_1000[self.pdata["parameters"][i]] = []
                self.SUSYFT_1000_5000[self.pdata["parameters"][i]] = []
                self.SUSYFT_GT5000[self.pdata["parameters"][i]] = []

                for j in range(len(self.data)):
                    if self.param["SUSYFT"][j] > 0.1 and self.param["SUSYFT"][j] <= 500.:
                        self.SUSYFT_LT500[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                    elif self.param["SUSYFT"][j] > 500. and self.param["SUSYFT"][j] <= 1000.:
                        self.SUSYFT_500_1000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                    elif self.param["SUSYFT"][j] > 1000. and self.param["SUSYFT"][j] <= 5000.:
                        self.SUSYFT_1000_5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])

                    elif self.param["SUSYFT"][j] >= 5000. and self.param["SUSYFT"][j] <= 20000:
                        self.SUSYFT_GT5000[self.pdata["parameters"][i]].append(self.param[self.pdata["parameters"][i]][j])
                    else:
                        continue

    def ProduceNewSLHA(self):
        pass





    
