#!/usr/bin/python

from __future__ import division
from math import *
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib, os
import matplotlib.cm as cm
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.interpolate import griddata
import scipy
import pylab, subprocess

pylab.rcParams['figure.figsize'] = (8.0, 6.0)

#input=np.genfromtxt('../data/withoutZpboundneutralinolsp.dat')
#rejectdata=np.genfromtxt('../data/withoutZpboundneutralinoreject.rej')
#relicdata=np.genfromtxt('../data/withoutZpboundneutralinorelic.dat')

#input=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/neutralinolsp.dat')
#rejectdata=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/neutralinoreject.rej')
#relicdata=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/neutralinorelic.dat')

#input=input.tolist()
#rejectdata=rejectdata.tolist()
#relicdata=relicdata.tolist()

#input2=np.genfromtxt('../data/backup/sneutrinowithoutZp_mcgill.dat')
#rejectdata2=np.genfromtxt('../data/backup/reject_sneutrinowithoutZp_mcgill.rej')
#relicdata2=np.genfromtxt('../data/backup/relicsneutrinowithoutZp_mcgill.dat')

input=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/sneutrinolsp.dat')
#rejectdata=np.genfromtxt('../data/withoutZpboundsneutrinoreject.rej')
relicdata=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/sneutrinorelic.dat')

#input=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/sneutrinolsp.dat')
#rejectdata=np.genfromtxt('../data/withoutZpboundsneutrinoreject.rej')
#relicdata=np.genfromtxt('/Users/oozdal/projects/mchiRBLR/data/sneutrinorelic.dat')

#input=np.genfromtxt('../data/sneutrinolspoldZpbound.dat')
#rejectdata=np.genfromtxt('../data/sneutrinorejectforoldZp.dat')
#relicdata=np.genfromtxt('../data/sneutrinorelicforoldZp.dat')


#input2=input2.tolist()
#rejectdata2=rejectdata2.tolist()
#relicdata2=relicdata2.tolist()

#input=input+input2
#rejectdata=rejectdata+rejectdata2
#relicdata=relicdata+relicdata2

#input=np.array(input)
#rejectdata=np.array(rejectdata)
#relicdata=np.array(relicdata)

#########################################################################
################ Loading vzrxsectiontoll in universal BLRISS ###########

datafromMadGraphforvzrtoll=np.genfromtxt("/Users/oozdal/projects/mBLRinvSeesaw_universal/revisionMadGraph/data/trueZplldata/neutralinolsp.dat")

universalmassVZR=datafromMadGraphforvzrtoll[:,17]
universalvzrxsectiontoll=datafromMadGraphforvzrtoll[:,343]

#########################################################################################
################ Loading vzrxsectiontoll in BLRISS with B-L Non-Universality  ###########

BLnondatafromMadGraphforvzrtoll=np.genfromtxt("/Users/oozdal/projects/mchiRBLR/data/BLnonuniversalneutralinolspfromMadGraph.dat")

BLnonuniversalmassVZR=BLnondatafromMadGraphforvzrtoll[:,17]
BLnonuniversalvzrxsectiontoll=BLnondatafromMadGraphforvzrtoll[:,350]
BLnonBRZpelecmu=BLnondatafromMadGraphforvzrtoll[:,284]

#################################################################################

#################################################################################
#################### Loading Experimental Results ####################
execfile("/Users/oozdal/projects/mchiRBLR/ExDATA.py")

#####################################################################
################### Loding Model ###################################

execfile("INPUT.py")
execfile("RELIC.py")
#execfile("REJECT.py")

###################################################################





###################################################################
"""
cm = plt.cm.get_cmap('rainbow')

fig, ax1 = plt.subplots()

NLSPmass=[]
for i in range(0,len(input)):
   if (NLSP[i]==1000014):
       NLSPmass.append(massSv2[i])
   if (NLSP[i]==1000022):
       NLSPmass.append(mchi1[i])

sc1 = ax1.scatter(massSv1/1000.,relic,c=abs(NLSPmass-massSv1), cmap=cm ,s=8, linewidth = '0.0',marker='o')

cbar1 = plt.colorbar(sc1, format = "%.0f")
cbar1.set_label(r"$\displaystyle m_{NLSP}-m_{LSP} $ (GeV)", fontsize=20)

cbar1 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} $ (GeV)", fontsize=20)
cbar1 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

ax1.axis([0,1.4,1e-3,1e6])

plt.plot([0, 1400], [0.09488, 0.09488], 'k--')
plt.plot([0, 1400], [0.14232, 0.14232], 'k--')

ax1.xaxis.set_major_locator(MultipleLocator(0.2))
ax1.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax1.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax1.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/relic_sneutrino_diff.eps')   # save the figure to file
plt.close(fig)
"""
####################################################################
"""
cm = plt.cm.get_cmap('rainbow')

fig, ax2 = plt.subplots()

sc2 = ax2.scatter(Icecube,relic,c=mchi1, cmap=cm ,s=10, linewidth = '0.0',marker='o')

Zmax = np.array(relic).max()
cbar2 = plt.colorbar(sc2, format = "%.0f")
cbar2.set_label(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (GeV)", fontsize=20)

cbar2 = plt.xlabel(r"$ {\rm Icecube22\ Exclusion\ CLs\ for\ \nu\ flux\ (\%)}$", fontsize=18)
cbar2 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)
cbar2 = plt.xlim([-0.02,1.0])
cbar2 = plt.ylim([10**(-2),10**4])

plt.plot([0, 100], [0.09, 0.09], 'k--')
plt.plot([0, 100], [0.14, 0.14], 'k--')
plt.plot([68, 68], [10**(-2), 10**4], 'k--')

ax2.text(67.0,1.1*10**2,r"$\displaystyle \sigma_1$",fontsize=20)

ax2.xaxis.set_major_locator(MultipleLocator(0.2))
ax2.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax2.yaxis.set_major_locator(MultipleLocator(100))
#ax2.yaxis.set_minor_locator(MultipleLocator(25))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax2.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_icecube_mchi1.png')   # save the figure to file
plt.close(fig)
"""
################################################################
"""
fig, ax6 = plt.subplots()

sc6 = ax6.scatter(relicmchi1,relicprotonSI, s=10, c='Red', marker='o',linewidth = '0.0',zorder=30 )

sc6 = ax6.scatter(mchi1,protonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

sc6 = ax6.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc6 = ax6.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label='LUX2014')

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (GeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{p}^{SI} $ (pb)", fontsize=20)

plt.xlim([0.0,1400])
plt.ylim([1e-14,1e-7])

ax6.xaxis.set_major_locator(MultipleLocator(200))
ax6.xaxis.set_minor_locator(MultipleLocator(50))


#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax6.tick_params(which='both', direction='out')

plt.legend(loc='upper left',frameon=False)

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/protoncross_mchi1.eps')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax7 = plt.subplots()

sc7 = ax7.scatter(relicmchi1,relicneutronSI, s=10, c='Red', marker='o',linewidth = '0.0',zorder=30 )

sc7 = ax7.scatter(mchi1,neutronSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

sc7 = ax7.scatter(rejectmassSv1,rejectneutronSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc7 = ax7.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label='LUX2014')

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (GeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{n}^{SI} $ (pb)", fontsize=20)

plt.xlim([0.0,1400])
plt.ylim([1e-14,1e-7])

#plt.plot([0, 70], [0.09488, 0.09488], 'k--')
#plt.plot([0, 70], [0.14232, 0.14232], 'k--')
#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax7.xaxis.set_major_locator(MultipleLocator(200))
ax7.xaxis.set_minor_locator(MultipleLocator(50))

#ax7.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax7.tick_params(which='both', direction='out')

plt.legend(loc='upper left',frameon=False)

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutroncross_mchi1.eps')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax8 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc8 = ax8.scatter(massSv1/1000., relic, c=SvRight*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar8 = plt.colorbar(sc8, format = "%.0f")
cbar8.set_label(r"$\displaystyle \widetilde{\nu}_R $ content (\%)", fontsize=20)

ax8.axis([0.,3.5,1e-3,1e4])
cbar8 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} $ (TeV) ", fontsize=20)
cbar8 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar8 = plt.xlim([-0.1,1400])
#cbar8 = plt.ylim([1e-10,1e-5])

plt.plot([0., 3.5], [0.09, 0.09], 'k--')
plt.plot([0., 3.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax8.xaxis.set_major_locator(MultipleLocator(0.5))
ax8.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax8.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax8.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_sneutrino_rightcontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax9 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc9 = ax9.scatter(massSv1/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar9 = plt.colorbar(sc9, format = "%.0f")
cbar9.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax9.axis([0.,3.5,1e-3,1e4])
cbar9 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} $ (TeV) ", fontsize=20)
cbar9 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar9 = plt.xlim([-0.1,1400])
#cbar9 = plt.ylim([1e-10,1e-5])

plt.plot([0., 3.5], [0.09, 0.09], 'k--')
plt.plot([0., 3.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax9.xaxis.set_major_locator(MultipleLocator(0.5))
ax9.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax9.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax9.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_sneutrino_leftcontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax10 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc10 = ax10.scatter(massSv1/1000., relic, c=Scalar*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar10 = plt.colorbar(sc10, format = "%.0f")
cbar10.set_label(r"$\displaystyle S $ content (\%)", fontsize=20)

ax10.axis([0.,3.5,1e-3,1e4])
cbar10 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} $ (TeV) ", fontsize=20)
cbar10 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar10 = plt.xlim([-0.1,1400])
#cbar10 = plt.ylim([1e-10,1e-5])

plt.plot([0., 3.5], [0.09, 0.09], 'k--')
plt.plot([0., 3.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax10.xaxis.set_major_locator(MultipleLocator(0.5))
ax10.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax10.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax10.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_sneutrino_Scontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax11 = plt.subplots()

MSSMLIKE=(SCALARMIX21**2)+(SCALARMIX22**2)
INTERAC=(SCALARMIX23**2)+(SCALARMIX24**2)

sc11 = ax11.scatter(masshh1, masshh2, c=INTERAC*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar11 = plt.colorbar(sc11, format = "%.0f")
cbar11.set_label(r"$\displaystyle h_{2} $ Singlet Higgs Fields Content (\%)", fontsize=20)

#ax11.axis([120,130,100,600])
cbar11 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar11 = plt.ylabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)


#plt.plot([0, 1.4], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1.4], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax11.xaxis.set_major_locator(MultipleLocator(2))
ax11.xaxis.set_minor_locator(MultipleLocator(1))

ax11.yaxis.set_major_locator(MultipleLocator(100))
ax11.yaxis.set_minor_locator(MultipleLocator(25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax11.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/h2_Singlet_content.eps')   # save the figure to file
plt.close(fig)

###############################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax13 = plt.subplots()

MSSMLIKE=(SCALARMIX11**2)+(SCALARMIX12**2)
INTERAC=(SCALARMIX13**2)+(SCALARMIX14**2)

sc13 = ax13.scatter(masshh1, masshh2, c=MSSMLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar13 = plt.colorbar(sc13, format = "%.0f")
cbar13.set_label(r"$\displaystyle h_{1} $ Doublet Higgs Fields Content (\%)", fontsize=20)

#ax13.axis([120,130,100,600])
cbar13 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar13 = plt.ylabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)


#plt.plot([0, 1.4], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1.4], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax13.xaxis.set_major_locator(MultipleLocator(2))
ax13.xaxis.set_minor_locator(MultipleLocator(1))

ax13.yaxis.set_major_locator(MultipleLocator(100))
ax13.yaxis.set_minor_locator(MultipleLocator(25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax13.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/h1_MSSMlike_content.eps')   # save the figure to file
plt.close(fig)

#################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax15 = plt.subplots()

MSSMLIKE=(PSEUDOSCALARMIX31**2)+(PSEUDOSCALARMIX32**2)
SINGLETLIKE=(PSEUDOSCALARMIX33**2)+(PSEUDOSCALARMIX34**2)

sc15 = ax15.scatter(mchi1/1000., massAh3/1000., c=MSSMLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

x = np.arange(0, 1500.0, 0.1)
y = 2*x
ax15.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

cbar15 = plt.colorbar(sc15, format = "%.0f")
cbar15.set_label(r"$\displaystyle A_1 $ (Doublet) content (\%)", fontsize=20)

ax15.axis([0.,1.4,0,7])
cbar15 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
cbar15 = plt.ylabel(r"$\displaystyle m_{A_{1}} $ (TeV) ", fontsize=20)

#cbar10 = plt.xlim([-0.1,1400])
#cbar10 = plt.ylim([1e-10,1e-5])

#plt.plot([0, 1400], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1400], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax15.xaxis.set_major_locator(MultipleLocator(0.2))
ax15.xaxis.set_minor_locator(MultipleLocator(0.05))

ax15.yaxis.set_major_locator(MultipleLocator(1))
ax15.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax15.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_A1_doubletlike.eps')   # save the figure to file
plt.close(fig)

#################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax16 = plt.subplots()

MSSMLIKE=(PSEUDOSCALARMIX41**2)+(PSEUDOSCALARMIX42**2)
SINGLETLIKE=(PSEUDOSCALARMIX43**2)+(PSEUDOSCALARMIX44**2)

sc16 = ax16.scatter(mchi1/1000., massAh4/1000., c=SINGLETLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar16 = plt.colorbar(sc16, format = "%.0f")
cbar16.set_label(r"$\displaystyle A_2 $ (Singlet) content (\%)", fontsize=20)

ax16.axis([0.,1.4,0,11])
cbar16 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
cbar16 = plt.ylabel(r"$\displaystyle m_{A_{2}} $ (TeV) ", fontsize=20)

xx = np.arange(0, 1500.0, 0.1)
yy = 2*xx
ax16.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax16.xaxis.set_major_locator(MultipleLocator(0.2))
ax16.xaxis.set_minor_locator(MultipleLocator(0.05))

ax16.yaxis.set_major_locator(MultipleLocator(1))
ax16.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax16.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_A2_singletlike.eps')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax17 = plt.subplots()

col = NMIX15**2

sc17 = ax17.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar17 = plt.colorbar(sc17, format = "%.0f")
cbar17.set_label(r"$\displaystyle \widetilde{B}_{R} $ Content (\%) ", fontsize=20)
ax17.axis([0.2,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.2, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.2, 1.4], [0.14, 0.14], 'k--')

ax17.xaxis.set_major_locator(MultipleLocator(0.2))
ax17.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax17.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax17.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_B_R_content.eps')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax18 = plt.subplots()

col = (NMIX13**2)+(NMIX14**2)

sc18 = ax18.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar18 = plt.colorbar(sc18, format = "%.0f")
cbar18.set_label(r"$\displaystyle \widetilde{H} $ Content (\%) ", fontsize=20)
ax18.axis([0.2,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.2, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.2, 1.4], [0.14, 0.14], 'k--')

ax18.xaxis.set_major_locator(MultipleLocator(0.2))
ax18.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax18.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax18.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_H_content.eps')   # save the figure to file
plt.close(fig)


###############################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax19 = plt.subplots()

col = (NMIX16**2)+(NMIX17**2)

sc19 = ax19.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar19 = plt.colorbar(sc19, format = "%.0f")
cbar19.set_label(r"$\displaystyle \widetilde{H}_R $ Content (\%) ", fontsize=20)
ax19.axis([0.2,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.2, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.2, 1.4], [0.14, 0.14], 'k--')

ax19.xaxis.set_major_locator(MultipleLocator(0.2))
ax19.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax19.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax19.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_H_R_content.eps')   # save the figure to file
plt.close(fig)

###############################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax20 = plt.subplots()

col = NMIX11**2

sc20 = ax20.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar20 = plt.colorbar(sc20, format = "%.0f")
cbar20.set_label(r"$\displaystyle \widetilde{B} $ Content (\%) ", fontsize=20)
ax20.axis([0.2,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.2, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.2, 1.4], [0.14, 0.14], 'k--')

ax20.xaxis.set_major_locator(MultipleLocator(0.2))
ax20.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax20.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax20.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/neutralino_B_content.eps')   # save the figure to file
plt.close(fig)


################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax21 = plt.subplots()

SvLeft=(SNUMIX21**2)+(SNUMIX22**2)+(SNUMIX23**2)
SvRight=(SNUMIX24**2)+(SNUMIX25**2)+(SNUMIX26**2)
Scalar=(SNUMIX27**2)+(SNUMIX28**2)+(SNUMIX29**2)

sc21 = ax21.scatter(massSv2/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar21 = plt.colorbar(sc21, format = "%.0f")
cbar21.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax21.axis([0.,3.5,1e-3,1e4])
cbar21 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_2}} $ (TeV) ", fontsize=20)
cbar21 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0., 3.5], [0.09, 0.09], 'k--')
plt.plot([0., 3.5], [0.14, 0.14], 'k--')

ax21.xaxis.set_major_locator(MultipleLocator(0.5))
ax21.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax21.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax21.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_Sv2_leftcontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax22 = plt.subplots()

SvLeft=(SNUMIX31**2)+(SNUMIX32**2)+(SNUMIX33**2)
SvRight=(SNUMIX34**2)+(SNUMIX35**2)+(SNUMIX36**2)
Scalar=(SNUMIX37**2)+(SNUMIX38**2)+(SNUMIX39**2)

sc22 = ax22.scatter(massSv3/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar22 = plt.colorbar(sc22, format = "%.0f")
cbar22.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax22.axis([0.,3.5,1e-3,1e4])
cbar22 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_3}} $ (TeV) ", fontsize=20)
cbar22 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0., 3.5], [0.09, 0.09], 'k--')
plt.plot([0., 3.5], [0.14, 0.14], 'k--')

ax22.xaxis.set_major_locator(MultipleLocator(0.5))
ax22.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax22.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax22.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_Sv3_leftcontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax23 = plt.subplots()

SvLeft=(SNUMIX41**2)+(SNUMIX42**2)+(SNUMIX43**2)
SvRight=(SNUMIX44**2)+(SNUMIX45**2)+(SNUMIX46**2)
Scalar=(SNUMIX47**2)+(SNUMIX48**2)+(SNUMIX49**2)

sc23 = ax23.scatter(massSv4/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar23 = plt.colorbar(sc23, format = "%.0f")
cbar23.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax23.axis([0.5,3.5,1e-3,1e4])
cbar23 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_4}} $ (TeV) ", fontsize=20)
cbar23 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.5, 3.5], [0.09, 0.09], 'k--')
plt.plot([0.5, 3.5], [0.14, 0.14], 'k--')

ax23.xaxis.set_major_locator(MultipleLocator(0.5))
ax23.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax23.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax23.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_Sv4_leftcontent.eps')   # save the figure to file
plt.close(fig)


################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax24 = plt.subplots()

SvLeft=(SNUMIX51**2)+(SNUMIX52**2)+(SNUMIX53**2)
SvRight=(SNUMIX54**2)+(SNUMIX55**2)+(SNUMIX56**2)
Scalar=(SNUMIX57**2)+(SNUMIX58**2)+(SNUMIX59**2)

sc24 = ax24.scatter(massSv5/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar24 = plt.colorbar(sc24, format = "%.0f")
cbar24.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax24.axis([0.5,4.0,1e-3,1e4])
cbar24 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_5}} $ (TeV) ", fontsize=20)
cbar24 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.5, 4.0], [0.09, 0.09], 'k--')
plt.plot([0.5, 4.0], [0.14, 0.14], 'k--')

ax24.xaxis.set_major_locator(MultipleLocator(0.5))
ax24.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax24.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax24.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_Sv5_leftcontent.eps')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax25 = plt.subplots()

SvLeft=(SNUMIX61**2)+(SNUMIX62**2)+(SNUMIX63**2)
SvRight=(SNUMIX64**2)+(SNUMIX65**2)+(SNUMIX66**2)
Scalar=(SNUMIX67**2)+(SNUMIX68**2)+(SNUMIX69**2)

sc25 = ax25.scatter(massSv6/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar25 = plt.colorbar(sc24, format = "%.0f")
cbar25.set_label(r"$\displaystyle \widetilde{\nu}_L $ content (\%)", fontsize=20)

ax25.axis([0.5,4.0,1e-3,1e4])
cbar25 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_6}} $ (TeV) ", fontsize=20)
cbar25 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.5, 4.0], [0.09, 0.09], 'k--')
plt.plot([0.5, 4.0], [0.14, 0.14], 'k--')

ax25.xaxis.set_major_locator(MultipleLocator(0.5))
ax25.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax25.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax25.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/relic_Sv6_leftcontent.eps')   # save the figure to file
plt.close(fig)


###################################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax26 = plt.subplots()

MSSMLIKE=(SCALARMIX31**2)+(SCALARMIX32**2)
INTERAC=(SCALARMIX33**2)+(SCALARMIX34**2)

sc26 = ax26.scatter(masshh1, masshh3/1000., c=MSSMLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar26 = plt.colorbar(sc26, format = "%.0f")
cbar26.set_label(r"$\displaystyle h_{3} $ Doublet Higgs Fields Content (\%)", fontsize=20)

ax26.axis([120,130,0.5,7])
cbar26 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar26 = plt.ylabel(r"$\displaystyle m_{h_3} $ (GeV) ", fontsize=20)


ax26.xaxis.set_major_locator(MultipleLocator(2))
ax26.xaxis.set_minor_locator(MultipleLocator(1))

ax26.yaxis.set_major_locator(MultipleLocator(1))
ax26.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax26.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/h3_Doublet_content.eps')   # save the figure to file
plt.close(fig)

###################################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax27 = plt.subplots()

MSSMLIKE=(SCALARMIX41**2)+(SCALARMIX42**2)
INTERAC=(SCALARMIX43**2)+(SCALARMIX44**2)

sc27 = ax27.scatter(masshh1, masshh4/1000., c=INTERAC*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar27 = plt.colorbar(sc27, format = "%.0f")
cbar27.set_label(r"$\displaystyle h_{4} $ Singlet Higgs Fields Content (\%)", fontsize=20)

ax27.axis([120,130,1,10])
cbar27 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar27 = plt.ylabel(r"$\displaystyle m_{h_4} $ (GeV) ", fontsize=20)

ax27.xaxis.set_major_locator(MultipleLocator(2))
ax27.xaxis.set_minor_locator(MultipleLocator(1))

ax27.yaxis.set_major_locator(MultipleLocator(1))
ax27.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax27.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/h4_Singlet_content.eps')   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax28 = plt.subplots()

sc28 = ax28.scatter(relicmchi1/1000.,relicIcecube, s=10, c='Red' ,linewidth = '0.0',marker='o',zorder=30 )

sc28 = ax28.scatter(mchi1/1000.,Icecube, s=10, c='Blue' ,linewidth = '0.0',marker='o',zorder=20 )

sc28 = ax28.scatter(rejectmchi1/1000.,rejectIcecube, s=10, c='Grey' ,linewidth = '0.0',marker='o',zorder=10 )

ax28.axis([0.,1.4,-0.03,14])

cbar28 = plt.ylabel(r"Icecube22 Exclusion CLs for $\displaystyle \nu$ flux (\%)", fontsize=18)
cbar28 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)

#ax28.text(1.42,66,r"$\displaystyle \sigma_1$",fontsize=20)

#plt.plot([0,1.4], [68, 68], 'k--')

ax28.xaxis.set_major_locator(MultipleLocator(0.2))
ax28.xaxis.set_minor_locator(MultipleLocator(0.05))

ax28.yaxis.set_major_locator(MultipleLocator(2.0))
ax28.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax28.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/icecube_mchi1.eps')   # save the figure to file
plt.close(fig)

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax29 = plt.subplots()

MSSMLIKE=(SCALARMIX11**2)+(SCALARMIX12**2)
INTERAC=(SCALARMIX13**2)+(SCALARMIX14**2)

sc29 = ax29.scatter(masshh1,LHC8gluonfusionh1, c=MSSMLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar29 = plt.colorbar(sc29, format = "%.0f")
cbar29.set_label(r"$\displaystyle h_{1} $ Doublet Higgs Fields Content (\%)", fontsize=20)

ax29.axis([121,129,13,21])
cbar29 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar29 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(gg \rightarrow h_1) $ (pb) ", fontsize=20)

ax29.xaxis.set_major_locator(MultipleLocator(1))
ax29.xaxis.set_minor_locator(MultipleLocator(0.5))

ax29.yaxis.set_major_locator(MultipleLocator(1))
ax29.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax29.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/gluonfusionh1_Doublet_content.eps')   # save the figure to file
plt.close(fig)

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax30 = plt.subplots()

MSSMLIKE=(SCALARMIX21**2)+(SCALARMIX22**2)
INTERAC=(SCALARMIX23**2)+(SCALARMIX24**2)

sc30 = ax30.scatter(masshh2,LHC8gluonfusionh2, c=INTERAC*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar30 = plt.colorbar(sc30, format = "%.0f")
cbar30.set_label(r"$\displaystyle h_{2} $ Singlet Higgs Fields Content (\%)", fontsize=20)

ax30.axis([100,300,-0.05,16])
cbar30 = plt.xlabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)
cbar30 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(gg \rightarrow h_2) $ (pb) ", fontsize=20)

ax30.xaxis.set_major_locator(MultipleLocator(50))
ax30.xaxis.set_minor_locator(MultipleLocator(10))

ax30.yaxis.set_major_locator(MultipleLocator(2.0))
ax30.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax30.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/gluonfusionh2_Singlet_content.eps')   # save the figure to file
plt.close(fig)

#############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax31 = plt.subplots()

MSSMLIKE=(SCALARMIX11**2)+(SCALARMIX12**2)
INTERAC=(SCALARMIX13**2)+(SCALARMIX14**2)

sc31 = ax31.scatter(masshh1,LHC8vectorfusionh1, c=MSSMLIKE*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar31 = plt.colorbar(sc31, format = "%.0f")
cbar31.set_label(r"$\displaystyle h_{1} $ Doublet Higgs Fields Content (\%)", fontsize=20)

ax31.axis([121,129,1.0,1.7])
cbar31 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar31 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(VB \rightarrow h_1) $ (pb) ", fontsize=20)

ax31.xaxis.set_major_locator(MultipleLocator(1))
ax31.xaxis.set_minor_locator(MultipleLocator(0.5))

ax31.yaxis.set_major_locator(MultipleLocator(0.1))
ax31.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax31.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/vectorfusionh1_Doublet_content.eps')   # save the figure to file
plt.close(fig)

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax32 = plt.subplots()

MSSMLIKE=(SCALARMIX21**2)+(SCALARMIX22**2)
INTERAC=(SCALARMIX23**2)+(SCALARMIX24**2)

sc32 = ax32.scatter(masshh2,LHC8vectorfusionh2, c=INTERAC*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar32 = plt.colorbar(sc32, format = "%.0f")
cbar32.set_label(r"$\displaystyle h_{2} $ Singlet Higgs Fields Content (\%)", fontsize=20)

ax32.axis([100,300,-0.02,0.35])
cbar32 = plt.xlabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)
cbar32 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(VB \rightarrow h_2) $ (pb) ", fontsize=20)

ax32.xaxis.set_major_locator(MultipleLocator(50))
ax32.xaxis.set_minor_locator(MultipleLocator(10))

ax32.yaxis.set_major_locator(MultipleLocator(0.05))
ax32.yaxis.set_minor_locator(MultipleLocator(0.01))

# Set both ticks to be outside
ax32.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/vectorfusionh2_Singlet_content.eps')   # save the figure to file
plt.close(fig)

#############################################################################

fig, ax33 = plt.subplots()

ax33.scatter(relicA0/relicm0, relicm0/1000., s=10, c='Red', marker='o',linewidth = '0.0',zorder=30 )

ax33.scatter(A0/m0, m0/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax33.scatter(rejectA0/rejectm0, rejectm0/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax33.axis([-3.,3.,0.,3.])
plt.xlabel(r"$\displaystyle A_{0}/m_{0} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{0} $ (TeV)", fontsize=20)

ax33.xaxis.set_major_locator(MultipleLocator(1))
ax33.xaxis.set_minor_locator(MultipleLocator(0.2))

ax33.yaxis.set_major_locator(MultipleLocator(0.5))
ax33.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax33.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/m0_A0m0.eps')   # save the figure to file
plt.close(fig)

##############################################################################

fig, ax34 = plt.subplots()

ax34.scatter(relictanb, relicm0/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax34.scatter(tanb, m0/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax34.scatter(rejecttanb, rejectm0/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax34.axis([0.,60.,0.,3.])
plt.xlabel(r"$\displaystyle tan\beta $ ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{0} $ (TeV)", fontsize=20)

ax34.xaxis.set_major_locator(MultipleLocator(10.))
ax34.xaxis.set_minor_locator(MultipleLocator(2.))

ax34.yaxis.set_major_locator(MultipleLocator(0.5))
ax34.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax34.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/m0_tanb.eps')   # save the figure to file
plt.close(fig)

###############################################################################

fig, ax35 = plt.subplots()

ax35.scatter(relicmhf/1000., relicm0/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax35.scatter(mhf/1000., m0/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax35.scatter(rejectmhf/1000., rejectm0/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax35.axis([0.,3.,0.,3.])
plt.xlabel(r"$\displaystyle M_{1/2} $ (TeV)", fontsize=20)
plt.ylabel(r"$\displaystyle m_{0} $ (TeV)", fontsize=20)

ax35.xaxis.set_major_locator(MultipleLocator(0.5))
ax35.xaxis.set_minor_locator(MultipleLocator(0.1))

ax35.yaxis.set_major_locator(MultipleLocator(0.5))
ax35.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax35.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/m0_mhf.eps')   # save the figure to file
plt.close(fig)

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax36 = plt.subplots()

meff= (massAh3*massAh4)/(massAh3+massAh4)

sc36 = ax36.scatter(meff/1000,Bsmumu, c=tanb, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar36 = plt.colorbar(sc36, format = "%.0f")

cbar36.set_label(r"$\displaystyle tan\beta $", fontsize=20)

ax36.axis([0,4.0,2.5E-9,6.5E-9])
cbar36 = plt.xlabel(r"$\displaystyle m_A^{eff} $ (TeV) ", fontsize=20)
cbar36 = plt.ylabel(r"$\displaystyle B_{s}^0 \rightarrow \mu^{+} \mu^{-} $ ", fontsize=20)

ax36.xaxis.set_major_locator(MultipleLocator(0.5))
ax36.xaxis.set_minor_locator(MultipleLocator(0.1))

ax36.yaxis.set_major_locator(MultipleLocator(0.5E-9))
ax36.yaxis.set_minor_locator(MultipleLocator(0.1E-9))

# Set both ticks to be outside
ax36.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/Bsmumu_Aefftanb.eps')   # save the figure to file
plt.close(fig)

#################################################################################

fig, ax37 = plt.subplots()

ax37.scatter(relicm0/1000., relicDAMU*10**10, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax37.scatter(m0/1000, DAMU*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax37.scatter(rejectm0/1000, rejectDAMU*10**10, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax37.axis([0,3.0,0.0,60])
plt.xlabel(r"$\displaystyle m_0 $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax37.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax37.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax37.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax37.text(3.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax37.text(3.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax37.text(3.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax37.xaxis.set_major_locator(MultipleLocator(0.5))
ax37.xaxis.set_minor_locator(MultipleLocator(0.1))

ax37.yaxis.set_major_locator(MultipleLocator(5))
ax37.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax37.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/DAMU_m0.eps')   # save the figure to file
plt.close(fig)

################################################################################

fig, ax38 = plt.subplots()

ax38.scatter(relicmhf/1000., relicDAMU*10**10, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax38.scatter(mhf/1000, DAMU*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax38.scatter(rejectmhf/1000, rejectDAMU*10**10, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax38.axis([0.5,3.0,0.0,60])
plt.xlabel(r"$\displaystyle M_{1/2} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax38.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax38.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax38.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax38.text(3.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax38.text(3.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax38.text(3.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax38.xaxis.set_major_locator(MultipleLocator(0.5))
ax38.xaxis.set_minor_locator(MultipleLocator(0.1))

ax38.yaxis.set_major_locator(MultipleLocator(5))
ax38.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax38.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/DAMU_mhf.eps')   # save the figure to file
plt.close(fig)

################################################################################

fig, ax39 = plt.subplots()

ax39.scatter(relictanb, relicDAMU*10**10, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax39.scatter(tanb, DAMU*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax39.scatter(rejecttanb, rejectDAMU*10**10, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax39.axis([0,60.0,0.0,60.0])
plt.xlabel(r"$\displaystyle tan\beta $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax39.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax39.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax39.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax39.text(61., 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax39.text(61., 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax39.text(61., 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax39.xaxis.set_major_locator(MultipleLocator(10.0))
ax39.xaxis.set_minor_locator(MultipleLocator(2.0))

ax39.yaxis.set_major_locator(MultipleLocator(5))
ax39.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax39.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/DAMU_tanb.eps')   # save the figure to file
plt.close(fig)

##############################################################################

fig, ax40 = plt.subplots()

ax40.scatter(relictanb, relicmhf/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax40.scatter(tanb, mhf/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax40.scatter(rejecttanb, rejectmhf/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax40.axis([0,60.0,0.0,3.0])
plt.xlabel(r"$\displaystyle tan\beta $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle M_{1/2} $ (TeV) ", fontsize=20)

ax40.xaxis.set_major_locator(MultipleLocator(10.0))
ax40.xaxis.set_minor_locator(MultipleLocator(2.0))

ax40.yaxis.set_major_locator(MultipleLocator(0.5))
ax40.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax40.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mhf_tanb.eps')   # save the figure to file
plt.close(fig)

###############################################################################

fig, ax41 = plt.subplots()

ax41.scatter(relicmasshh1, relicmasshh2, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax41.scatter(masshh1, masshh2, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax41.scatter(rejectmasshh1, rejectmasshh2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(120., 130., 0.1)
y = x
ax41.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax41.axis([120.,130.,100.0,200.0])
plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)

ax41.xaxis.set_major_locator(MultipleLocator(2.0))
ax41.xaxis.set_minor_locator(MultipleLocator(0.5))

ax41.yaxis.set_major_locator(MultipleLocator(25.))
ax41.yaxis.set_minor_locator(MultipleLocator(5.))

# Set both ticks to be outside
ax41.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/masshh2_mashh1.eps')   # save the figure to file
plt.close(fig)

#############################################################################

fig, ax42 = plt.subplots()

ax42.scatter(relicmchi1/1000., relicgluino/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax42.scatter(mchi1/1000., gluino/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax42.scatter(rejectmchi1/1000., rejectgluino/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax42.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax42.axis([0.,1.4,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{g}} $ (TeV) ", fontsize=20)

ax42.xaxis.set_major_locator(MultipleLocator(0.20))
ax42.xaxis.set_minor_locator(MultipleLocator(0.05))

ax42.yaxis.set_major_locator(MultipleLocator(1.))
ax42.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax42.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/gluino_mchi1.eps')   # save the figure to file
plt.close(fig)

###########################################################################

fig, ax43 = plt.subplots()

ax43.scatter(relicmchi1/1000., relicmassSv1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax43.scatter(mchi1/1000., massSv1/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax43.scatter(rejectmchi1/1000., rejectmassSv1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax43.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax43.axis([0.,1.4,0.,3.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\nu}_1} $ (TeV) ", fontsize=20)

ax43.xaxis.set_major_locator(MultipleLocator(0.20))
ax43.xaxis.set_minor_locator(MultipleLocator(0.05))

ax43.yaxis.set_major_locator(MultipleLocator(0.5))
ax43.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax43.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_massSv1.eps')   # save the figure to file
plt.close(fig)

#############################################################################

fig, ax44 = plt.subplots()

ax44.scatter(relicmchi1/1000., relicmcha1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax44.scatter(mchi1/1000., mcha1/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax44.scatter(rejectmchi1/1000., rejectmcha1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 2.5, 0.01)
#y = x
#ax44.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = xx
y2 = xx+0.080385
#y1 = xx+(xx*0.08)
#y2 = xx-(xx*0.08)
#ax44.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax44.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax44.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax44.axis([0.,1.4,0.,2.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_1^{\pm}} $ (TeV) ", fontsize=20)

ax44.xaxis.set_major_locator(MultipleLocator(0.20))
ax44.xaxis.set_minor_locator(MultipleLocator(0.05))

ax44.yaxis.set_major_locator(MultipleLocator(0.20))
ax44.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax44.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mcha1_mchi1.eps')   # save the figure to file
plt.close(fig)

#############################################################################

fig, ax45 = plt.subplots()

ax45.scatter(relicmchi1/1000., relicmassAh3/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax45.scatter(mchi1/1000., massAh3/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax45.scatter(rejectmchi1/1000., rejectmassAh3/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax45.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 1.4, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax45.plot(x, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax45.plot(x, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax45.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax45.axis([0.,1.4,0.,6.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{A_1} $ (TeV) ", fontsize=20)

ax45.xaxis.set_major_locator(MultipleLocator(0.20))
ax45.xaxis.set_minor_locator(MultipleLocator(0.05))

ax45.yaxis.set_major_locator(MultipleLocator(1.0))
ax45.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax45.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_massAh3.eps')   # save the figure to file
plt.close(fig)

################################################################################

fig, ax46 = plt.subplots()

ax46.scatter(relicmchi1/1000., relicmassAh4/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax46.scatter(mchi1/1000., massAh4/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax46.scatter(rejectmchi1/1000., rejectmassAh4/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = 2*x
ax46.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

#xx = np.arange(0, 1.4, 0.01)
#y1 = 2*xx+(2*xx*0.08)
#y2 = 2*xx-(2*xx*0.08)
#ax46.plot(x, y1, color='lime',lw=2, zorder=40,alpha=0.5)
#ax46.plot(x, y2, color='lime',lw=2, zorder=40,alpha=0.5)

#ax46.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax46.axis([0.,1.4,0.,10.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{A_2} $ (TeV) ", fontsize=20)

ax46.xaxis.set_major_locator(MultipleLocator(0.20))
ax46.xaxis.set_minor_locator(MultipleLocator(0.05))

ax46.yaxis.set_major_locator(MultipleLocator(1.0))
ax46.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax46.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_massAh4.eps')   # save the figure to file
plt.close(fig)

#################################################################################

fig, ax47 = plt.subplots()

ax47.scatter(relicmchi1/1000., relicmasstau1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax47.scatter(mchi1/1000., masstau1/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax47.scatter(rejectmchi1/1000., rejectmasstau1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax47.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax47.axis([0.,1.4,0.,3.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\tau}_1} $ (TeV) ", fontsize=20)

ax47.xaxis.set_major_locator(MultipleLocator(0.20))
ax47.xaxis.set_minor_locator(MultipleLocator(0.05))

ax47.yaxis.set_major_locator(MultipleLocator(0.5))
ax47.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax47.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_massstau.eps')   # save the figure to file
plt.close(fig)

##################################################################################

fig, ax48 = plt.subplots()

ax48.scatter(relicmchi1/1000., relicmasst1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax48.scatter(mchi1/1000., masst1/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax48.scatter(rejectmchi1/1000., rejectmasst1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax48.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax48.axis([0.,1.4,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{t}_1} $ (TeV) ", fontsize=20)

ax48.xaxis.set_major_locator(MultipleLocator(0.20))
ax48.xaxis.set_minor_locator(MultipleLocator(0.05))

ax48.yaxis.set_major_locator(MultipleLocator(1.))
ax48.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax48.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_masst1.eps')   # save the figure to file
plt.close(fig)

################################################################################

fig, ax49 = plt.subplots()

ax49.scatter(relicmchi1/1000., relicmassb1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax49.scatter(mchi1/1000., massb1/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax49.scatter(rejectmchi1/1000., rejectmassb1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = x
ax49.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax49.axis([0.,1.4,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{b}_1} $ (TeV) ", fontsize=20)

ax49.xaxis.set_major_locator(MultipleLocator(0.20))
ax49.xaxis.set_minor_locator(MultipleLocator(0.05))

ax49.yaxis.set_major_locator(MultipleLocator(1.))
ax49.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax49.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/mchi1_massb1.eps')   # save the figure to file
plt.close(fig)

##################################################################################

fig, ax50 = plt.subplots()

ax50.scatter(relicmassAh3/1000., relicmasshh3/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax50.scatter(massAh3/1000., masshh3/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax50.scatter(rejectmassAh3/1000., rejectmasshh3/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 1.4, 0.01)
#y = x
#ax50.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax50.axis([0.,5.,0.,5.])
plt.xlabel(r"$\displaystyle m_{A_1} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_3} $ (TeV) ", fontsize=20)

ax50.xaxis.set_major_locator(MultipleLocator(1.))
ax50.xaxis.set_minor_locator(MultipleLocator(0.2))

ax50.yaxis.set_major_locator(MultipleLocator(1.))
ax50.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax50.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/massAh3_massh3.eps')   # save the figure to file
plt.close(fig)

###################################################################################

fig, ax51 = plt.subplots()

ax51.scatter(relicvR/1000., relicMSUSY/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax51.scatter(vR/1000., MSUSY/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax51.scatter(rejectvR/1000., rejectMSUSY/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(2., 6., 0.01)
y = x
ax51.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax51.axis([2.,20.,0.,6.])
plt.xlabel(r"$\displaystyle \nu_{R} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle M_{SUSY} $ (TeV) ", fontsize=20)

ax51.xaxis.set_major_locator(MultipleLocator(2.))
ax51.xaxis.set_minor_locator(MultipleLocator(0.5))

ax51.yaxis.set_major_locator(MultipleLocator(1.))
ax51.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax51.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/MSUSY_vR.eps')   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax52 = plt.subplots()

ax52.scatter(relicgluino/1000., relicmassd1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax52.scatter(gluino/1000., massd1/1000., s=20, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax52.scatter(rejectgluino/1000., rejectmassd1/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(3., 8., 0.01)
#y = x
#ax52.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax52.axis([0.,6.,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{g}} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{q}} $ (TeV) ", fontsize=20)

ax52.xaxis.set_major_locator(MultipleLocator(1.))
ax52.xaxis.set_minor_locator(MultipleLocator(0.2))

ax52.yaxis.set_major_locator(MultipleLocator(1.))
ax52.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax52.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/gluino_squarks.eps')   # save the figure to file
plt.close(fig)

##########################################################################

fig, ax53 = plt.subplots()

ax53.scatter(relicmassmu1/1000., relicmassmu2/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax53.scatter(massmu1/1000., massmu2/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax53.scatter(rejectmassmu1/1000., rejectmassmu2/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0., 5., 0.01)
y = x
ax53.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax53.axis([0.,5.,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\mu}_1} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\mu}_2} $ (TeV) ", fontsize=20)

ax53.xaxis.set_major_locator(MultipleLocator(1.))
ax53.xaxis.set_minor_locator(MultipleLocator(0.2))

ax53.yaxis.set_major_locator(MultipleLocator(1.))
ax53.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax53.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/massmu2_massmu1.eps')   # save the figure to file
plt.close(fig)

############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax54 = plt.subplots()

sc54 = ax54.scatter(massmu1/1000,massmu2/1000., c=DAMU*10**10, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar54 = plt.colorbar(sc54, format = "%.0f")

cbar54.set_label(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $", fontsize=20)

x = np.arange(0., 5., 0.01)
y = x
ax54.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax54.axis([0.,5.,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\mu}_1} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\mu}_2} $ (TeV) ", fontsize=20)

ax54.xaxis.set_major_locator(MultipleLocator(1.))
ax54.xaxis.set_minor_locator(MultipleLocator(0.2))

ax54.yaxis.set_major_locator(MultipleLocator(1.))
ax54.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax54.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/massmu2_massmu1_DAMU.eps')   # save the figure to file
plt.close(fig)

############################################################################

fig, ax55 = plt.subplots()

ax55.scatter(relicvR/1000., relicmassVZR/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax55.scatter(vR/1000., massVZR/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax55.scatter(rejectvR/1000., rejectmassVZR/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0., 5., 0.01)
#y = x
#ax55.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax55.axis([2.,20.,1.,8.])
plt.xlabel(r"$\displaystyle \nu_{R} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{Z'}  $ (TeV) ", fontsize=20)

ax55.xaxis.set_major_locator(MultipleLocator(2.))
ax55.xaxis.set_minor_locator(MultipleLocator(0.5))

ax55.yaxis.set_major_locator(MultipleLocator(1.0))
ax55.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set both ticks to be outside
ax55.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/vR_massVZR.eps')   # save the figure to file
plt.close(fig)

##############################################################################

fig, ax56 = plt.subplots()

ax56.scatter(relicmchi1/1000., relicmassVZR/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax56.scatter(mchi1/1000., massVZR/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax56.scatter(rejectmchi1/1000., rejectmassVZR/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 1.4, 0.01)
y = 2*x
ax56.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

#y1 = 2*x+(2*x*0.08)
#y2 = 2*x-(2*x*0.08)
#ax56.plot(x, y1, color='lime',lw=2, zorder=40,alpha=0.5)
#ax56.plot(x, y2, color='lime',lw=2, zorder=40,alpha=0.5)

ax56.axis([0.,1.4,0.,7.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{Z'} $ (TeV) ", fontsize=20)

ax56.xaxis.set_major_locator(MultipleLocator(0.20))
ax56.xaxis.set_minor_locator(MultipleLocator(0.05))

ax56.yaxis.set_major_locator(MultipleLocator(0.5))
ax56.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax56.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/mchi1_massVZR.eps')   # save the figure to file
plt.close(fig)

#############################################################################

fig, ax57 = plt.subplots()

ax57.scatter(relicmassVZR/1000., relicmasshh2,s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax57.scatter(massVZR/1000., masshh2, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax57.scatter(rejectmassVZR/1000., rejectmasshh2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(2.5, 4.5, 0.01)
#y = x
#ax57.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

#y1 = 2*x+(2*x*0.08)
#y2 = 2*x-(2*x*0.08)
#ax56.plot(x, y1, color='lime',lw=2, zorder=40,alpha=0.5)
#ax56.plot(x, y2, color='lime',lw=2, zorder=40,alpha=0.5)

ax57.axis([2.0,7.5,0.,1000.])
plt.xlabel(r"$\displaystyle m_{Z'} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_2} $ (TeV) ", fontsize=20)

ax57.xaxis.set_major_locator(MultipleLocator(0.5))
ax57.xaxis.set_minor_locator(MultipleLocator(0.1))

ax57.yaxis.set_major_locator(MultipleLocator(100.0))
ax57.yaxis.set_minor_locator(MultipleLocator(20.0))

# Set both ticks to be outside
ax57.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/masshh2_massVZR.eps')   # save the figure to file
plt.close(fig)

#####################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax58 = plt.subplots()

sc58 = ax58.scatter(mchi1/1000.,relic, c=mcha1, cmap=cm ,s=10, linewidth = '0.0',marker='o')

cbar58 = plt.colorbar(sc58, format = "%.0f")
cbar58.set_label(r"$\displaystyle m_{\widetilde{\chi}_1^{\pm}} $ (GeV)  " , fontsize=20)

ax58.axis([0,1.4,1e-2,1e4])
cbar58 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
cbar58 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax58.xaxis.set_major_locator(MultipleLocator(0.2))
ax58.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax58.yaxis.set_major_locator(MultipleLocator(1))
#ax58.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax58.tick_params(which='both', direction='out')

plt.yscale('log')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/neut_chargino_relic.eps')   # save the figure to file
plt.close(fig)

##########################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax59 = plt.subplots()

col = NMIX15**2

sc59 = ax59.scatter(mchi1/1000., massAh3/1000., c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

x = np.arange(0, 1500.0, 0.1)
y = 2*x
ax59.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

cbar59 = plt.colorbar(sc59, format = "%.0f")
cbar59.set_label(r"$\displaystyle \widetilde{B}_{R} $ Content (\%) ", fontsize=20)

ax59.axis([0.,1.4,0,7])
cbar59 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
cbar59 = plt.ylabel(r"$\displaystyle m_{A_{1}} $ (TeV) ", fontsize=20)

#plt.plot([0, 1400], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1400], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax59.xaxis.set_major_locator(MultipleLocator(0.2))
ax59.xaxis.set_minor_locator(MultipleLocator(0.05))

ax59.yaxis.set_major_locator(MultipleLocator(1))
ax59.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax59.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/neutralino_A1_BRmixture.eps')   # save the figure to file
plt.close(fig)

##################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax60 = plt.subplots()

col = (NMIX16**2)+(NMIX17**2)

sc60 = ax60.scatter(mchi1/1000., massAh3/1000., c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

x = np.arange(0, 1500.0, 0.1)
y = 2*x
ax60.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

cbar60 = plt.colorbar(sc60, format = "%.0f")
cbar60.set_label(r"$\displaystyle \widetilde{H}_{R} $ Content (\%) ", fontsize=20)

ax60.axis([0.,1.4,0,7])
cbar60 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} $ (TeV) ", fontsize=20)
cbar60 = plt.ylabel(r"$\displaystyle m_{A_{1}} $ (TeV) ", fontsize=20)

#plt.plot([0, 1400], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1400], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax60.xaxis.set_major_locator(MultipleLocator(0.2))
ax60.xaxis.set_minor_locator(MultipleLocator(0.05))

ax60.yaxis.set_major_locator(MultipleLocator(1))
ax60.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
#plt.yscale('log')

# Set both ticks to be outside
ax60.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/neutralino_A1_HRmixture.eps')   # save the figure to file
plt.close(fig)

#####################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax61 = plt.subplots()

col = (NMIX15**2)

sc61 = ax61.scatter(mchi1/1000.,protonSI,c=col*100, cmap=cm, s=10,marker='o',linewidth = '0.0')

#sc61 = ax61.plot(LUXDATALSPMASS,LUXDATARELIC,label='LUX2014')

cbar61 = plt.colorbar(sc61, format = "%.0f")
cbar61.set_label(r"$\displaystyle \widetilde{B}_{R} $ Content (\%) ", fontsize=20)

ax61.axis([0.,1.4,1e-14,1e-7])

cbar61 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (GeV) ", fontsize=20)
cbar61 = plt.ylabel(r"$\displaystyle \sigma_{p}^{SI} $ (pb)", fontsize=20)

ax61.xaxis.set_major_locator(MultipleLocator(0.2))
ax61.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax61.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax61.tick_params(which='both', direction='out')

#plt.legend(loc='upper left',frameon=False)

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/protoncross_mchi1_BRcontent.eps')   # save the figure to file
plt.close(fig)

#######################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax62 = plt.subplots()

col = (NMIX16**2)+(NMIX17**2)

sc62 = ax62.scatter(mchi1/1000.,protonSI,c=col*100, cmap=cm, s=10,marker='o',linewidth = '0.0')

#sc62 = ax62.plot(LUXDATALSPMASS,LUXDATARELIC,label='LUX2014')

cbar62 = plt.colorbar(sc62, format = "%.0f")
cbar62.set_label(r"$\displaystyle \widetilde{H}_{R} $ Content (\%) ", fontsize=20)

ax62.axis([0.,1.4,1e-14,1e-7])

cbar62 = plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (GeV) ", fontsize=20)
cbar62 = plt.ylabel(r"$\displaystyle \sigma_{p}^{SI} $ (pb)", fontsize=20)

ax62.xaxis.set_major_locator(MultipleLocator(0.2))
ax62.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax62.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax62.tick_params(which='both', direction='out')

#plt.legend(loc='upper left',frameon=False)

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/protoncross_mchi1_HRcontent.eps')   # save the figure to file
plt.close(fig)

#####################################################################################

fig, ax63 = plt.subplots()

ax63.scatter(relictanb, relicmhf/1000.,s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax63.scatter(tanb, mhf/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax63.scatter(rejecttanb, rejectmhf/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(2.5, 4.5, 0.01)
#y = x
#ax63.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

#y1 = 2*x+(2*x*0.08)
#y2 = 2*x-(2*x*0.08)
#ax63.plot(x, y1, color='lime',lw=2, zorder=40,alpha=0.5)
#ax63.plot(x, y2, color='lime',lw=2, zorder=40,alpha=0.5)

ax63.axis([0.,60.,0.,3.])
plt.xlabel(r"$\displaystyle tan\beta $ ", fontsize=20)
plt.ylabel(r"$\displaystyle M_{1/2} $ (TeV) ", fontsize=20)

ax63.xaxis.set_major_locator(MultipleLocator(10.))
ax63.xaxis.set_minor_locator(MultipleLocator(2.))

ax63.yaxis.set_major_locator(MultipleLocator(0.5))
ax63.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax63.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/mhf_tanb.eps')   # save the figure to file
plt.close(fig)

#####################################################################################

fig, ax64 = plt.subplots()

ax64.scatter(relicmasshh1, relicLHC8gluonfusionh1, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax64.scatter(masshh1, LHC8gluonfusionh1, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax64.scatter(rejectmasshh1, rejectLHC8gluonfusionh1, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax64.axis([121,129,0,21])
cbar64 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar64 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(gg \rightarrow h_1) $ (pb) ", fontsize=20)

ax64.xaxis.set_major_locator(MultipleLocator(1))
ax64.xaxis.set_minor_locator(MultipleLocator(0.5))

ax64.yaxis.set_major_locator(MultipleLocator(1))
ax64.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax64.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/gluonfusionh1_h1.eps')   # save the figure to file
plt.close(fig)

#########################################################################################

fig, ax65 = plt.subplots()

ax65.scatter(relicmasshh2, relicLHC8gluonfusionh2, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax65.scatter(masshh2, LHC8gluonfusionh2, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax65.scatter(rejectmasshh2, rejectLHC8gluonfusionh2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax65.axis([100,300,0.,16.])
cbar65 = plt.xlabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)
cbar65 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(gg \rightarrow h_2) $ (pb) ", fontsize=20)

ax65.xaxis.set_major_locator(MultipleLocator(50))
ax65.xaxis.set_minor_locator(MultipleLocator(10))

ax65.yaxis.set_major_locator(MultipleLocator(2))
ax65.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax65.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/gluonfusionh2_h2.eps')   # save the figure to file
plt.close(fig)

##########################################################################################

fig, ax66 = plt.subplots()

ax66.scatter(relicmasshh1, relicLHC8vectorfusionh1, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax66.scatter(masshh1, LHC8vectorfusionh1, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax66.scatter(rejectmasshh1, rejectLHC8vectorfusionh1, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax66.axis([121,129,0,1.7])
cbar66 = plt.xlabel(r"$\displaystyle m_{h_1} $ (GeV) ", fontsize=20)
cbar66 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(VB \rightarrow h_1) $ (pb) ", fontsize=20)

ax66.xaxis.set_major_locator(MultipleLocator(1))
ax66.xaxis.set_minor_locator(MultipleLocator(0.5))

ax66.yaxis.set_major_locator(MultipleLocator(0.1))
ax66.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax66.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/vectorfusionh1_h1.eps')   # save the figure to file
plt.close(fig)

############################################################################################

fig, ax67 = plt.subplots()

ax67.scatter(relicmasshh2, relicLHC8vectorfusionh2, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax67.scatter(masshh2, LHC8vectorfusionh2, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax67.scatter(rejectmasshh2, rejectLHC8vectorfusionh2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax67.axis([100,300,-0.02,0.35])
cbar67 = plt.xlabel(r"$\displaystyle m_{h_2} $ (GeV) ", fontsize=20)
cbar67 = plt.ylabel(r"$\displaystyle \sigma_{LHC8}(VB \rightarrow h_2) $ (pb) ", fontsize=20)

ax67.xaxis.set_major_locator(MultipleLocator(50))
ax67.xaxis.set_minor_locator(MultipleLocator(10))

ax67.yaxis.set_major_locator(MultipleLocator(0.05))
ax67.yaxis.set_minor_locator(MultipleLocator(0.01))

# Set both ticks to be outside
ax67.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/vectorfusionh2_h2.eps')   # save the figure to file
plt.close(fig)

###########################################################################################

fig, ax68 = plt.subplots()

ax68.scatter(relicmassAh4/1000., relicmasshh4/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax68.scatter(massAh4/1000., masshh4/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax68.scatter(rejectmassAh4/1000., rejectmasshh4/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 11., 0.01)
y = x
ax68.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax68.axis([0.,11.,2.,11.])
plt.xlabel(r"$\displaystyle m_{A_2} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_4} $ (TeV) ", fontsize=20)

ax68.xaxis.set_major_locator(MultipleLocator(1.))
ax68.xaxis.set_minor_locator(MultipleLocator(0.2))

ax68.yaxis.set_major_locator(MultipleLocator(1.))
ax68.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax68.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/massAh4_massh4.eps')   # save the figure to file
plt.close(fig)

############################################################################################

fig, ax69 = plt.subplots()

ax69.scatter(relicmassVZR/1000., relicBRZpallleptons, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax69.scatter(massVZR/1000., BRZpallleptons, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

#ax69.scatter(rejectmassVZR/1000., rejectBRZpallleptons, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax69.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax69.axis([3.,7.5,25.,55.])
plt.xlabel(r"$\displaystyle m_{Z'} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR} (Z^\prime\to ll) $ (\%) ", fontsize=20)

ax69.xaxis.set_major_locator(MultipleLocator(0.5))
ax69.xaxis.set_minor_locator(MultipleLocator(0.1))

ax69.yaxis.set_major_locator(MultipleLocator(5.))
ax69.yaxis.set_minor_locator(MultipleLocator(1.))

# Set both ticks to be outside
ax69.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZll_Z.eps')   # save the figure to file
plt.close(fig)

##############################################################################################

fig, ax70 = plt.subplots()

ax70.scatter(relicmassVZR/1000., relicBRZpsleptons, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax70.scatter(massVZR/1000., BRZpsleptons, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax70.scatter(rejectmassVZR/1000., rejectBRZpsleptons, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax70.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax70.axis([3.,7.5,-0.02,16.])
plt.xlabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR}(Z^\prime\to \tilde{l} \tilde{l}) $ [\%]", fontsize=20)

ax70.xaxis.set_major_locator(MultipleLocator(0.5))
ax70.xaxis.set_minor_locator(MultipleLocator(0.1))

ax70.yaxis.set_major_locator(MultipleLocator(2.))
ax70.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax70.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZpsleptons_Zp.eps')   # save the figure to file
plt.close(fig)

###############################################################################################

fig, ax71 = plt.subplots()

ax71.scatter(relicmassVZR/1000., relicBRZXX, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax71.scatter(massVZR/1000., BRZXX, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax71.scatter(rejectmassVZR/1000., rejectBRZXX, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax71.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax71.axis([3.,7.5,-0.02,9.])
plt.xlabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR}(Z^\prime\to \widetilde{\chi} \widetilde{\chi}) $ [\%]", fontsize=20)

ax71.xaxis.set_major_locator(MultipleLocator(0.5))
ax71.xaxis.set_minor_locator(MultipleLocator(0.1))

ax71.yaxis.set_major_locator(MultipleLocator(1.))
ax71.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax71.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZpneutchar_Zp.eps')   # save the figure to file
plt.close(fig)

###############################################################################################

fig, ax72 = plt.subplots()

ax72.scatter(relicmassVZR/1000., relicBRZjets, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax72.scatter(massVZR/1000., BRZjets, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax72.scatter(rejectmassVZR/1000., rejectBRZjets, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax72.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax72.axis([3.,7.5,40.,65.])
plt.xlabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR}(Z^\prime\to jj) $ [\%]", fontsize=20)

ax72.xaxis.set_major_locator(MultipleLocator(0.5))
ax72.xaxis.set_minor_locator(MultipleLocator(0.1))

ax72.yaxis.set_major_locator(MultipleLocator(5.))
ax72.yaxis.set_minor_locator(MultipleLocator(1.))

# Set both ticks to be outside
ax72.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZpjets_Zp.eps')   # save the figure to file
plt.close(fig)

###############################################################################################

fig, ax73 = plt.subplots()

ax73.scatter(relicmassVZR/1000., relicBRZJustSMpar, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax73.scatter(massVZR/1000., BRZJustSMpar, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax73.scatter(rejectmassVZR/1000., rejectBRZJustSMpar, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax73.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax73.axis([3.,7.5,40.,65.])
plt.xlabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR}(Z^\prime\to {\rm SM}) $ [\%]", fontsize=20)

ax73.xaxis.set_major_locator(MultipleLocator(0.5))
ax73.xaxis.set_minor_locator(MultipleLocator(0.1))

ax73.yaxis.set_major_locator(MultipleLocator(5.))
ax73.yaxis.set_minor_locator(MultipleLocator(1.))

# Set both ticks to be outside
ax73.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZJustSMpar_Zp.eps')   # save the figure to file
plt.close(fig)

##############################################################################################

fig, ax74 = plt.subplots()

ax74.scatter(relicmassVZR/1000., relicBRZpSMll, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax74.scatter(massVZR/1000., BRZpSMll, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax74.scatter(rejectmassVZR/1000., rejectBRZpSMll, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax74.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax74.axis([3.,7.5,24.,38.])
plt.xlabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle {\rm BR}(Z^\prime\to l_{SM}l_{SM}) $ [\%]", fontsize=20)

ax74.xaxis.set_major_locator(MultipleLocator(0.5))
ax74.xaxis.set_minor_locator(MultipleLocator(0.1))

ax74.yaxis.set_major_locator(MultipleLocator(2.))
ax74.yaxis.set_minor_locator(MultipleLocator(0.5))

# Set both ticks to be outside
ax74.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/BRZpSMll_Zp.eps')   # save the figure to file
plt.close(fig)

##############################################################################################

fig, ax75 = plt.subplots()

ax75.scatter(relictanbp, relicmassVZR/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax75.scatter(tanbp, massVZR/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax75.scatter(rejecttanbp, rejectmassVZR/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#x = np.arange(0, 11., 0.01)
#y = x
#ax75.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

ax75.axis([0.85,1.2,0.,8.])
plt.xlabel(r"$\displaystyle tan \beta $ ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{Z^\prime} $ (TeV) ", fontsize=20)

ax75.xaxis.set_major_locator(MultipleLocator(0.05))
ax75.xaxis.set_minor_locator(MultipleLocator(0.01))

ax75.yaxis.set_major_locator(MultipleLocator(1.))
ax75.yaxis.set_minor_locator(MultipleLocator(0.25))

# Set both ticks to be outside
ax75.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/tanbp_Zp.eps')   # save the figure to file
plt.close(fig)

##############################################################################################

fig, ax76 = plt.subplots()

ax76.scatter(relicmchi1/1000., relicmcha2/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax76.scatter(mchi1/1000., mcha2/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax76.scatter(rejectmchi1/1000., rejectmcha2/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax76.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax76.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax76.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax76.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax76.axis([0.,1.4,0.,2.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_2^{\pm}} $ (TeV) ", fontsize=20)

ax76.xaxis.set_major_locator(MultipleLocator(0.20))
ax76.xaxis.set_minor_locator(MultipleLocator(0.05))

ax76.yaxis.set_major_locator(MultipleLocator(0.20))
ax76.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax76.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/mcha2_mchi1.eps')   # save the figure to file
plt.close(fig)

#################################################################################################

fig, ax77 = plt.subplots()

ax77.scatter(relicmchi1/1000., relicmchi2/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax77.scatter(mchi1/1000., mchi2/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax77.scatter(rejectmchi1/1000., rejectmchi2/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax77.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax77.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax77.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax77.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax77.axis([0.,1.4,0.,2.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_2^0} $ (TeV) ", fontsize=20)

ax77.xaxis.set_major_locator(MultipleLocator(0.20))
ax77.xaxis.set_minor_locator(MultipleLocator(0.05))

ax77.yaxis.set_major_locator(MultipleLocator(0.20))
ax77.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax77.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/mchi2_mchi1.eps')   # save the figure to file
plt.close(fig)

###############################################################################

fig, ax78 = plt.subplots()

ax78.scatter(relicmchi1/1000., relicmchi3/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax78.scatter(mchi1/1000., mchi3/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax78.scatter(rejectmchi1/1000., rejectmchi3/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax78.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax78.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax78.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax78.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax78.axis([0.,1.4,0.,2.5])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_3^0} $ (TeV) ", fontsize=20)

ax78.xaxis.set_major_locator(MultipleLocator(0.20))
ax78.xaxis.set_minor_locator(MultipleLocator(0.05))

ax78.yaxis.set_major_locator(MultipleLocator(0.20))
ax78.yaxis.set_minor_locator(MultipleLocator(0.05))

# Set both ticks to be outside
ax78.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/mchi3_mchi1.eps')   # save the figure to file
plt.close(fig)

###################################################################################

fig, ax79 = plt.subplots()

ax79.scatter(relicmchi1/1000., relicmasshh2, s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax79.scatter(mchi1/1000., masshh2, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax79.scatter(rejectmchi1/1000., rejectmasshh2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax79.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax79.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax79.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax79.fill_between(xx,y1*1000,y2*1000, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax79.axis([0.,1.4,100.,600.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_2} $ (TeV) ", fontsize=20)

ax79.xaxis.set_major_locator(MultipleLocator(0.20))
ax79.xaxis.set_minor_locator(MultipleLocator(0.05))

ax79.yaxis.set_major_locator(MultipleLocator(100.))
ax79.yaxis.set_minor_locator(MultipleLocator(25.))

# Set both ticks to be outside
ax79.tick_params(which='both', direction='out')

fig.savefig('/home/heplab/Desktop/mBLRISS/SPheno333_neutLSP/plot/tex/masshh2_mchi1.eps')   # save the figure to file
plt.close(fig)

###################################################################################

fig, ax80 = plt.subplots()

ax80.scatter(relicmchi1/1000., relicmasshh3/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax80.scatter(mchi1/1000., masshh3/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax80.scatter(rejectmchi1/1000., rejectmasshh3/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax80.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax80.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax80.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax80.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax80.axis([0.,1.4,0.,5.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_3} $ (TeV) ", fontsize=20)

ax80.xaxis.set_major_locator(MultipleLocator(0.20))
ax80.xaxis.set_minor_locator(MultipleLocator(0.05))

ax80.yaxis.set_major_locator(MultipleLocator(0.5))
ax80.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax80.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/masshh3_mchi1.eps')   # save the figure to file
plt.close(fig)

#####################################################################################

fig, ax81 = plt.subplots()

ax81.scatter(relicmchi1/1000., relicmasshh4/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax81.scatter(mchi1/1000., masshh4/1000., s=10, c='Blue',marker='o',linewidth = '0.0',zorder=20)

ax81.scatter(rejectmchi1/1000., rejectmasshh4/1000., s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

x = np.arange(0, 2.5, 0.01)
y = x
ax81.plot(x, y, color='lime',lw=2, zorder=40,alpha=0.5)

xx = np.arange(0, 2.5, 0.01)
y1 = 2*xx+(2*xx*0.08)
y2 = 2*xx-(2*xx*0.08)
#ax81.plot(xx, y1, color='deepskyblue',lw=2, zorder=40,alpha=0.5)
#ax81.plot(xx, y2, color='deepskyblue',lw=2, zorder=40,alpha=0.5)

ax81.fill_between(xx,y1,y2, facecolor = 'yellow', interpolate=True, label='$1\sigma$', alpha=.35,linewidth=0.0,zorder=50)

ax81.axis([0.,1.4,3.,8.])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} $ (TeV) ", fontsize=20)
plt.ylabel(r"$\displaystyle m_{h_4} $ (TeV) ", fontsize=20)

ax81.xaxis.set_major_locator(MultipleLocator(0.20))
ax81.xaxis.set_minor_locator(MultipleLocator(0.05))

ax81.yaxis.set_major_locator(MultipleLocator(0.5))
ax81.yaxis.set_minor_locator(MultipleLocator(0.1))

# Set both ticks to be outside
ax81.tick_params(which='both', direction='out')

fig.savefig('/gs/scratch/oozdal/mBLRISS/universal/plots/tex/masshh4_mchi1.eps')   # save the figure to file
plt.close(fig)

"""




#plt.title('Interesting Graph\nCheck it put')
#plt.legend()
#plt.show()

