self.param["m0"]=self.data[:,0]
self.mhf=self.data[:,1]
#self.sgnmu=self.data[:,2]
self.A0=self.data[:,3]
#self.sgnmup=self.data[:,4]
self.tanb=self.data[:,5]
self.tanbp=self.data[:,6]
self.vR=self.data[:,7]

self.masshh1=self.data[:,8]
self.masshh2=self.data[:,9]
self.masshh3=self.data[:,10]
self.masshh4=self.data[:,11]

self.massAh3=self.data[:,12]
self.massAh4=self.data[:,13]
#self.massHpm2=self.data[:,14]
#self.massWZ=self.data[:,15]
#self.massVWm=self.data[:,16]
self.massVZR=self.data[:,17]
self.gluino=self.data[:,18]

self.mchi1=abs(self.data[:,19])
#self.mchi2=abs(self.data[:,20])
#self.mchi3=abs(self.data[:,21])
#self.mchi4=abs(self.data[:,22])
#self.mchi5=abs(self.data[:,23])
#self.mchi6=abs(self.data[:,24])
#self.mchi7=abs(self.data[:,25])
self.param["mcha1"]=abs(self.data[:,26])
#self.mcha2=abs(self.data[:,27])

self.LSP=self.data[:,28]
self.NLSP=self.data[:,29]

self.yv1_GUT=self.data[:,30]
self.yv2_GUT=self.data[:,31]
self.yv3_GUT=self.data[:,32]

self.ys1_GUT=self.data[:,33]
self.ys2_GUT=self.data[:,34]
self.ys3_GUT=self.data[:,35]

#self.LHC7gluonfusionh1=self.data[:,36]
#self.LHC7vectorfusionh1=self.data[:,37]
#self.LHC7WHproductionh1=self.data[:,38]
#self.LHC7ZHproductionh1=self.data[:,39]
#self.LHC7ttHproductionh1=self.data[:,40]

#self.LHC7gluonfusionh2=self.data[:,41]
#self.LHC7vectorfusionh2=self.data[:,42]
#self.LHC7WHproductionh2=self.data[:,43]
#self.LHC7ZHproductionh2=self.data[:,44]
#self.LHC7ttHproductionh2=self.data[:,45]

self.LHC8gluonfusionh1=self.data[:,46]
self.LHC8vectorfusionh1=self.data[:,47]
self.LHC8WHproductionh1=self.data[:,48]
self.LHC8ZHproductionh1=self.data[:,49]
self.LHC8ttHproductionh1=self.data[:,50]

self.LHC8gluonfusionh2=self.data[:,51]
self.LHC8vectorfusionh2=self.data[:,52]
self.LHC8WHproductionh2=self.data[:,53]
self.LHC8ZHproductionh2=self.data[:,54]
self.LHC8ttHproductionh2=self.data[:,55]

self.LHC13gluonfusionh1=self.data[:,56]
#self.LHC13vectorfusionh1=self.data[:,57]
#self.LHC13WHproductionh1=self.data[:,58]
#self.LHC13ZHproductionh1=self.data[:,59]
#self.LHC13ttHproductionh1=self.data[:,60]

self.LHC13gluonfusionh2=self.data[:,61]
#self.LHC13vectorfusionh2=self.data[:,62]
#self.LHC13WHproductionh2=self.data[:,63]
#self.LHC13ZHproductionh2=self.data[:,64]
#self.LHC13ttHproductionh2=self.data[:,65]

"""
self.LHC14gluonfusionh1=self.data[:,66]
self.LHC14vectorfusionh1=self.data[:,67]
self.LHC14WHproductionh1=self.data[:,68]
self.LHC14ZHproductionh1=self.data[:,69]
self.LHC14ttHproductionh1=self.data[:,70]

self.LHC14gluonfusionh2=self.data[:,71]
self.LHC14vectorfusionh2=self.data[:,72]
self.LHC14WHproductionh2=self.data[:,73]
self.LHC14ZHproductionh2=self.data[:,74]
self.LHC14ttHproductionh2=self.data[:,75]


self.LHC100gluonfusionh1=self.data[:,76]
self.LHC100vectorfusionh1=self.data[:,77]
self.LHC100WHproductionh1=self.data[:,78]
self.LHC100ZHproductionh1=self.data[:,79]
self.LHC100ttHproductionh1=self.data[:,80]

self.LHC100gluonfusionh2=self.data[:,81]
self.LHC100vectorfusionh2=self.data[:,82]
self.LHC100WHproductionh2=self.data[:,83]
self.LHC100ZHproductionh2=self.data[:,84]
self.LHC100ttHproductionh2=self.data[:,85]
"""

self.DAMU=self.data[:,86] # muon g-2

# Bphysics
self.BXsgamma=self.data[:,87]
self.RBtaunu=self.data[:,88]
self.Bsmumu=self.data[:,89]  #B_s--> mu mu

self.Higgsbo=self.data[:,90] # The results of the HiggsBounds Program. The result is 1 or 0
self.Higgschi=self.data[:,91]   # Higgs Chi^2 from HiggsSignals Program
self.totchi=self.data[:,92]     # Total Chi^2 from HiggsSignals Program
self.relic=self.data[:,93]      # Relic Density from micrOMEGAs Program

self.protonSI=self.data[:,94]   # Proton Spin Independent Cross-Section
self.protonSD=self.data[:,95]   # Proton Spin Dependent Cross-Section

self.neutronSI=self.data[:,96]  # Neutron Spin Independent Cross-Section
self.neutronSD=self.data[:,97]  # Neutron Spin Dependent Cross-Section

#self.Ge=self.data[:,98]
#self.Xe=self.data[:,99]
#self.Na=self.data[:,100]
#self.I=self.data[:,101]
self.Icecube=self.data[:,102]

self.massd1=self.data[:,103]
#self.massd2=self.data[:,104]
#self.masss1=self.data[:,105]
#self.masss2=self.data[:,106]
self.massb1=self.data[:,107]
#self.massb2=self.data[:,108]

#self.massu1=self.data[:,109]
#self.massu2=self.data[:,110]
#self.massc1=self.data[:,111]
#self.massc2=self.data[:,112]
self.masst1=self.data[:,113]
self.masst2=self.data[:,114]

#self.masse1=self.data[:,115]
#self.masse2=self.data[:,116]
self.massmu1=self.data[:,117]
self.massmu2=self.data[:,118]
self.masstau1=self.data[:,119]
#self.masstau2=self.data[:,120]

self.NMIX11=self.data[:,121]
self.NMIX12=self.data[:,122]
self.NMIX13=self.data[:,123]
self.NMIX14=self.data[:,124]
self.NMIX15=self.data[:,125]
self.NMIX16=self.data[:,126]
self.NMIX17=self.data[:,127]

self.NMIX21=self.data[:,128]
self.NMIX22=self.data[:,129]
self.NMIX23=self.data[:,130]
self.NMIX24=self.data[:,131]
self.NMIX25=self.data[:,132]
self.NMIX26=self.data[:,133]
self.NMIX27=self.data[:,134]

self.NMIX31=self.data[:,135]
self.NMIX32=self.data[:,136]
self.NMIX33=self.data[:,137]
self.NMIX34=self.data[:,138]
self.NMIX35=self.data[:,139]
self.NMIX36=self.data[:,140]
self.NMIX37=self.data[:,141]

self.NMIX41=self.data[:,142]
self.NMIX42=self.data[:,143]
self.NMIX43=self.data[:,144]
self.NMIX44=self.data[:,145]
self.NMIX45=self.data[:,146]
self.NMIX46=self.data[:,147]
self.NMIX47=self.data[:,148]

self.NMIX51=self.data[:,149]
self.NMIX52=self.data[:,150]
self.NMIX53=self.data[:,151]
self.NMIX54=self.data[:,152]
self.NMIX55=self.data[:,153]
self.NMIX56=self.data[:,154]
self.NMIX57=self.data[:,155]

self.NMIX61=self.data[:,156]
self.NMIX62=self.data[:,157]
self.NMIX63=self.data[:,158]
self.NMIX64=self.data[:,159]
self.NMIX65=self.data[:,160]
self.NMIX66=self.data[:,161]
self.NMIX67=self.data[:,162]

self.NMIX71=self.data[:,163]
self.NMIX72=self.data[:,164]
self.NMIX73=self.data[:,165]
self.NMIX74=self.data[:,166]
self.NMIX75=self.data[:,167]
self.NMIX76=self.data[:,168]
self.NMIX77=self.data[:,169]

self.SNUMIX11=self.data[:,170]
self.SNUMIX12=self.data[:,171]
self.SNUMIX13=self.data[:,172]
self.SNUMIX14=self.data[:,173]
self.SNUMIX15=self.data[:,174]
self.SNUMIX16=self.data[:,175]
self.SNUMIX17=self.data[:,176]
self.SNUMIX18=self.data[:,177]
self.SNUMIX19=self.data[:,178]

self.SNUMIX21=self.data[:,179]
self.SNUMIX22=self.data[:,180]
self.SNUMIX23=self.data[:,181]
self.SNUMIX24=self.data[:,182]
self.SNUMIX25=self.data[:,183]
self.SNUMIX26=self.data[:,184]
self.SNUMIX27=self.data[:,185]
self.SNUMIX28=self.data[:,186]
self.SNUMIX29=self.data[:,187]

self.SNUMIX31=self.data[:,188]
self.SNUMIX32=self.data[:,189]
self.SNUMIX33=self.data[:,190]
self.SNUMIX34=self.data[:,191]
self.SNUMIX35=self.data[:,192]
self.SNUMIX36=self.data[:,193]
self.SNUMIX37=self.data[:,194]
self.SNUMIX38=self.data[:,195]
self.SNUMIX39=self.data[:,196]

self.SNUMIX41=self.data[:,197]
self.SNUMIX42=self.data[:,198]
self.SNUMIX43=self.data[:,199]
self.SNUMIX44=self.data[:,200]
self.SNUMIX45=self.data[:,201]
self.SNUMIX46=self.data[:,202]
self.SNUMIX47=self.data[:,203]
self.SNUMIX48=self.data[:,204]
self.SNUMIX49=self.data[:,205]

self.SNUMIX51=self.data[:,206]
self.SNUMIX52=self.data[:,207]
self.SNUMIX53=self.data[:,208]
self.SNUMIX54=self.data[:,209]
self.SNUMIX55=self.data[:,210]
self.SNUMIX56=self.data[:,211]
self.SNUMIX57=self.data[:,212]
self.SNUMIX58=self.data[:,213]
self.SNUMIX59=self.data[:,214]

self.SNUMIX61=self.data[:,215]
self.SNUMIX62=self.data[:,216]
self.SNUMIX63=self.data[:,217]
self.SNUMIX64=self.data[:,218]
self.SNUMIX65=self.data[:,219]
self.SNUMIX66=self.data[:,220]
self.SNUMIX67=self.data[:,221]
self.SNUMIX68=self.data[:,222]
self.SNUMIX69=self.data[:,223]

self.SNUMIX71=self.data[:,224]
self.SNUMIX72=self.data[:,225]
self.SNUMIX73=self.data[:,226]
self.SNUMIX74=self.data[:,227]
self.SNUMIX75=self.data[:,228]
self.SNUMIX76=self.data[:,229]
self.SNUMIX77=self.data[:,230]
self.SNUMIX78=self.data[:,231]
self.SNUMIX79=self.data[:,232]

self.SNUMIX81=self.data[:,233]
self.SNUMIX82=self.data[:,234]
self.SNUMIX83=self.data[:,235]
self.SNUMIX84=self.data[:,236]
self.SNUMIX85=self.data[:,237]
self.SNUMIX86=self.data[:,238]
self.SNUMIX87=self.data[:,239]
self.SNUMIX88=self.data[:,240]
self.SNUMIX89=self.data[:,241]

self.SNUMIX91=self.data[:,242]
self.SNUMIX92=self.data[:,243]
self.SNUMIX93=self.data[:,244]
self.SNUMIX94=self.data[:,245]
self.SNUMIX95=self.data[:,246]
self.SNUMIX96=self.data[:,247]
self.SNUMIX97=self.data[:,248]
self.SNUMIX98=self.data[:,249]
self.SNUMIX99=self.data[:,250]

self.SCALARMIX11=self.data[:,251]
self.SCALARMIX12=self.data[:,252]
self.SCALARMIX13=self.data[:,253]
self.SCALARMIX14=self.data[:,254]

self.SCALARMIX21=self.data[:,255]
self.SCALARMIX22=self.data[:,256]
self.SCALARMIX23=self.data[:,257]
self.SCALARMIX24=self.data[:,258]

self.SCALARMIX31=self.data[:,259]
self.SCALARMIX32=self.data[:,260]
self.SCALARMIX33=self.data[:,261]
self.SCALARMIX34=self.data[:,262]

self.SCALARMIX41=self.data[:,263]
self.SCALARMIX42=self.data[:,264]
self.SCALARMIX43=self.data[:,265]
self.SCALARMIX44=self.data[:,266]

self.PSEUDOSCALARMIX11=self.data[:,267]
self.PSEUDOSCALARMIX12=self.data[:,268]
self.PSEUDOSCALARMIX13=self.data[:,269]
self.PSEUDOSCALARMIX14=self.data[:,270]

self.PSEUDOSCALARMIX21=self.data[:,271]
self.PSEUDOSCALARMIX22=self.data[:,272]
self.PSEUDOSCALARMIX23=self.data[:,273]
self.PSEUDOSCALARMIX24=self.data[:,274]

self.PSEUDOSCALARMIX31=self.data[:,275]
self.PSEUDOSCALARMIX32=self.data[:,276]
self.PSEUDOSCALARMIX33=self.data[:,277]
self.PSEUDOSCALARMIX34=self.data[:,278]

self.PSEUDOSCALARMIX41=self.data[:,279]
self.PSEUDOSCALARMIX42=self.data[:,280]
self.PSEUDOSCALARMIX43=self.data[:,281]
self.PSEUDOSCALARMIX44=self.data[:,282]

self.BRZpallleptons=self.data[:,283]
self.BRZpelecmu=self.data[:,284] 
self.BRZpsleptons=self.data[:,285]
self.BRZXX=self.data[:,286]
self.BRZjets=self.data[:,287]
self.BRZJustSMpar=self.data[:,288]

self.CHARGEMIX11=self.data[:,289]
self.CHARGEMIX12=self.data[:,290]
self.CHARGEMIX21=self.data[:,291]
self.CHARGEMIX22=self.data[:,292]

self.ZZMIX11=self.data[:,293]
self.ZZMIX12=self.data[:,294]
self.ZZMIX13=self.data[:,295]
self.ZZMIX21=self.data[:,296]
self.ZZMIX22=self.data[:,297]
self.ZZMIX23=self.data[:,298]
self.ZZMIX31=self.data[:,299]
self.ZZMIX32=self.data[:,300]
self.ZZMIX33=self.data[:,301]

self.gBLGUT=self.data[:,302]
self.gLGUT=self.data[:,303]
self.gRGUT=self.data[:,304]
self.g3GUT=self.data[:,305]

self.gBLSUSY=self.data[:,306]
self.gLSUSY=self.data[:,307]
self.gRSUSY=self.data[:,308]
self.g3SUSY=self.data[:,309]
self.gBLgRSUSY=self.data[:,310]
self.gRgBLSUSY=self.data[:,311]

self.MuR=self.data[:,312]
self.Mu=self.data[:,313]
self.BmuR=self.data[:,314]
self.Bmu=self.data[:,315]
self.vChiRb=self.data[:,316]
self.vChiR=self.data[:,317]
self.vd=self.data[:,318]
self.vu=self.data[:,319]
self.v=self.data[:,320]
#self.betaH=self.data[:,321]

self.mHd2SUSY=self.data[:,322]
self.mHu2SUSY=self.data[:,323]
self.mCR2SUSY=self.data[:,324]
self.mCRb2SUSY=self.data[:,325]
self.MBBRSUSY=self.data[:,326]
self.M1SUSY=self.data[:,327]
self.M2SUSY=self.data[:,328]
self.M4SUSY=self.data[:,328]
self.M3SUSY=self.data[:,330]

self.mHd2GUT=self.data[:,331]
self.mHu2GUT=self.data[:,332]
self.mCR2GUT=self.data[:,333]
self.mCRb2GUT=self.data[:,334]
self.MBBRGUT=self.data[:,335]
self.M1GUT=self.data[:,336]
self.M2GUT=self.data[:,337]
self.M4GUT=self.data[:,338]
self.M3GUT=self.data[:,339]
self.MuRGUT=self.data[:,340]

self.microsigmav=self.data[:,341]
self.photonflux=self.data[:,342]
self.positronflux=self.data[:,343]
self.antiprotonflux=self.data[:,344]
self.neutrinoflux=self.data[:,345]
self.antinuetrinoflux=self.data[:,346]
self.muonflux=self.data[:,347]

self.BRhh1VPVP=self.data[:,348]
self.BRhh2VPVP=self.data[:,349]
self.vzrxsectiontoll=self.data[:,350]

self.massSv1=self.data[:,351]
#self.massSv2=self.data[:,352]
#self.massSv3=self.data[:,353]
#self.massSv4=self.data[:,354]
#self.massSv5=self.data[:,355]
#self.massSv6=self.data[:,356]
#self.massSv7=self.data[:,357]
#self.massSv8=self.data[:,358]
#self.massSv9=self.data[:,359]

self.order=self.data[:,360]  # Note that list index starts from 0 in Python. Thus actually there are (order + 1) values in our reading.f90 code!



#############################################################################
############################# Extra Calculations ############################

def closest(list, Number):
    aux = []
    for valor in list:
        aux.append(abs(Number-valor))

    return aux.index(min(aux))



self.MSUSY=(self.masst1*self.masst2)**(1/2)

self.sigmav=(3*1e-27)/self.relic #Approximation

self.nucleonSI = (self.protonSI + self.neutronSI)/2
    


self.relicPlanckvalue = 0.1184
self.fixedprotonSI = self.protonSI*(self.relic/self.relicPlanckvalue)
self.fixedneutronSI = self.neutronSI*(self.relic/self.relicPlanckvalue)
self.fixednucleonSI = (self.fixedprotonSI + self.fixedneutronSI)/2


self.corXENONRELIC=[]
for i in range(len(self.mchi1)):
    self.corXENONRELIC.append(XENONRELIC[closest(XENONWIMPMASS,self.mchi1[i])])


self.protonSIstrength = self.fixedprotonSI/self.corXENONRELIC
self.neutronSIstrength = self.fixedneutronSI/self.corXENONRELIC
self.nucleonSIstrength = (self.protonSIstrength+self.neutronSIstrength)/2

############################################################################

self.Bcontent = self.NMIX11**2
self.Wcontent = self.NMIX12**2
self.BRcontent = self.NMIX15**2
self.HRcontent = (self.NMIX16**2)+(self.NMIX17**2)
self.Hcontent = (self.NMIX13**2)+(self.NMIX14**2)


self.SvLeft=(self.SNUMIX11**2)+(self.SNUMIX12**2)+(self.SNUMIX13**2)
self.SvRight=(self.SNUMIX14**2)+(self.SNUMIX15**2)+(self.SNUMIX16**2)
self.Scalar=(self.SNUMIX17**2)+(self.SNUMIX18**2)+(self.SNUMIX19**2)
