relicSvLeft=(relicSNUMIX11**2)+(relicSNUMIX12**2)+(relicSNUMIX13**2)
relicSvRight=(relicSNUMIX14**2)+(relicSNUMIX15**2)+(relicSNUMIX16**2)
relicScalar=(relicSNUMIX17**2)+(relicSNUMIX18**2)+(relicSNUMIX19**2)


relicSvLeft_relicmassd1=[]
relicSvLeft_relicgluino=[]
relicSvLeft_relicmchi1=[]
relicSvLeft_relicprotonSI=[]
relicSvLeft_relicneutronSI=[]
relicSvLeft_relicnucleonSI=[]

relicSvLeft_fixedrelicprotonSI=[]
relicSvLeft_fixedrelicneutronSI=[]
relicSvLeft_fixedrelicnucleonSI=[]

relicSvLeft_relicprotonSIstrengthforDARWIN=[]
relicSvLeft_relicnucleonSIstrength=[]
relicSvLeft_relicmassSv1=[]


#######################################

relicSvRight_relicmassd1=[]
relicSvRight_relicgluino=[]
relicSvRight_relicmchi1=[]
relicSvRight_relicprotonSI=[]
relicSvRight_relicneutronSI=[]
relicSvRight_relicnucleonSI=[]

relicSvRight_fixedrelicprotonSI=[]
relicSvRight_fixedrelicneutronSI=[]
relicSvRight_fixedrelicnucleonSI=[]

relicSvRight_relicprotonSIstrengthforDARWIN=[]
relicSvRight_relicnucleonSIstrength=[]
relicSvRight_relicmassSv1=[]

########################################

relicScalar_relicmassd1=[]
relicScalar_relicgluino=[]
relicScalar_relicmchi1=[]
relicScalar_relicprotonSI=[]
relicScalar_relicneutronSI=[]
relicScalar_relicnucleonSI=[]

relicScalar_fixedrelicprotonSI=[]
relicScalar_fixedrelicneutronSI=[]
relicScalar_fixedrelicnucleonSI=[]

relicScalar_relicprotonSIstrengthforDARWIN=[]
relicScalar_relicnucleonSIstrength=[]
relicScalar_relicmassSv1=[]

########################################

relicmixedSv_relicmassd1=[]
relicmixedSv_relicgluino=[]
relicmixedSv_relicmchi1=[]
relicmixedSv_relicprotonSI=[]
relicmixedSv_relicneutronSI=[]
relicmixedSv_relicnucleonSI=[]

relicmixedSv_fixedrelicprotonSI=[]
relicmixedSv_fixedrelicneutronSI=[]
relicmixedSv_fixedrelicnucleonSI=[]

relicmixedSv_relicprotonSIstrengthforDARWIN=[]
relicmixedSv_relicnucleonSIstrength=[]
relicmixedSv_relicmassSv1=[]

########################################

i=0

while i < len(relicdata):
    if relicSvLeft[i] > .90:
        relicSvLeft_relicmchi1.append(relicmchi1[i])
        relicSvLeft_relicprotonSI.append(relicprotonSI[i])
        relicSvLeft_relicneutronSI.append(relicneutronSI[i])
        relicSvLeft_relicmassd1.append(relicmassd1[i])
        relicSvLeft_relicgluino.append(relicgluino[i])
        relicSvLeft_relicnucleonSI.append(relicnucleonSI[i])
        relicSvLeft_fixedrelicprotonSI.append(fixedrelicprotonSI[i])
        relicSvLeft_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        relicSvLeft_relicprotonSIstrengthforDARWIN.append(relicprotonSIstrengthforDARWIN[i])
        relicSvLeft_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        relicSvLeft_relicmassSv1.append(relicmassSv1[i])

    elif relicSvRight[i] > .90:
        relicSvRight_relicmchi1.append(relicmchi1[i])
        relicSvRight_relicprotonSI.append(relicprotonSI[i])
        relicSvRight_relicneutronSI.append(relicneutronSI[i])
        relicSvRight_relicmassd1.append(relicmassd1[i])
        relicSvRight_relicgluino.append(relicgluino[i])
        relicSvRight_relicnucleonSI.append(relicnucleonSI[i])
        relicSvRight_fixedrelicprotonSI.append(fixedrelicprotonSI[i])
        relicSvRight_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        relicSvRight_relicprotonSIstrengthforDARWIN.append(relicprotonSIstrengthforDARWIN[i])
        relicSvRight_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        relicSvRight_relicmassSv1.append(relicmassSv1[i])

    elif relicScalar[i] > .90:
        relicScalar_relicmchi1.append(relicmchi1[i])
        relicScalar_relicprotonSI.append(relicprotonSI[i])
        relicScalar_relicneutronSI.append(relicneutronSI[i])
        relicScalar_relicmassd1.append(relicmassd1[i])
        relicScalar_relicgluino.append(relicgluino[i])
        relicScalar_fixedrelicprotonSI.append(fixedrelicprotonSI[i])
        relicScalar_relicnucleonSI.append(relicnucleonSI[i])
        relicScalar_relicprotonSIstrengthforDARWIN.append(relicprotonSIstrengthforDARWIN[i])
        relicScalar_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        relicScalar_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        relicScalar_relicmassSv1.append(relicmassSv1[i])

    else:    
        relicmixedSv_relicmchi1.append(relicmchi1[i])
        relicmixedSv_relicprotonSI.append(relicprotonSI[i])
        relicmixedSv_relicneutronSI.append(relicneutronSI[i])
        relicmixedSv_relicmassd1.append(relicmassd1[i])
        relicmixedSv_relicgluino.append(relicgluino[i])
        relicmixedSv_fixedrelicprotonSI.append(fixedrelicprotonSI[i])
        relicmixedSv_relicprotonSIstrengthforDARWIN.append(relicprotonSIstrengthforDARWIN[i])
        relicmixedSv_relicnucleonSI.append(relicnucleonSI[i])
        relicmixedSv_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        relicmixedSv_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        relicmixedSv_relicmassSv1.append(relicmassSv1[i])

    i+=1


################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax11 = plt.subplots()

sc11 = ax11.scatter(np.array(relicmixedSv_relicmassSv1)/1000.,relicmixedSv_fixedrelicprotonSI, s=15, c='orange', marker='o',linewidth = '0.0',zorder=600, label=r"$\displaystyle \widetilde{\nu}_{R}-\widetilde{\nu}_{S} {\rm\ mixed\ DM} $" )

sc11 = ax11.scatter(np.array(relicSvRight_relicmassSv1)/1000.,relicSvRight_fixedrelicprotonSI, s=15, c='aqua', marker='o',linewidth = '0.0',zorder=700, label=r"$\displaystyle \widetilde{\nu}_{R} {\rm\ -like\ DM} $")

#sc11 = ax11.scatter(relicmassSv1/1000.,fixedrelicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc11 = ax11.scatter(massSv1/1000.,fixedprotonSI, s=4,c='Blue',marker='o',linewidth = '0.0',zorder=10, label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

#sc11 = ax11.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc11 = ax11.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

#sc11 = ax11.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.6, linewidth = '2.0')

sc11 = ax11.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T\ \pm\ 1\sigma, \pm\ 2\sigma                 } $",zorder=40, alpha=0.6, linewidth = '3.0')

sc11 = ax11.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc11 = ax11.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=17)

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=16)

ax11.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax11.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamax, 1e-6, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \widetilde{\sigma}_{p}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-14,1e-7])

ax11.xaxis.set_major_locator(MultipleLocator(0.1))
ax11.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax11.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_fixedprotonSI_massSv1_content.png')   # save the figure to file

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax12 = plt.subplots()

sc12 = ax12.scatter(np.array(relicmixedSv_relicmassSv1)/1000.,relicmixedSv_relicprotonSIstrengthforDARWIN, s=15, c='orange', marker='o',linewidth = '0.0',zorder=600, label=r"$\displaystyle \widetilde{\nu}_{R}-\widetilde{\nu}_{S} {\rm\ mixed\ DM} $" )

sc12 = ax12.scatter(np.array(relicSvRight_relicmassSv1)/1000.,relicSvRight_relicprotonSIstrengthforDARWIN, s=15, c='aqua', marker='o',linewidth = '0.0',zorder=700, label=r"$\displaystyle \widetilde{\nu}_{R} {\rm\ -like\ DM} $")

#sc12 = ax12.scatter(relicmassSv1/1000.,fixedrelicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc12 = ax12.scatter(massSv1/1000.,protonSIstrengthforDARWIN, s=4,c='Blue',marker='o',linewidth = '0.0',zorder=10, label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

#sc12 = ax12.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

ax12.fill_between(np.linspace(0, 1, len(order), endpoint=True), np.array(corXENONRELIC)/np.array(corDARWINRELIC), 1e7, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

ax12.fill_between(np.linspace(0, 1, len(order), endpoint=True), np.array(corXENONnTXSECTION)/np.array(corDARWINRELIC), 1e7, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=16, label=r"$\displaystyle {\rm\ Predicted\ by\ XENONnT`} $")

ax12.axhspan(1., 1e7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=17, label=r"$\displaystyle {\rm\ Predicted\ by\ DARWIN} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle R_{\rm SI} = \widetilde{\sigma}_{\rm SI}^{\rm nucleon} / \sigma_{\rm DARWIN}$", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-3,1e7])

ax12.xaxis.set_major_locator(MultipleLocator(0.1))
ax12.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_protonSIstrengthforDARWIN_massSv1_content.png')   # save the figure to file
