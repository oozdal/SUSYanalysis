#!/usr/bin/python

#execfile("readingpart1.py")

###################################################################
"""
relicBcontent = relicNMIX11**2
relicBRcontent = relicNMIX15**2
relicHRcontent = (relicNMIX16**2)+(relicNMIX17**2)
relicHcontent = (relicNMIX13**2)+(relicNMIX14**2)


BBR_relicmassd1=[]
BBR_relicgluino=[]

HR_relicmassd1=[]
HR_relicgluino=[]

HR_relicmassd1=[]
HR_relicgluino=[]

mix_relicmassd1=[]
mix_relicgluino=[]

i=0

while i < len(relicdata):
    if relicBRcontent[i] > .56 and relicBcontent[i] > .36:
        BBR_relicmassd1.append(relicmassd1[i])
        BBR_relicgluino.append(relicgluino[i])
    elif  relicHcontent[i] > .5:
        H_relicmassd1.append(relicmassd1[i])
        H_relicgluino.append(relicgluino[i])
    elif  relicHRcontent[i] > .5:
        HR_relicmassd1.append(relicmassd1[i])
        HR_relicgluino.append(relicgluino[i])
    else:
        mix_relicmassd1.append(relicmassd1[i])
        mix_relicgluino.append(relicgluino[i])

    i+=1


fig, ax85 = plt.subplots()

sc85 = ax85.scatter(np.array(HR_relicgluino)/1000.,np.array(HR_relicmassd1)/1000., s=16, c='black', marker='o',linewidth = '0.0',zorder=60, label=r"$ \displaystyle \widetilde{H}_R - like\ \widetilde{\chi}_{1}^{0} $" )

sc85 = ax85.scatter(np.array(H_relicgluino)/1000.,np.array(H_relicmassd1)/1000., s=13, c='lime', marker='o',linewidth = '0.0',zorder=50, label=r"$ \displaystyle \widetilde{H} - like\ \widetilde{\chi}_{1}^{0}$" )

sc85 = ax85.scatter(np.array(mix_relicgluino)/1000.,np.array(mix_relicmassd1)/1000., s=12, c='paleturquoise', marker='o',linewidth = '0.0',zorder=40, label=r"${\rm\ Mixed\ \widetilde{\chi}_{1}^{0}} $")

sc85 = ax85.scatter(np.array(BBR_relicgluino)/1000.,np.array(BBR_relicmassd1)/1000., s=8, c='lightcoral', marker='o',linewidth = '0.0',zorder=30, label=r"$ \displaystyle \%60 \widetilde{B}_R - \%40 \widetilde{B} $" )

#ax85.scatter(relicgluino/1000., relicmassd1/1000., s=10, c='r', marker='o',linewidth = '0.0',zorder=30 )

ax85.scatter(gluino/1000., massd1/1000., s=4, c='Blue',marker='o',linewidth = '0.0',zorder=20, label=r"$ {\rm\ Excluded\ by\ \Omega_{DM} h^2\ bound} $")

ax85.scatter(rejectgluino/1000., rejectmassd1/1000., s=4, c='Grey', marker='o',linewidth = '0.0',zorder=10, label=r"$ {\rm\ Excluded\ by\ constraints} $" )

ax85.plot(GLUINOMASS/1000.,SQUARKSMASS/1000.,label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=100,alpha=0.5)

ax85.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35,linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax85.axis([1.,6.,1.,6.])
plt.xlabel(r"$\displaystyle m_{\widetilde{g}} {\rm\ (TeV)} $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{q}} {\rm\ (TeV)} $", fontsize=20)

ax85.xaxis.set_major_locator(MultipleLocator(1.))
ax85.xaxis.set_minor_locator(MultipleLocator(0.2))

ax85.yaxis.set_major_locator(MultipleLocator(1.))
ax85.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax85.tick_params(which='both', direction='out')

plt.legend(loc='lower right',frameon=True)

fig.savefig('/Users/oozdal/Desktop/PRDrevision/plot/gluino_squarks_color.png')   # save the figure to file
plt.close(fig)
"""
##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax12 = plt.subplots()

sc12 = ax12.scatter(BLnonuniversalmassVZR/1000., BLnonuniversalvzrxsectiontoll, c=BLnonBRZpelecmu*100, cmap=cm ,s=10, linewidth = '0.0',marker='o',zorder=16, label=r"$ {\rm\ BLRISS\ with\ B-L\ Non-universality } $", alpha=0.5)


#cbar12 = plt.colorbar(sc12, format = "%.0f")
cbar12 = plt.colorbar(sc12)
cbar12.set_label(r"$\displaystyle {\rm\ BR(Z' \to l^+l^-)\ [\%]}$", fontsize=20)

sc12 = ax12.scatter(universalmassVZR/1000., universalvzrxsectiontoll, color="black", s=10, linewidth = '0.0',marker='o',zorder=15, label=r"$ {\rm\ BLRISS\ with\ universal\ BC } $")

ax12.axis([2.0,5.0,1e-5,1e-2])
cbar12 = plt.xlabel(r"$\displaystyle M_{Z'} {\rm\ [TeV]} $", fontsize=20)
cbar12 = plt.ylabel(r"$\displaystyle \sigma B {\rm\ [pb]} $", fontsize=20)

sc12 = ax12.plot(observedxsection13TeVZpmassforll, observedxsection13TeVZpll, label=r"$ {\rm\ ATLAS\ Observed\ Limit} $",color='r', linewidth=2.0, zorder=40,alpha=0.7)

sc12 = ax12.plot(expectedxsection13TeVZpmassforll,expectedxsection13TeVZpll,'--',label=r"$ {\rm\ Expected\ Limit} $",color='k', linewidth=2.0, zorder=30,alpha=0.7)

ax12.fill_between(expectedxsection13TeVZpmassforll, expectedxsection13TeVZpll2sigmamin, expectedxsection13TeVZpll2sigmamax, label=r"$ {\rm\ Expected\ \pm\ 2 \sigma} $", facecolor = 'gold', interpolate=True, alpha=.2,linewidth=0.0, zorder=10)

ax12.fill_between(expectedxsection13TeVZpmassforll, expectedxsection13TeVZpll1sigmamin, expectedxsection13TeVZpll1sigmamax, label=r"$ {\rm\ Expected\ \pm\ 1 \sigma} $", facecolor = 'lime', interpolate=True, alpha=.2,linewidth=0.0, zorder=20)

#plt.plot([0, 1.4], [0.09488, 0.09488], 'k--')
#plt.plot([0, 1.4], [0.14232, 0.14232], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax12.xaxis.set_major_locator(MultipleLocator(0.5))
ax12.xaxis.set_minor_locator(MultipleLocator(0.1))

#ax12.yaxis.set_major_locator(MultipleLocator(1))
#ax12.yaxis.set_minor_locator(MultipleLocator(0.25))

#plt.xscale('log')
plt.yscale('log')

ax12.text(4.0, 4e-4, r"$\displaystyle {\rm\ \sqrt{s} = 13\ TeV}$", fontsize=15)
ax12.text(4.2, 6e-4, r"$\displaystyle {\rm\ Z' \to l^+l^-\ }$", fontsize=15)

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

leg = plt.legend(loc='best', frameon=False, ncol=1, fontsize=10)
leg.set_zorder(100)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_vzrxsectiontoll.png')   # save the figure to file
plt.close(fig)

################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax17 = plt.subplots()

col = NMIX15**2

sc17 = ax17.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')
#cbar17 = plt.colorbar(sc17, format = "%.0f")
cbar17 = plt.colorbar(sc17)
cbar17.set_label(r"$\displaystyle \widetilde{B}_{R} {\rm\ Content\ [\%]}$", fontsize=20)
ax17.axis([0.0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax17.xaxis.set_major_locator(MultipleLocator(0.2))
ax17.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax17.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax17.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_B_R_content.png')   # save the figure to file
plt.close(fig)

###############################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax20 = plt.subplots()

col = NMIX11**2

sc20 = ax20.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')
#cbar20 = plt.colorbar(sc20, format = "%.0f")
cbar20 = plt.colorbar(sc20)
cbar20.set_label(r"$\displaystyle \widetilde{B} {\rm\ Content\ [\%]}$", fontsize=20)
ax20.axis([0.0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax20.xaxis.set_major_locator(MultipleLocator(0.2))
ax20.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax20.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax20.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_B_content.png')   # save the figure to file
plt.close(fig)

###############################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax19 = plt.subplots()

col = (NMIX16**2)+(NMIX17**2)

sc19 = ax19.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

#cbar19 = plt.colorbar(sc19, format = "%.0f")
cbar19 = plt.colorbar(sc19)
cbar19.set_label(r"$\displaystyle \widetilde{H}_R {\rm\ Content\ [\%]}$", fontsize=20)
ax19.axis([0.0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax19.xaxis.set_major_locator(MultipleLocator(0.2))
ax19.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax19.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax19.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_H_R_content.png')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax18 = plt.subplots()

col = (NMIX13**2)+(NMIX14**2)

sc18 = ax18.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')
#cbar18 = plt.colorbar(sc18, format = "%.0f")
cbar18 = plt.colorbar(sc18)
cbar18.set_label(r"$\displaystyle \widetilde{H} {\rm\ Content\ [\%]}$", fontsize=20)
ax18.axis([0.0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax18.xaxis.set_major_locator(MultipleLocator(0.2))
ax18.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax18.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax18.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_H_content.png')   # save the figure to file
plt.close(fig)

##################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax21 = plt.subplots()

col = (NMIX12**2)

sc21 = ax21.scatter(mchi1/1000.,relic,c=col*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')
#cbar21 = plt.colorbar(sc18, format = "%.0f")
cbar21 = plt.colorbar(sc18)
cbar21.set_label(r"$\displaystyle \widetilde{W} {\rm\ Content\ [\%]}$", fontsize=20)
ax21.axis([0.0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0.0, 1.4], [0.09, 0.09], 'k--')
plt.plot([0.0, 1.4], [0.14, 0.14], 'k--')

ax21.xaxis.set_major_locator(MultipleLocator(0.2))
ax21.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax21.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax21.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_W_content.png')   # save the figure to file
plt.close(fig)

################################################################

fig, ax6 = plt.subplots()

sc6 = ax6.scatter(relicmchi1/1000.,fixedrelicnucleonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc6 = ax6.scatter(mchi1/1000.,fixednucleonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc6 = ax6.scatter(rejectmchi1,(rejectprotonSI+rejectneutronSI)/2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#sc6 = ax6.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label=r"${\rm LUX2014} $",zorder=40, alpha=0.6,linewidth = '2.0')

sc6 = ax6.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.5, linewidth = '2.0')

sc6 = ax6.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T \pm 1 \sigma, \pm 2 \sigma} $",zorder=40, alpha=0.5,linewidth = '3.0')

sc6 = ax6.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=400, alpha=0.5,linewidth = '2.0')

sc6 = ax6.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=400, alpha=0.6,linewidth = '2.0')

ax6.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax6.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax6.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax6.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{\rm nucleon}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.4])
plt.ylim([1e-22,1e-7])

ax6.xaxis.set_major_locator(MultipleLocator(0.2))
ax6.xaxis.set_minor_locator(MultipleLocator(0.05))


#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax6.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleoncross_mchi1_new.png')   # save the figure to file
plt.close(fig)

################################################################

fig, ax7 = plt.subplots()

sc7 = ax7.scatter(relicmchi1/1000.,relicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc7 = ax7.scatter(mchi1/1000.,protonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc7 = ax7.scatter(rejectmchi1,(rejectprotonSI+rejectneutronSI)/2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#sc7 = ax7.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label=r"${\rm LUX2014} $",zorder=40, alpha=0.6,linewidth = '2.0')

sc7 = ax7.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.5, linewidth = '2.0')

sc7 = ax7.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T \pm 1 \sigma, \pm 2 \sigma} $",zorder=40, alpha=0.5,linewidth = '3.0')

sc7 = ax7.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=400, alpha=0.5,linewidth = '2.0')

sc7 = ax7.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=400, alpha=0.6,linewidth = '2.0')

ax7.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax7.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax7.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax7.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{\rm p}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.4])
plt.ylim([1e-22,1e-7])

ax7.xaxis.set_major_locator(MultipleLocator(0.2))
ax7.xaxis.set_minor_locator(MultipleLocator(0.05))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax7.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_protoncross_mchi1.png')   # save the figure to file
plt.close(fig)

################################################################

fig, ax8 = plt.subplots()

sc8 = ax8.scatter(relicmchi1/1000.,relicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc8 = ax8.scatter(mchi1/1000.,protonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc8 = ax8.scatter(rejectmchi1,(rejectprotonSI+rejectneutronSI)/2, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#sc8 = ax8.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label=r"${\rm LUX2014} $",zorder=40, alpha=0.6,linewidth = '2.0')

sc8 = ax8.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.5, linewidth = '2.0')

sc8 = ax8.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T \pm 1 \sigma, \pm 2 \sigma} $",zorder=40, alpha=0.5,linewidth = '3.0')

sc8 = ax8.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=400, alpha=0.5,linewidth = '2.0')

sc8 = ax8.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=400, alpha=0.6,linewidth = '2.0')

ax8.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax8.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax8.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax8.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{\rm n}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.4])
plt.ylim([1e-22,1e-7])

ax8.xaxis.set_major_locator(MultipleLocator(0.2))
ax8.xaxis.set_minor_locator(MultipleLocator(0.05))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax8.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutroncross_mchi1.png')   # save the figure to file
plt.close(fig)

################################################################

fig, ax9 = plt.subplots()

sc9 = ax9.scatter(np.array(excludedbyXENON1T_relicmchi1)/1000., np.array(excludedbyXENON1T_relicnucleonSIstrength), s=15, c='lime', marker='o',linewidth = '0.0',zorder=700 )

sc9 = ax9.scatter(relicmchi1/1000., relicnucleonSIstrength, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc9 = ax9.scatter(mchi1/1000., nucleonSIstrength, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)


plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle R_{\rm SI} = \widetilde{\sigma}_{\rm SI}^{\rm nucleon} / \sigma_{\rm XENON\ 1T}$", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-11,1e3])

ax9.axhspan(1., 1e3,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=250)

ax9.xaxis.set_major_locator(MultipleLocator(0.1))
ax9.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax9.tick_params(which='both', direction='out')

#leg=plt.legend(loc='best',frameon=True)
#leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleonSIstrength_mchi1_withXENON1Texc.png')   # save the figure to file
plt.close(fig)

################################################################

