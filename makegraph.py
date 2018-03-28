################################################################
"""
#cm = plt.cm.get_cmap('rainbow')

fig, ax1 = plt.subplots()

sc1 = ax1.scatter(np.array(sneutrinorelic.MixedSv1["MassSv1"])/1000., np.array(sneutrinorelic.MixedSv1["ProtonSI"]), s=15, c='orange', marker='o',linewidth = '0.0',zorder=600, label=r"$\displaystyle \widetilde{\nu}_{R}-\widetilde{\nu}_{S} {\rm\ mixed\ DM} $" )

sc1 = ax1.scatter(np.array(sneutrinorelic.RightSv1["MassSv1"])/1000., np.array(sneutrinorelic.RightSv1["ProtonSI"]), s=15, c='aqua', marker='o',linewidth = '0.0',zorder=700, label=r"$\displaystyle \widetilde{\nu}_{R} {\rm\ -like\ DM} $")

sc1 = ax1.scatter(np.array(sneutrinorelic.LeftSv1["MassSv1"])/1000., np.array(sneutrinorelic.LeftSv1["ProtonSI"]), s=15, c='lightgreen', marker='o',linewidth = '0.0',zorder=800, label=r"$\displaystyle \widetilde{\nu}_{L} {\rm\ -like\ DM} $")


sc1 = ax1.scatter(np.array(sneutrinoLHC.param["MassSv1"])/1000., np.array(sneutrinoLHC.param["ProtonSI"]), s=4, c='Blue', marker='o',linewidth = '0.0',zorder=10, label=r"$ {\rm Excluded\ by\ \Omega h^2\ bound} $")

#sc1 = ax1.plot(LUXDATALSPMASS/1000.,LUXDATARELIC,c='black',label=r"${\rm LUX2014}$",zorder=40, alpha=0.6,linewidth = '2.0')

sc1 = ax1.plot(XENONWIMPMASS/1000., XENON1TXSECTION, c='lime',label=r"${\rm XENON1T\ \pm\ 1\sigma, \pm\ 2\sigma                 } $",zorder=40, alpha=0.6, linewidth = '3.0')

sc1 = ax1.plot(XENONnTWIMPMASS/1000.,XENONnTXSECTION,c='black',label=r"${\rm XENONnT/LZ } $",zorder=40, alpha=0.5,linewidth = '2.0')

sc1 = ax1.plot(DARWINWIMPMASS/1000.,DARWINXSECTION,c='magenta',label=r"${\rm DARWIN(200t \times y)} $",zorder=40, alpha=0.6,linewidth = '2.0')

ax1.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION2sigmamin, XENON1TXSECTION2sigmamax, facecolor = 'green', interpolate=True, alpha=.2,linewidth=0.0, zorder=17)

ax1.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION1sigmamin, XENON1TXSECTION1sigmamax, facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=16)

ax1.axvspan(((SM.ZBosonMass/1000)/2)*0.8, ((SM.ZBosonMass/1000)/2)*1.2, color='violet',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ Z\ funnel} $")

ax1.axvspan(((SM.HiggsBosonMass/1000)/2)*0.8, ((SM.HiggsBosonMass/1000)/2)*1.2, color='lightpink',fill=True,alpha=.2,linewidth=0.0,zorder=300, label=r"$\displaystyle {\rm\ SM-like\ h\ funnel} $")

xmin = 0.0
xmax = 1.6
ymin = 1e-14
ymax = 1e-4

ax1.fill_between(XENONWIMPMASS/1000, XENON1TXSECTION2sigmamax, ymax, facecolor = 'navy', interpolate=True, alpha=.2,linewidth=0.0, zorder=15, label=r"$\displaystyle {\rm\ Excluded\ by\ XENON1T`} $")

plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]} $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \widetilde{\sigma}_{p}^{SI} {\rm\ [pb]} $", fontsize=20)

plt.xlim([xmin,xmax])
plt.ylim([ymin,ymax])

ax1.xaxis.set_major_locator(MultipleLocator(0.1))
ax1.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax1.tick_params(which='both', direction='out')

leg=plt.legend(loc='best',frameon=True)
leg.set_zorder(800)

fig.savefig( plotdirpath + projectname + "_ProtonSI_MassSv1_content.png")   # save the figure to file
"""
############################################################################################

fig, ax2 = plt.subplots()

ax2.scatter(np.array(neutLHC.BBRlike["mchi1"])/1000., np.array(neutLHC.BBRlike["DAMU"])*10**10, s=10, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.Winolike["mchi1"])/1000., np.array(neutLHC.Winolike["DAMU"])*10**10, s=10, c='orangered',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.HRlike["mchi1"])/1000., np.array(neutLHC.HRlike["DAMU"])*10**10, s=10, c='Pink',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.Higgsinolike["mchi1"])/1000., np.array(neutLHC.Higgsinolike["DAMU"])*10**10, s=10, c='firebrick',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax2.scatter(np.array(neutLHC.Mixedmchi1["mchi1"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"])*10**10, s=10, c='Violet',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )




#ax2.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["DAMU"])*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax2.scatter(np.array(neutrelic.param["mchi1"])/1000., np.array(neutrelic.param["DAMU"])*10**10, s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

xmin = 0.0
xmax = 1.0
ymin = 0.0
ymax = 60.0

ax2.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax2.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax2.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax2.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax2.text(xmax + 0.05, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax2.text(xmax + 0.05, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax2.text(xmax + 0.05, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax2.xaxis.set_major_locator(MultipleLocator(0.1))
ax2.xaxis.set_minor_locator(MultipleLocator(0.025))

ax2.yaxis.set_major_locator(MultipleLocator(5))
ax2.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax2.tick_params(which='both', direction='out')

leg = plt.legend(loc='best',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_mchi1.png")   # save the figure to file
plt.close(fig)

