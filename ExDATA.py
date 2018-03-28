###################################################

LUXDATA=np.genfromtxt('expdata/LUX2014.dat')

LUXDATALSPMASS=LUXDATA[:,0]

LUXDATARELIC=(LUXDATA[:,1])/1e9

###################################################

LUX2017=np.loadtxt('expdata/LUX2017.dat',delimiter=',')

LUX2017WIMPMASS=LUX2017[:,0]

LUX2017RELIC=(LUX2017[:,1])*1e36

####################################################

XENONDATA=np.loadtxt('expdata/XENON1T.dat',delimiter=',')

XENONWIMPMASS=XENONDATA[:,0]

XENONRELIC=(XENONDATA[:,1])*1e36 # to convert cm^2 to pb

XENONRELIC2sigmamax = XENONRELIC+XENONRELIC*47.5/100
XENONRELIC2sigmamin = XENONRELIC-XENONRELIC*47.5/100
XENONRELIC1sigmamax = XENONRELIC+XENONRELIC*34/100
XENONRELIC1sigmamin = XENONRELIC-XENONRELIC*34/100

#####################################################

SQUARKSCMS=np.loadtxt('expdata/gluino_squarks.dat',delimiter=',')
#SQUARKSCMS=np.genfromtxt('gluino_squarks.dat')

GLUINOMASS=SQUARKSCMS[:,0]

SQUARKSMASS=SQUARKSCMS[:,1]

oldobslim=np.loadtxt('expdata/oldobslim.dat',delimiter=',')

gluinoobslim=oldobslim[:,0]

squarksobslim=oldobslim[:,1]

######################################################

DARWIN=np.loadtxt('expdata/DARWIN.dat',delimiter=',')

DARWINWIMPMASS=DARWIN[:,0]

DARWINXSECTION=(DARWIN[:,1])*1e36

#####################################################

XENONnTDATA=np.loadtxt('expdata/XENONnT.dat',delimiter=',')

XENONnTWIMPMASS=XENONnTDATA[:,0]

XENONnTXSECTION=(XENONnTDATA[:,1])*1e36

####################################################

observedxsection13TeVZplldata=np.loadtxt('expdata/observedxsection13TeVZpll.dat',delimiter=',')

observedxsection13TeVZpmassforll=observedxsection13TeVZplldata[:,0]

observedxsection13TeVZpll=observedxsection13TeVZplldata[:,1]

observedxsection13TeVZpll2sigmamax = observedxsection13TeVZpll+observedxsection13TeVZpll*47.5/100
observedxsection13TeVZpll2sigmamin = observedxsection13TeVZpll-observedxsection13TeVZpll*47.5/100
observedxsection13TeVZpll1sigmamax = observedxsection13TeVZpll+observedxsection13TeVZpll*34/100
observedxsection13TeVZpll1sigmamin = observedxsection13TeVZpll-observedxsection13TeVZpll*34/100

###

expectedxsection13TeVZplldata=np.loadtxt('expdata/expectedxsection13TeVZpll.dat',delimiter=',')

expectedxsection13TeVZpmassforll=expectedxsection13TeVZplldata[:,0]

expectedxsection13TeVZpll=expectedxsection13TeVZplldata[:,1]

expectedxsection13TeVZpll2sigmamax = expectedxsection13TeVZpll+expectedxsection13TeVZpll*70/100
expectedxsection13TeVZpll2sigmamin = expectedxsection13TeVZpll-expectedxsection13TeVZpll*45/100
expectedxsection13TeVZpll1sigmamax = expectedxsection13TeVZpll+expectedxsection13TeVZpll*34/100
expectedxsection13TeVZpll1sigmamin = expectedxsection13TeVZpll-expectedxsection13TeVZpll*25/100

###################################################

observedxsection13TeVZpqqbardata=np.loadtxt('expdata/observedxsection13TeVZpqqbar.dat',delimiter=',')

observedxsection13TeVZpmassforqqbar=observedxsection13TeVZpqqbardata[:,0]

observedxsection13TeVZpqqbar=observedxsection13TeVZpqqbardata[:,1]

observedxsection13TeVZpqqbar2sigmamax = observedxsection13TeVZpqqbar+observedxsection13TeVZpqqbar*47.5/100
observedxsection13TeVZpqqbar2sigmamin = observedxsection13TeVZpqqbar-observedxsection13TeVZpqqbar*47.5/100
observedxsection13TeVZpqqbar1sigmamax = observedxsection13TeVZpqqbar+observedxsection13TeVZpqqbar*34/100
observedxsection13TeVZpqqbar1sigmamin = observedxsection13TeVZpqqbar-observedxsection13TeVZpqqbar*30/100

###

expectedxsection13TeVZpqqbardata=np.loadtxt('expdata/expectedxsection13TeVZpqqbar.dat',delimiter=',')

expectedxsection13TeVZpmassforqqbar=expectedxsection13TeVZpqqbardata[:,0]

expectedxsection13TeVZpqqbar=expectedxsection13TeVZpqqbardata[:,1]

expectedxsection13TeVZpqqbar2sigmamax = expectedxsection13TeVZpqqbar+expectedxsection13TeVZpqqbar*70./100
expectedxsection13TeVZpqqbar2sigmamin = expectedxsection13TeVZpqqbar-expectedxsection13TeVZpqqbar*47.5/100
expectedxsection13TeVZpqqbar1sigmamax = expectedxsection13TeVZpqqbar+expectedxsection13TeVZpqqbar*34/100
expectedxsection13TeVZpqqbar1sigmamin = expectedxsection13TeVZpqqbar-expectedxsection13TeVZpqqbar*30/100

###################################################

fermilatbbbardata=np.loadtxt('expdata/fermilatbbbar.dat',delimiter=',')
fermilatbbbarWIMPmass=fermilatbbbardata[:,0]
fermilatbbbarsigmav=fermilatbbbardata[:,1]

###################################################

fermilatWWdata=np.loadtxt('expdata/fermilatWW.dat',delimiter=',')
fermilatWWWIMPmass=fermilatWWdata[:,0]
fermilatWWsigmav=fermilatWWdata[:,1]

##################################################

fermilattautaudata=np.loadtxt('expdata/fermilattautau.dat',delimiter=',')
fermilattautauWIMPmass=fermilattautaudata[:,0]
fermilattautausigmav=fermilattautaudata[:,1]

##################################################

fermilatmumudata=np.loadtxt('expdata/fermilatmumu.dat',delimiter=',')
fermilatmumuWIMPmass=fermilatmumudata[:,0]
fermilatmumusigmav=fermilatmumudata[:,1]

##################################################
