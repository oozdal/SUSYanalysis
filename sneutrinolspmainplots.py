

############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax8 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc8 = ax8.scatter(massSv1/1000., relic, c=SvRight*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

#cbar8 = plt.colorbar(sc8, format = "%.0f")
cbar8 = plt.colorbar(sc8)
cbar8.set_label(r"$\displaystyle \widetilde{\nu}_R {\rm\ content\ [\%] $", fontsize=20)

ax8.axis([0.,1.20,1e-2,1e4])
cbar8 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} {\rm\ [TeV]} $ ", fontsize=20)
cbar8 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar8 = plt.xlim([-0.1,1400])
#cbar8 = plt.ylim([1e-10,1e-5])

plt.plot([0., 1.5], [0.09, 0.09], 'k--')
plt.plot([0., 1.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax8.xaxis.set_major_locator(MultipleLocator(0.20))
ax8.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax8.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax8.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_relic_sneutrino_rightcontent.png')   # save the figure to file
plt.close(fig)

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax9 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc9 = ax9.scatter(massSv1/1000., relic, c=Scalar*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

#cbar9 = plt.colorbar(sc8, format = "%.0f")
cbar9 = plt.colorbar(sc8)
cbar9.set_label(r"$\displaystyle S\ {\rm\ content\ [\%] $", fontsize=20)

ax9.axis([0.,1.20,1e-2,1e4])
cbar9 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} {\rm\ [TeV]} $ ", fontsize=20)
cbar9 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar9 = plt.xlim([-0.1,1400])
#cbar9 = plt.ylim([1e-10,1e-5])

plt.plot([0., 1.5], [0.09, 0.09], 'k--')
plt.plot([0., 1.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax9.xaxis.set_major_locator(MultipleLocator(0.20))
ax9.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax9.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax9.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_relic_sneutrino_Scalarcontent.png')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax10 = plt.subplots()

SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

sc10 = ax10.scatter(massSv1/1000., relic, c=SvLeft*100, cmap=cm ,s=10, linewidth = '0.0',marker='o')

#cbar10 = plt.colorbar(sc8, format = "%.0f")
cbar10 = plt.colorbar(sc8)
cbar10.set_label(r"$\displaystyle \widetilde{\nu}_L {\rm\ content\ [\%] $", fontsize=20)

ax10.axis([0.,1.20,1e-2,1e4])
cbar10 = plt.xlabel(r"$\displaystyle m_{\widetilde{\nu_1}} {\rm\ [TeV]} $ ", fontsize=20)
cbar10 = plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

#cbar10 = plt.xlim([-0.1,1400])
#cbar10 = plt.ylim([1e-10,1e-5])

plt.plot([0., 1.5], [0.09, 0.09], 'k--')
plt.plot([0., 1.5], [0.14, 0.14], 'k--')

#plt.plot([68, 68], [10**(-2), 10**2], 'k--')

ax10.xaxis.set_major_locator(MultipleLocator(0.20))
ax10.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax10.yaxis.set_major_locator(MultipleLocator(1e))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax10.tick_params(which='both', direction='out')

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_relic_sneutrino_leftcontent.png')   # save the figure to file
plt.close(fig)

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax3 = plt.subplots()

sc3 = ax3.scatter(relicmassSv1/1000.,relicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc3 = ax3.scatter(massSv1/1000.,protonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc3 = ax3.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc3 = ax3.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

sc3 = ax3.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.6, linewidth = '2.0')

sc3 = ax3.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T} $",zorder=40, alpha=0.6, linewidth = '3.0')

sc3 = ax3.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc3 = ax3.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax3.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax3.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax3.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax3.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{p}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.2])
plt.ylim([1e-14,1e-6])

ax3.xaxis.set_major_locator(MultipleLocator(0.2))
ax3.xaxis.set_minor_locator(MultipleLocator(0.05))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax3.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_protoncross_massSv1.png')   # save the figure to file

##############################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax4 = plt.subplots()

sc4 = ax4.scatter(relicmassSv1/1000.,relicneutronSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc4 = ax4.scatter(massSv1/1000.,neutronSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc4 = ax4.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc4 = ax4.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

sc4 = ax4.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.6, linewidth = '2.0')

sc4 = ax4.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T} $",zorder=40, alpha=0.6, linewidth = '3.0')

sc4 = ax4.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc4 = ax4.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax4.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax4.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax4.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax4.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \sigma_{n}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.2])
plt.ylim([1e-14,1e-4])

ax4.xaxis.set_major_locator(MultipleLocator(0.2))
ax4.xaxis.set_minor_locator(MultipleLocator(0.05))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax4.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutroncross_massSv1.png')   # save the figure to file

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax11 = plt.subplots()

sc11 = ax11.scatter(relicmassSv1/1000.,fixedrelicprotonSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc11 = ax11.scatter(massSv1/1000.,fixedprotonSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc11 = ax11.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc11 = ax11.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

#sc11 = ax11.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.6, linewidth = '2.0')

sc11 = ax11.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T} $",zorder=40, alpha=0.6, linewidth = '3.0')

sc11 = ax11.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc11 = ax11.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax11.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax11.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

ax11.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamax, 1e-6, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \widetilde{\sigma}_{p}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-14,1e-6])

ax11.xaxis.set_major_locator(MultipleLocator(0.1))
ax11.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax11.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_fixedprotoncross_massSv1.png')   # save the figure to file

################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax12 = plt.subplots()

sc12 = ax12.scatter(relicmassSv1/1000.,fixedrelicneutronSI, s=15, c='Red', marker='o',linewidth = '0.0',zorder=600 )

sc12 = ax12.scatter(massSv1/1000.,fixedneutronSI, s=10,c='Blue',marker='o',linewidth = '0.0',zorder=20)

#sc12 = ax12.scatter(rejectmassSv1,rejectprotonSI, s=10, c='Grey', marker='o',linewidth = '0.0',zorder=10 )

sc12 = ax12.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

#sc12 = ax12.plot(LUX2017WIMPMASS/1000.,LUX2017RELIC,c='cyan',label=r"${\rm LUX2017} $",zorder=40, alpha=0.6, linewidth = '2.0')

sc12 = ax12.plot(XENONWIMPMASS/1000.,XENONRELIC,c='lime',label=r"${\rm XENON1T} $",zorder=40, alpha=0.6, linewidth = '3.0')

sc12 = ax12.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc12 = ax12.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax12.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamin, XENONRELIC2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=500)

ax12.fill_between(XENONWIMPMASS/1000, XENONRELIC1sigmamin, XENONRELIC1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=550)

ax12.axvspan(0.083892592, 0.098482608, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax12.axvspan(0.1150828, 0.1350972,color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

ax12.fill_between(XENONWIMPMASS/1000, XENONRELIC2sigmamax, 1e-6, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \widetilde{\sigma}_{n}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([0.0,1.0])
plt.ylim([1e-14,1e-6])

ax12.xaxis.set_major_locator(MultipleLocator(0.1))
ax12.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_fixedneutroncross_massSv1.png')   # save the figure to file
