relicBcontent = relicNMIX11**2
relicWcontent = relicNMIX12**2
relicBRcontent = relicNMIX15**2
relicHRcontent = (relicNMIX16**2)+(relicNMIX17**2)
relicHcontent = (relicNMIX13**2)+(relicNMIX14**2)


BBR_relicmassd1=[]
BBR_relicgluino=[]
BBR_relicmchi1=[]
BBR_relicprotonSI=[]
BBR_relicneutronSI=[]
BBR_relicnucleonSI=[]
BBR_fixedrelicnucleonSI=[]
BBR_relicnucleonSIstrength=[]
BBR_relicnucleonSIstrengthforDARWIN=[]


W_relicmassd1=[]
W_relicgluino=[]
W_relicmchi1=[]
W_relicprotonSI=[]
W_relicneutronSI=[]
W_relicnucleonSI=[]
W_fixedrelicnucleonSI=[]
W_relicnucleonSIstrength=[]
W_relicnucleonSIstrengthforDARWIN=[]

HR_relicmassd1=[]
HR_relicgluino=[]
HR_relicmchi1=[]
HR_relicprotonSI=[]
HR_relicneutronSI=[]
HR_relicnucleonSI=[]
HR_fixedrelicnucleonSI=[]
HR_relicnucleonSIstrength=[]
HR_relicnucleonSIstrengthforDARWIN=[]

H_relicmassd1=[]
H_relicgluino=[]
H_relicmchi1=[]
H_relicprotonSI=[]
H_relicneutronSI=[]
H_relicnucleonSI=[]
H_fixedrelicnucleonSI=[]
H_relicnucleonSIstrength=[]
H_relicnucleonSIstrengthforDARWIN=[]

mix_relicmassd1=[]
mix_relicgluino=[]
mix_relicmchi1=[]
mix_relicprotonSI=[]
mix_relicneutronSI=[]
mix_relicnucleonSI=[]
mix_fixedrelicnucleonSI=[]
mix_relicnucleonSIstrength=[]
mix_relicnucleonSIstrengthforDARWIN=[]


i=0

while i < len(relicdata):
    if relicBRcontent[i] + relicBcontent[i] > .80:
        BBR_relicmchi1.append(relicmchi1[i])
        BBR_relicprotonSI.append(relicprotonSI[i])
        BBR_relicneutronSI.append(relicneutronSI[i])
        BBR_relicmassd1.append(relicmassd1[i])
        BBR_relicgluino.append(relicgluino[i])
        BBR_relicnucleonSI.append(relicnucleonSI[i])
        BBR_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        BBR_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        BBR_relicnucleonSIstrengthforDARWIN.append(relicnucleonSIstrengthforDARWIN[i])

    elif relicHRcontent[i] > .80:
        HR_relicmchi1.append(relicmchi1[i])
        HR_relicprotonSI.append(relicprotonSI[i])
        HR_relicneutronSI.append(relicneutronSI[i])
        HR_relicmassd1.append(relicmchi1[i])
        HR_relicgluino.append(relicgluino[i])
        HR_relicnucleonSI.append(relicnucleonSI[i])
        HR_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        HR_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        HR_relicnucleonSIstrengthforDARWIN.append(relicnucleonSIstrengthforDARWIN[i])

    elif relicWcontent[i] > .80:
        W_relicmchi1.append(relicmchi1[i])
        W_relicprotonSI.append(relicprotonSI[i])
        W_relicneutronSI.append(relicneutronSI[i])
        W_relicmassd1.append(relicmchi1[i])
        W_relicgluino.append(relicgluino[i])
        W_relicnucleonSI.append(relicnucleonSI[i])
        W_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        W_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        W_relicnucleonSIstrengthforDARWIN.append(relicnucleonSIstrengthforDARWIN[i])

    elif relicHcontent[i] > .80:
        H_relicmchi1.append(relicmchi1[i])
        H_relicprotonSI.append(relicprotonSI[i])
        H_relicneutronSI.append(relicneutronSI[i])
        H_relicmassd1.append(relicmchi1[i])
        H_relicgluino.append(relicgluino[i])
        H_relicnucleonSI.append(relicnucleonSI[i])
        H_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        H_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        H_relicnucleonSIstrengthforDARWIN.append(relicnucleonSIstrengthforDARWIN[i])

    else:
        mix_relicmchi1.append(relicmchi1[i])
        mix_relicprotonSI.append(relicprotonSI[i])
        mix_relicneutronSI.append(relicneutronSI[i])
        mix_relicmassd1.append(relicmchi1[i])
        mix_relicgluino.append(relicgluino[i])
        mix_relicnucleonSI.append(relicnucleonSI[i])
        mix_fixedrelicnucleonSI.append(fixedrelicnucleonSI[i])
        mix_relicnucleonSIstrength.append(relicnucleonSIstrength[i])
        mix_relicnucleonSIstrengthforDARWIN.append(relicnucleonSIstrengthforDARWIN[i])

    i+=1


############################################################################################

fig, ax83 = plt.subplots()

sc83 = ax83.scatter(np.array(mix_relicmchi1)/1000,(np.array(mix_relicnucleonSI)), s=16, c='darkgoldenrod', marker='o',linewidth = '0.0',zorder=40, label=r"$\displaystyle {\rm\ Mixed\ \widetilde{\chi}_{1}^{0}} $" )

sc83 = ax83.scatter(np.array(BBR_relicmchi1)/1000,(np.array(BBR_relicnucleonSI)), s=10, c='lightcoral', marker='o',linewidth = '0.0',zorder=20, label=r"$ \displaystyle \widetilde{B}_R -\widetilde{B} {\rm\ mixed}$" )

#sc83 = ax83.scatter(np.array(W_relicmchi1)/1000,(np.array(W_relicprotonSI)+np.array(W_relicneutronSI))/2, s=20, c='orangered', marker='o',linewidth = '0.0',zorder=60, label=r"$ \displaystyle \widetilde{W} {\rm\ -like} $" )

sc83 = ax83.scatter(np.array(H_relicmchi1)/1000,(np.array(H_relicnucleonSI)), s=13, c='firebrick', marker='o',linewidth = '0.0',zorder=50, label=r"$\displaystyle \widetilde{H} {\rm\ -like\ \widetilde{\chi}_{1}^{0}} $" )

sc83 = ax83.scatter(np.array(HR_relicmchi1)/1000,(np.array(HR_relicnucleonSI)), s=15, c='k', marker='o',linewidth = '0.0',zorder=30, alpha = 0.5, label=r"$\displaystyle \widetilde{H}_R {\rm\ -like\ \widetilde{\chi}_{1}^{0}} $" )

#sc83 = ax83.scatter(relicmchi1,(relicprotonSI+relicneutronSI)/2, s=4, c='Red', marker='o',linewidth = '0.0',zorder=30 )

sc83 = ax83.scatter(np.array(mchi1)/1000,nucleonSI, s=4,c='Blue',marker='o',linewidth = '0.0',zorder=10,label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

#sc83 = ax83.scatter(rejectmchi1,(rejectprotonSI+rejectneutronSI)/2, s=4, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#sc83 = ax83.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label=r"${\rm LUX2014} $",zorder=40, alpha=0.6,linewidth = '2.0')

#sc83 = ax83.plot(LUX2017WIMPMASS/1000,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=400, alpha=0.6, linewidth = '2.0')

sc83 = ax83.plot(XENONWIMPMASS/1000,XENONRELIC,c='lime',label=r"${\rm XENON1T \pm 1 \sigma, \pm 2 \sigma} $",zorder=400, alpha=0.6,linewidth = '3.0')

sc83 = ax83.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=400, alpha=0.5,linewidth = '2.0')

sc83 = ax83.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=400, alpha=0.6,linewidth = '2.0')

ax83.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax83.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax83.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamax, 1e-7, facecolor = 'blue', interpolate=True, alpha=.2,linewidth=0.0, zorder=750)

ax83.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax83.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{\rm nucleon}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.4])
plt.ylim([1e-22,1e-7])

ax83.xaxis.set_major_locator(MultipleLocator(0.200))
ax83.xaxis.set_minor_locator(MultipleLocator(0.050))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax83.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True,ncol=1, fontsize=10)
leg.set_zorder(700)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleoncross_mchi1_content_nonrescaled.png')   # save the figure to file
plt.close(fig)

####################################################################################




############################################################################################

fig, ax84 = plt.subplots()

sc84 = ax84.scatter(np.array(mix_relicmchi1)/1000,(np.array(mix_fixedrelicnucleonSI)), s=16, c='cyan', marker='o',linewidth = '0.0',zorder=40, label=r"$\displaystyle {\rm\ Mixed\ \widetilde{\chi}_{1}^{0}} $" )

sc84 = ax84.scatter(np.array(BBR_relicmchi1)/1000,(np.array(BBR_fixedrelicnucleonSI)), s=10, c='lightcoral', marker='o',linewidth = '0.0',zorder=20, label=r"$ \displaystyle \widetilde{B}_R -\widetilde{B} {\rm\ mixed}$" )

#sc84 = ax84.scatter(np.array(W_relicmchi1)/1000,(np.array(W_relicprotonSI)+np.array(W_relicneutronSI))/2, s=20, c='orangered', marker='o',linewidth = '0.0',zorder=60, label=r"$ \displaystyle \widetilde{W} {\rm\ -like} $" )

#sc84 = ax84.scatter(np.array(H_relicmchi1)/1000,(np.array(H_fixedrelicnucleonSI)), s=13, c='firebrick', marker='o',linewidth = '0.0',zorder=50, label=r"$\displaystyle \widetilde{H} {\rm\ -like\ \widetilde{\chi}_{1}^{0}} $" )

sc84 = ax84.scatter(np.array(HR_relicmchi1)/1000,(np.array(HR_fixedrelicnucleonSI)), s=15, c='darkred', marker='o',linewidth = '0.0',zorder=30, label=r"$\displaystyle \widetilde{H}_R {\rm\ -like\ \widetilde{\chi}_{1}^{0}} $" )

#sc84 = ax84.scatter(relicmchi1,(relicprotonSI+relicneutronSI)/2, s=4, c='Red', marker='o',linewidth = '0.0',zorder=30 )

sc84 = ax84.scatter(np.array(mchi1)/1000,fixednucleonSI, s=4,c='Blue',marker='o',linewidth = '0.0',zorder=10,label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

#sc84 = ax84.scatter(rejectmchi1,(rejectprotonSI+rejectneutronSI)/2, s=4, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

#sc84 = ax84.plot(LUXDATALSPMASS,LUXDATARELIC,c='black',label=r"${\rm LUX2014} $",zorder=40, alpha=0.6,linewidth = '2.0')

#sc84 = ax84.plot(LUX2017WIMPMASS/1000,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=400, alpha=0.6, linewidth = '2.0')

sc84 = ax84.plot(XENONWIMPMASS/1000,XENONRELIC,c='lime',label=r"${\rm XENON1T \pm 1 \sigma, \pm 2 \sigma} $",zorder=400, alpha=0.6,linewidth = '3.0')

sc84 = ax84.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=400, alpha=0.5,linewidth = '2.0')

sc84 = ax84.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=400, alpha=0.6,linewidth = '2.0')

ax84.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax84.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax84.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamax, 1e-7, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

ax84.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax84.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \widetilde{\sigma}_{\rm nucleon}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-22,1e-7])

ax84.xaxis.set_major_locator(MultipleLocator(0.100))
ax84.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax84.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True,ncol=1, fontsize=10)
leg.set_zorder(700)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleoncross_mchi1_content_rescaled.png')   # save the figure to file
plt.close(fig)

####################################################################################


############################################################################################

fig, ax85 = plt.subplots()

#sc85 = ax85.scatter(np.array(excludedbyXENON1T_relicmchi1)/1000., np.array(excludedbyXENON1T_relicnucleonSIstrength), s=15, c='lime', marker='o',linewidth = '0.0',zorder=1000 )

sc85 = ax85.scatter(np.array(mix_relicmchi1)/1000,(np.array(mix_relicnucleonSIstrength)), s=16, c='cyan', marker='o',linewidth = '0.0',zorder=40, label=r"$\displaystyle {\rm\ Mixed\ \widetilde{\chi}_{1}^{0}} $" )

sc85 = ax85.scatter(np.array(BBR_relicmchi1)/1000,(np.array(BBR_relicnucleonSIstrength)), s=10, c='lightcoral', marker='o',linewidth = '0.0',zorder=20, label=r"$ \displaystyle \widetilde{B}_R -\widetilde{B} {\rm\ mixed}$" )

sc85 = ax85.scatter(np.array(HR_relicmchi1)/1000,(np.array(HR_relicnucleonSIstrength)), s=15, c='darkred', marker='o',linewidth = '0.0',zorder=30, label=r"$\displaystyle \widetilde{H}_R {\rm\ -like\ \widetilde{\chi}_{1}^{0}} $" )

sc85 = ax85.scatter(np.array(mchi1)/1000., np.array(nucleonSIstrength), s=10,c='Blue',marker='o',linewidth = '0.0', zorder=10, label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle R_{\rm SI} = \widetilde{\sigma}_{\rm SI}^{\rm nucleon} / \sigma_{\rm XENON\ 1T}$", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-11,1e3])

ax85.axhspan(1., 1e3,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

ax85.xaxis.set_major_locator(MultipleLocator(0.1))
ax85.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax85.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(1200)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleonSIstrength_mchi1_contentwithXENON1Texc.png')   # save the figure to file
plt.close(fig)

####################################################################################


############################################################################################

fig, ax86 = plt.subplots()

#sc86 = ax86.scatter(np.array(excludedbyXENON1T_relicmchi1)/1000., np.array(excludedbyXENON1T_relicnucleonSIstrength), s=15, c='lime', marker='o',linewidth = '0.0',zorder=1000 )

sc86 = ax86.scatter(np.array(mix_relicmchi1)/1000,(np.array(mix_relicnucleonSIstrengthforDARWIN)), s=16, c='cyan', marker='o',linewidth = '0.0',zorder=40, label=r"$\displaystyle {\rm\ Mixed\ \widetilde{\chi}_{1}^{0}\ DM}$" )

sc86 = ax86.scatter(np.array(BBR_relicmchi1)/1000,(np.array(BBR_relicnucleonSIstrengthforDARWIN)), s=10, c='lightcoral', marker='o',linewidth = '0.0',zorder=20, label=r"$ \displaystyle \widetilde{B}_R -\widetilde{B} {\rm\ mixed\ DM}$" )

sc86 = ax86.scatter(np.array(HR_relicmchi1)/1000,(np.array(HR_relicnucleonSIstrengthforDARWIN)), s=15, c='darkred', marker='o',linewidth = '0.0',zorder=30, label=r"$\displaystyle \widetilde{H}_R {\rm\ -like\ \widetilde{\chi}_{1}^{0}\ DM}$" )

sc86 = ax86.scatter(np.array(mchi1)/1000., np.array(nucleonSIstrengthforDARWIN), s=4,c='Blue',marker='o',linewidth = '0.0', zorder=10, label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle R_{\rm SI} = \widetilde{\sigma}_{\rm SI}^{\rm nucleon} / \sigma_{\rm DARWIN}$", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-7,1e5])


ax86.fill_between(np.linspace(0, 1, 94383, endpoint=True), np.array(corXENONRELIC)/np.array(corDARWINRELIC), 1e7, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

ax86.fill_between(np.linspace(0, 1, 94383, endpoint=True), np.array(corXENONnTXSECTION)/np.array(corDARWINRELIC), 1e7, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=16, label=r"$\displaystyle {\rm\ Predicted\ by\ XENONnT`} $")

ax86.axhspan(1., 1e7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=17, label=r"$\displaystyle {\rm\ Predicted\ by\ DARWIN} $")

ax86.xaxis.set_major_locator(MultipleLocator(0.1))
ax86.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax86.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(1200)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_nucleonSIstrength_mchi1_contentwithDARWINexc.png')   # save the figure to file
plt.close(fig)

####################################################################################

