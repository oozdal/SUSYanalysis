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

ax2.scatter(np.array(neutLHC.BBRlike["mchi1"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=5, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.Winolike["mchi1"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=5, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.HRlike["mchi1"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=5, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax2.scatter(np.array(neutLHC.Higgsinolike["mchi1"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=5, c='firebrick',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax2.scatter(np.array(neutLHC.Mixedmchi1["mchi1"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=10, c='Violet',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )




#ax2.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["DAMU"]), s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax2.scatter(np.array(neutrelic.param["mchi1"])/1000., np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

xmin = 0.0
xmax = 1.0
ymin = 0.0
ymax = 46.0

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

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax3 = plt.subplots()

ax3.scatter(np.array(neutLHC.BBRlike["mcha1"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax3.scatter(np.array(neutLHC.Winolike["mcha1"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax3.scatter(np.array(neutLHC.HRlike["mcha1"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax3.scatter(np.array(neutLHC.Higgsinolike["mcha1"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax3.scatter(np.array(neutLHC.Mixedmchi1["mcha1"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )




#ax3.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["DAMU"]), c=np.array(neutLHC.param["mcha1"]), cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax3.scatter(np.array(neutrelic.param["mchi1"])/1000., np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )


xmin = 0.0
xmax = 2.4
ymin = 0.0
ymax = 45.0

#cbar3.set_clim(0.0, 700)

ax3.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^\pm} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax3.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax3.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax3.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax3.text(xmax + 0.05, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax3.text(xmax + 0.05, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax3.text(xmax + 0.05, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax3.xaxis.set_major_locator(MultipleLocator(0.2))
ax3.xaxis.set_minor_locator(MultipleLocator(0.05))

ax3.yaxis.set_major_locator(MultipleLocator(5))
ax3.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax3.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper left',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_mcha1.png")   # save the figure to file
plt.close(fig)

############################################################################################
"""
cm = plt.cm.get_cmap('rainbow')

fig, ax4 = plt.subplots()

ax4.scatter(np.array(neutLHC.BBRlike["MassSv1"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax4.scatter(np.array(neutLHC.Winolike["MassSv1"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax4.scatter(np.array(neutLHC.HRlike["MassSv1"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax4.scatter(np.array(neutLHC.Higgsinolike["MassSv1"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax4.scatter(np.array(neutLHC.Mixedmchi1["MassSv1"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )




#ax4.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["DAMU"]), c=np.array(neutLHC.param["mcha1"]), cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax4.scatter(np.array(neutrelic.param["mchi1"])/1000., np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )


xmin = 0.0
xmax = 2.4
ymin = 0.0
ymax = 45.0

#cbar4.set_clim(0.0, 700)

ax4.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax4.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax4.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax4.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax4.text(xmax + 0.05, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax4.text(xmax + 0.05, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax4.text(xmax + 0.05, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax4.xaxis.set_major_locator(MultipleLocator(0.2))
ax4.xaxis.set_minor_locator(MultipleLocator(0.05))

ax4.yaxis.set_major_locator(MultipleLocator(5))
ax4.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax4.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper left',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_MassSv1.png")   # save the figure to file
plt.close(fig)
"""
############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax5 = plt.subplots()

ax5.scatter(np.array(neutLHC.LeftSv1["MassSv1"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

ax5.scatter(np.array(neutLHC.RightSv1["MassSv1"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )

ax5.scatter(np.array(neutLHC.MixedSv1["MassSv1"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )

xmin = 0.0
xmax = 2.0
ymin = 0.0
ymax = 45.0

#cbar5.set_clim(0.0, 700)

ax5.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_1} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax5.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax5.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax5.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax5.text(xmax + 0.05, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax5.text(xmax + 0.05, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax5.text(xmax + 0.05, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax5.xaxis.set_major_locator(MultipleLocator(0.2))
ax5.xaxis.set_minor_locator(MultipleLocator(0.05))

ax5.yaxis.set_major_locator(MultipleLocator(5))
ax5.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax5.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_MassSv1.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax6 = plt.subplots()

#ax6.scatter(np.array(neutLHC.LeftSv1["Smuon1"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax6.scatter(np.array(neutLHC.RightSv1["Smuon1"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )

#ax6.scatter(np.array(neutLHC.MixedSv1["Smuon1"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax6.scatter(np.array(neutLHC.BBRlike["Smuon1"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax6.scatter(np.array(neutLHC.Winolike["Smuon1"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax6.scatter(np.array(neutLHC.HRlike["Smuon1"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax6.scatter(np.array(neutLHC.Higgsinolike["Smuon1"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax6.scatter(np.array(neutLHC.Mixedmchi1["Smuon1"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )



xmin = 0.0
xmax = 8.0
ymin = 0.0
ymax = 45.0

#cbar6.set_clim(0.0, 700)

ax6.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\mu}_1} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax6.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax6.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax6.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax6.text(xmax + 0.05, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax6.text(xmax + 0.05, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax6.text(xmax + 0.05, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax6.xaxis.set_major_locator(MultipleLocator(1))
ax6.xaxis.set_minor_locator(MultipleLocator(0.25))

ax6.yaxis.set_major_locator(MultipleLocator(5))
ax6.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax6.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_Smuon1.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax7 = plt.subplots()

#ax7.scatter(np.array(neutLHC.LeftSv1["Smuon1"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax7.scatter(np.array(neutLHC.RightSv1["Smuon1"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )

#ax7.scatter(np.array(neutLHC.MixedSv1["Smuon1"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


#ax7.scatter(np.array(neutrelic.BBRlike["tanb"]), np.array(neutrelic.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

#ax7.scatter(np.array(neutrelic.Winolike["tanb"]), np.array(neutrelic.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax7.scatter(np.array(neutrelic.HRlike["tanb"]), np.array(neutrelic.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

#ax7.scatter(np.array(neutrelic.Higgsinolike["tanb"]), np.array(neutrelic.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax7.scatter(np.array(neutrelic.Mixedmchi1["tanb"]), np.array(neutrelic.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )

ax7.scatter(np.array(neutLHC.param["tanb"]), np.array(neutLHC.param["DAMU"]), c="cyan", cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP\ Scenario} $" )

#ax7.scatter(np.array(neutrelic.param["tanb"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax7.scatter(np.array(sneutrinoLHC.param["tanb"]), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )



xmin = 2.0
xmax = 60.0
ymin = 0.0
ymax = 45.0

#cbar6.set_clim(0.0, 700)

ax7.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle tan\beta $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax7.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax7.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax7.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax7.text(xmax + 0.2, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax7.text(xmax + 0.2, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax7.text(xmax + 0.2, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax7.xaxis.set_major_locator(MultipleLocator(5))
ax7.xaxis.set_minor_locator(MultipleLocator(1))

ax7.yaxis.set_major_locator(MultipleLocator(5))
ax7.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax7.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper left',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_tanb.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax8 = plt.subplots()

#ax8.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax8.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax8.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


#ax8.scatter(np.array(neutLHC.BBRlike["m0"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

#ax8.scatter(np.array(neutLHC.Winolike["m0"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax8.scatter(np.array(neutLHC.HRlike["m0"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

#ax8.scatter(np.array(neutLHC.Higgsinolike["m0"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

#ax8.scatter(np.array(neutLHC.Mixedmchi1["m0"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )

ax8.scatter(np.array(neutLHC.param["m0"]/1000.), np.array(neutLHC.param["DAMU"]), c="cyan", cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP\ Scenario} $" )

#ax8.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax8.scatter(np.array(sneutrinoLHC.param["m0"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )


xmin = 0.0
xmax = 3.0
ymin = 0.0
ymax = 45.0

#cbar8.set_clim(0.0, 700)

ax8.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_0 {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax8.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax8.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax8.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax8.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax8.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax8.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax8.xaxis.set_major_locator(MultipleLocator(0.5))
ax8.xaxis.set_minor_locator(MultipleLocator(0.1))

ax8.yaxis.set_major_locator(MultipleLocator(5))
ax8.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax8.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_m0.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax9 = plt.subplots()

#ax9.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax9.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax9.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax9.scatter(np.array(neutLHC.BBRlike["M2GUT"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax9.scatter(np.array(neutLHC.Winolike["M2GUT"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.5, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax9.scatter(np.array(neutLHC.HRlike["M2GUT"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax9.scatter(np.array(neutLHC.Higgsinolike["M2GUT"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax9.scatter(np.array(neutLHC.Mixedmchi1["M2GUT"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )

#ax9.scatter(np.array(neutLHC.param["M2GUT"]/1000.), np.array(neutLHC.param["DAMU"]), c="cyan", cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP\ Scenario} $" )

#ax9.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax9.scatter(np.array(sneutrinoLHC.param["M2GUT"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )


xmin = -4.0
xmax = 4.0
ymin = 0.0
ymax = 45.0

#cbar8.set_clim(0.0, 700)

ax9.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle M_2 {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax9.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax9.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax9.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax9.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax9.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax9.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax9.xaxis.set_major_locator(MultipleLocator(1))
ax9.xaxis.set_minor_locator(MultipleLocator(0.25))

ax9.yaxis.set_major_locator(MultipleLocator(5))
ax9.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax9.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_M2GUT.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax10 = plt.subplots()

#ax10.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax10.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax10.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax10.scatter(np.array(neutLHC.BBRlike["M1GUT"])/1000., np.array(neutLHC.BBRlike["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax10.scatter(np.array(neutLHC.Winolike["M1GUT"])/1000., np.array(neutLHC.Winolike["DAMU"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=20, alpha=.8, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax10.scatter(np.array(neutLHC.HRlike["M1GUT"])/1000., np.array(neutLHC.HRlike["DAMU"]), s=4, c='lightgreen',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax10.scatter(np.array(neutLHC.Higgsinolike["M1GUT"])/1000., np.array(neutLHC.Higgsinolike["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax10.scatter(np.array(neutLHC.Mixedmchi1["M1GUT"])/1000., np.array(neutLHC.Mixedmchi1["DAMU"]), s=4, c='cyan',marker='o',linewidth = '0.0',zorder=40,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )

#ax10.scatter(np.array(neutLHC.param["M2GUT"]/1000.), np.array(neutLHC.param["DAMU"]), c="cyan", cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP\ Scenario} $" )

#ax10.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax10.scatter(np.array(sneutrinoLHC.param["M2GUT"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )


xmin = -5.0
xmax = 5.0
ymin = 0.0
ymax = 45.0

#cbar10.set_clim(0.0, 700)

ax10.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle M_1 {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax10.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax10.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax10.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax10.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax10.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax10.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax10.xaxis.set_major_locator(MultipleLocator(1))
ax10.xaxis.set_minor_locator(MultipleLocator(0.25))

ax10.yaxis.set_major_locator(MultipleLocator(5))
ax10.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax10.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_DAMU_M1GUT.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax11 = plt.subplots()

#ax11.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax11.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax11.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax11.scatter(np.array(neutLHC.BBRlike["mchi1"])/1000., np.array(neutLHC.BBRlike["Microsigmav"]), s=4, c='lime',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ LSP} $" )

ax11.scatter(np.array(neutLHC.Winolike["mchi1"])/1000., np.array(neutLHC.Winolike["Microsigmav"]), s=4, c='orangered',marker='o',linewidth = '0.0',zorder=40, alpha=.8, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax11.scatter(np.array(neutLHC.HRlike["mchi1"])/1000., np.array(neutLHC.HRlike["Microsigmav"]), s=4, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ LSP} $" )

ax11.scatter(np.array(neutLHC.Higgsinolike["mchi1"])/1000., np.array(neutLHC.Higgsinolike["Microsigmav"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ LSP} $" )

ax11.scatter(np.array(neutLHC.Mixedmchi1["mchi1"])/1000., np.array(neutLHC.Mixedmchi1["Microsigmav"]), s=4, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ LSP} $" )

#ax11.scatter(np.array(neutLHC.param["M2GUT"]/1000.), np.array(neutLHC.param["DAMU"]), c="cyan", cmap=cm, s=10, marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP\ Scenario} $" )

#ax11.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax11.scatter(np.array(sneutrinoLHC.param["M2GUT"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )

ax11.plot(fermilatbbbarWIMPmass/1000.,fermilatbbbarsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ b\overline{b}} $",color='k', linewidth=2.0, zorder=310,alpha=0.7)

ax11.plot(fermilatWWWIMPmass/1000.,fermilatWWsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ W^-W^+} $",color='blue', linewidth=2.0, zorder=300,alpha=0.7)

ax11.plot(fermilattautauWIMPmass/1000.,fermilattautausigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \tau^-\tau^+} $",color='m', linewidth=2.0, zorder=305,alpha=0.7)

ax11.plot(fermilatmumuWIMPmass/1000.,fermilatmumusigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \mu^-\mu^+} $",color='olive', linewidth=2.0, zorder=300,alpha=0.7)

xmin = 0.0
xmax = 1.8
ymin = 1e-35
ymax = 1e-21

ax11.fill_between(fermilatbbbarWIMPmass/1000., fermilatbbbarsigmav, ymax , facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=25, label="Excluded by Fermi-LAT")

#cbar11.set_clim(0.0, 700)

ax11.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle < \sigma v> {\rm\ [cm^3s^{-1}]} $ ", fontsize=20)

ax11.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax11.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax11.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax11.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax11.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax11.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax11.xaxis.set_major_locator(MultipleLocator(0.2))
ax11.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax11.yaxis.set_major_locator(MultipleLocator(5))
#ax11.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax11.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_mchi1_sigmav.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax12 = plt.subplots()

#ax12.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax12.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax12.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax12.scatter(np.array(neutrelic.BBRlike["mchi1"])/1000., np.array(neutrelic.BBRlike["Microsigmav"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

ax12.scatter(np.array(neutrelic.Winolike["mchi1"])/1000., np.array(neutrelic.Winolike["Microsigmav"]), s=12, c='orangered',marker='o',linewidth = '0.0',zorder=40, alpha=.8, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax12.scatter(np.array(neutrelic.HRlike["mchi1"])/1000., np.array(neutrelic.HRlike["Microsigmav"]), s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )

ax12.scatter(np.array(neutrelic.Higgsinolike["mchi1"])/1000., np.array(neutrelic.Higgsinolike["Microsigmav"]), s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax12.scatter(np.array(neutrelic.Mixedmchi1["mchi1"])/1000., np.array(neutrelic.Mixedmchi1["Microsigmav"]), s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )

ax12.scatter(np.array(neutLHC.param["mchi1"]/1000.), np.array(neutLHC.param["Microsigmav"]), c="lightblue", cmap=cm, s=3, marker='o',linewidth = '0.0',zorder=5,label= r"$ {\rm\ Excluded\ by\ \Omega h^2\ bound} $" )

#ax12.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax12.scatter(np.array(sneutrinoLHC.param["M2GUT"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )

ax12.plot(fermilatbbbarWIMPmass/1000.,fermilatbbbarsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ b\overline{b}} $",color='k', linewidth=2.0, zorder=310,alpha=0.7)

ax12.plot(fermilatWWWIMPmass/1000.,fermilatWWsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ W^-W^+} $",color='blue', linewidth=2.0, zorder=300,alpha=0.7)

ax12.plot(fermilattautauWIMPmass/1000.,fermilattautausigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \tau^-\tau^+} $",color='m', linewidth=2.0, zorder=305,alpha=0.7)

ax12.plot(fermilatmumuWIMPmass/1000.,fermilatmumusigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \mu^-\mu^+} $",color='olive', linewidth=2.0, zorder=300,alpha=0.7)

xmin = 0.0
xmax = 1.8
ymin = 1e-35
ymax = 1e-21

ax12.fill_between(fermilatbbbarWIMPmass/1000., fermilatbbbarsigmav, ymax , facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=25, label="Excluded by Fermi-LAT")

#cbar12.set_clim(0.0, 700)

ax12.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle < \sigma v> {\rm\ [cm^3s^{-1}]} $ ", fontsize=20)

ax12.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax12.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax12.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax12.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax12.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax12.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax12.xaxis.set_major_locator(MultipleLocator(0.2))
ax12.xaxis.set_minor_locator(MultipleLocator(0.05))

#ax12.yaxis.set_major_locator(MultipleLocator(5))
#ax12.yaxis.set_minor_locator(MultipleLocator(1))

plt.yscale('log')

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_mchi1_sigmavwithrelicbound.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax13 = plt.subplots()

#ax13.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax13.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax13.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


ax13.scatter(np.array(neutrelic.BBRlike["mchi1"])/1000., np.array(neutrelic.BBRlike["mcha1"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

ax13.scatter(np.array(neutrelic.Winolike["mchi1"])/1000., np.array(neutrelic.Winolike["mcha1"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=40, alpha=.9, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax13.scatter(np.array(neutrelic.HRlike["mchi1"])/1000., np.array(neutrelic.HRlike["mcha1"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )

ax13.scatter(np.array(neutrelic.Higgsinolike["mchi1"])/1000., np.array(neutrelic.Higgsinolike["mcha1"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax13.scatter(np.array(neutrelic.Mixedmchi1["mchi1"])/1000., np.array(neutrelic.Mixedmchi1["mcha1"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )

ax13.scatter(np.array(neutLHC.param["mchi1"]/1000.), np.array(neutLHC.param["mcha1"])/1000., c="lightblue", cmap=cm, s=3, marker='o',linewidth = '0.0',zorder=5,label= r"$ {\rm\ Excluded\ by\ \Omega h^2\ bound} $" )

#ax13.scatter(np.array(neutrelic.param["m0"]), np.array(neutrelic.param["DAMU"]), s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax13.scatter(np.array(sneutrinoLHC.param["M2GUT"]/1000.), np.array(sneutrinoLHC.param["DAMU"]), s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ LSP\ Scenario} $" )

#ax13.plot(fermilatbbbarWIMPmass/1000.,fermilatbbbarsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ b\overline{b}} $",color='k', linewidth=2.0, zorder=310,alpha=0.7)

#ax13.plot(fermilatWWWIMPmass/1000.,fermilatWWsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ W^-W^+} $",color='blue', linewidth=2.0, zorder=300,alpha=0.7)

#ax13.plot(fermilattautauWIMPmass/1000.,fermilattautausigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \tau^-\tau^+} $",color='m', linewidth=2.0, zorder=305,alpha=0.7)

#ax13.plot(fermilatmumuWIMPmass/1000.,fermilatmumusigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \mu^-\mu^+} $",color='olive', linewidth=2.0, zorder=300,alpha=0.7)

xmin = 0.0
xmax = 2.2
ymin = 0.0
ymax = 2.2

#ax13.fill_between(fermilatbbbarWIMPmass/1000., fermilatbbbarsigmav, ymax , facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=25, label="Excluded by Fermi-LAT")

#cbar13.set_clim(0.0, 700)

ax13.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_1^\pm} {\rm\ [TeV]}$", fontsize=20)

#ax13.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
#ax13.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
#ax13.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

#ax13.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
#ax13.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
#ax13.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax13.xaxis.set_major_locator(MultipleLocator(0.2))
ax13.xaxis.set_minor_locator(MultipleLocator(0.05))

ax13.yaxis.set_major_locator(MultipleLocator(0.2))
ax13.yaxis.set_minor_locator(MultipleLocator(0.05))

#plt.yscale('log')

# Set both ticks to be outside
ax13.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_mcha1_mcha1_forDM.png")   # save the figure to file
plt.close(fig)

############################################################################################

cm = plt.cm.get_cmap('rainbow')

fig, ax14 = plt.subplots()

#ax14.scatter(np.array(neutLHC.LeftSv1["m0"])/1000., np.array(neutLHC.LeftSv1["DAMU"]), s=4, c='yellow',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ \widetilde{\nu}_L\ like\ \widetilde{\nu}_1} $" )

#ax14.scatter(np.array(neutLHC.RightSv1["m0"])/1000., np.array(neutLHC.RightSv1["DAMU"]), s=4, c='firebrick',marker='o',linewidth = '0.0',zorder=30, alpha=.75, label= r"$ {\rm\ \widetilde{\nu}_R\ like\ \widetilde{\nu}_1} $" )


#ax14.scatter(np.array(neutLHC.MixedSv1["m0"])/1000., np.array(neutLHC.MixedSv1["DAMU"]), s=4, c='green',marker='o',linewidth = '0.0',zorder=20, alpha=.75, label= r"$ {\rm\ Mixed\ \widetilde{\nu}_1} $" )


#ax14.scatter(np.array(neutLHC.BBRlike["mchi1"])/1000., np.array(neutLHC.BBRlike["mcha1"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

#ax14.scatter(np.array(neutLHC.Winolike["mchi1"])/1000., np.array(neutLHC.Winolike["mcha1"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=40, alpha=.9, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax14.scatter(np.array(neutLHC.HRlike["mchi1"])/1000., np.array(neutLHC.HRlike["mcha1"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )

#ax14.scatter(np.array(neutLHC.Higgsinolike["mchi1"])/1000., np.array(neutLHC.Higgsinolike["mcha1"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=50,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax14.scatter(np.array(neutLHC.Mixedmchi1["mchi1"])/1000., np.array(neutLHC.Mixedmchi1["mcha1"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )

ax14.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["mcha1"])/1000., c="lightblue", cmap=cm, s=3, marker='o',linewidth = '0.0',zorder=5, label= r"$ {\rm\ Neutralino\ LSP} $" )

#ax14.scatter(np.array(neutrelic.param["mchi1"])/1000., np.array(neutrelic.param["mcha1"])/1000., s=10, c='Red',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ DM} $" )

#ax14.scatter(np.array(sneutrinorelic.param["mchi1"])/1000., np.array(sneutrinorelic.param["mcha1"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Sneutrino\ DM} $" )

ax14.scatter(np.array(neutLHC.muong2_1sig["mchi1"])/1000., np.array(neutLHC.muong2_1sig["mcha1"])/1000., s=12, c='yellow',marker='o',linewidth = '0.0',zorder=20,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 1 \sigma }$" )

ax14.scatter(np.array(neutLHC.muong2_2sig["mchi1"])/1000., np.array(neutLHC.muong2_2sig["mcha1"])/1000., s=12, c='y',marker='o',linewidth = '0.0',zorder=19,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 2 \sigma }$" )

#ax14.plot(fermilatbbbarWIMPmass/1000.,fermilatbbbarsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ b\overline{b}} $",color='k', linewidth=2.0, zorder=310,alpha=0.7)

#ax14.plot(fermilatWWWIMPmass/1000.,fermilatWWsigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ W^-W^+} $",color='blue', linewidth=2.0, zorder=300,alpha=0.7)

#ax14.plot(fermilattautauWIMPmass/1000.,fermilattautausigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \tau^-\tau^+} $",color='m', linewidth=2.0, zorder=305,alpha=0.7)

#ax14.plot(fermilatmumuWIMPmass/1000.,fermilatmumusigmav, '--',label=r"$\displaystyle {\rm\ Fermi-LAT\ \mu^-\mu^+} $",color='olive', linewidth=2.0, zorder=300,alpha=0.7)

xmin = 0.0
xmax = 2.2
ymin = 0.0
ymax = 2.2

#ax14.fill_between(fermilatbbbarWIMPmass/1000., fermilatbbbarsigmav, ymax , facecolor = 'yellow', interpolate=True, alpha=.2,linewidth=0.0, zorder=25, label="Excluded by Fermi-LAT")

#cbar14.set_clim(0.0, 700)

ax14.axis([xmin,xmax,ymin,ymax])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_1^0} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{\chi}_1^\pm} {\rm\ [TeV]}$", fontsize=20)

#ax14.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
#ax14.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
#ax14.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

#ax14.text(xmax + 0.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
#ax14.text(xmax + 0.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
#ax14.text(xmax + 0.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax14.xaxis.set_major_locator(MultipleLocator(0.2))
ax14.xaxis.set_minor_locator(MultipleLocator(0.05))

ax14.yaxis.set_major_locator(MultipleLocator(0.2))
ax14.yaxis.set_minor_locator(MultipleLocator(0.05))

#plt.yscale('log')

# Set both ticks to be outside
ax14.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True)
leg.set_zorder(100)

fig.savefig( plotdirpath + projectname + "_mcha1_mcha1_formuong2.png")   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax15 = plt.subplots()

ax15.scatter(np.array(neutLHC.param["gluino"])/1000., np.array(neutLHC.param["squarkmass"])/1000., s=3, c='lightblue',marker='o',linewidth = '0.0',zorder=15, label= r"$ {\rm\ Neutralino\ LSP\ Solutions} $")

ax15.plot(GLUINOMASS/1000.,SQUARKSMASS/1000.,label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=40,alpha=0.5)

ax15.scatter(np.array(neutLHC.muong2_1sig["gluino"])/1000., np.array(neutLHC.muong2_1sig["squarkmass"])/1000., s=12, c='yellow',marker='o',linewidth = '0.0',zorder=20,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 1 \sigma }$" )

ax15.scatter(np.array(neutLHC.muong2_2sig["gluino"])/1000., np.array(neutLHC.muong2_2sig["squarkmass"])/1000., s=12, c='y',marker='o',linewidth = '0.0',zorder=19,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 2 \sigma }$" )

ax15.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35,linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax15.axis([1.,10.,1.,9.])
plt.xlabel(r"$\displaystyle m_{\widetilde{g}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{q}} {\rm\ [TeV]} $", fontsize=20)

ax15.xaxis.set_major_locator(MultipleLocator(1.))
ax15.xaxis.set_minor_locator(MultipleLocator(0.2))

ax15.yaxis.set_major_locator(MultipleLocator(1.))
ax15.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax15.tick_params(which='both', direction='out')

plt.legend(loc='upper left',frameon=False)

fig.savefig( plotdirpath + projectname + "_gluino_squarks_formuong2.png")   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax16 = plt.subplots()

ax16.scatter(np.array(neutLHC.param["gluino"])/1000., np.array(neutLHC.param["squarkmass"])/1000., s=3, c='lightblue',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ Neutralino\ LSP\ Excluded\ by\ \Omega_{DM} h^2\ bound} $")

ax16.scatter(np.array(neutrelic.param["gluino"])/1000., np.array(neutrelic.param["squarkmass"])/1000., s=10, c='red',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ 0.09 < \Omega_{DM} h^2\ < 0.14} $")


#ax16.scatter(np.array(neutrelic.Higgsinolike["gluino"])/1000., np.array(neutrelic.Higgsinolike["squarkmass"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax16.scatter(np.array(neutrelic.BBRlike["gluino"])/1000., np.array(neutrelic.BBRlike["squarkmass"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

#ax16.scatter(np.array(neutrelic.Winolike["gluino"])/1000., np.array(neutrelic.Winolike["squarkmass"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=30, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax16.scatter(np.array(neutrelic.HRlike["gluino"])/1000., np.array(neutrelic.HRlike["squarkmass"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )


#ax16.scatter(np.array(neutrelic.Mixedmchi1["gluino"])/1000., np.array(neutrelic.Mixedmchi1["squarkmass"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )


ax16.plot(GLUINOMASS/1000., SQUARKSMASS/1000., label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=40,alpha=0.5)

ax16.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35, linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax16.axis([1.,10.,1.,9.])
plt.xlabel(r"$\displaystyle m_{\widetilde{g}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{\widetilde{q}} {\rm\ [TeV]} $", fontsize=20)

ax16.xaxis.set_major_locator(MultipleLocator(1.))
ax16.xaxis.set_minor_locator(MultipleLocator(0.2))

ax16.yaxis.set_major_locator(MultipleLocator(1.))
ax16.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax16.tick_params(which='both', direction='out')

plt.legend(loc='upper left',frameon=False)

fig.savefig( plotdirpath + projectname + "_gluino_squarks_forDM.png")   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax17 = plt.subplots()

ax17.scatter(np.array(neutLHC.param["tanb"]), np.array(neutLHC.param["massAh3"])/1000., s=3, c='lightblue',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ Neutralino\ LSP\ Excluded\ by\ \Omega_{DM} h^2\ bound} $")

#ax17.scatter(np.array(neutrelic.param["tanb"]), np.array(neutrelic.param["massAh3"])/1000., s=10, c='red',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ 0.09 < \Omega_{DM} h^2\ < 0.14} $")

ax17.scatter(np.array(neutLHC.muong2_1sig["tanb"]), np.array(neutLHC.muong2_1sig["massAh3"])/1000., s=12, c='yellow',marker='o',linewidth = '0.0',zorder=20,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 1 \sigma }$" )

ax17.scatter(np.array(neutLHC.muong2_2sig["tanb"]), np.array(neutLHC.muong2_2sig["massAh3"])/1000., s=12, c='y',marker='o',linewidth = '0.0',zorder=19,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 2 \sigma }$" )

#ax17.scatter(np.array(neutrelic.Higgsinolike["gluino"])/1000., np.array(neutrelic.Higgsinolike["squarkmass"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax17.scatter(np.array(neutrelic.BBRlike["gluino"])/1000., np.array(neutrelic.BBRlike["squarkmass"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

#ax17.scatter(np.array(neutrelic.Winolike["gluino"])/1000., np.array(neutrelic.Winolike["squarkmass"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=30, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax17.scatter(np.array(neutrelic.HRlike["gluino"])/1000., np.array(neutrelic.HRlike["squarkmass"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=30, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )


#ax17.scatter(np.array(neutrelic.Mixedmchi1["gluino"])/1000., np.array(neutrelic.Mixedmchi1["squarkmass"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )


#ax17.plot(GLUINOMASS/1000., SQUARKSMASS/1000., label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=40,alpha=0.5)

#ax17.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35, linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax17.axis([2.,60.,0.,6.])
plt.xlabel(r"$\displaystyle tan\beta $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{A_1} {\rm\ [TeV]} $", fontsize=20)

ax17.xaxis.set_major_locator(MultipleLocator(10.))
ax17.xaxis.set_minor_locator(MultipleLocator(2.))

ax17.yaxis.set_major_locator(MultipleLocator(1.))
ax17.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax17.tick_params(which='both', direction='out')

plt.legend(loc='upper right',frameon=True)

fig.savefig( plotdirpath + projectname + "_massAh3_tanb_formuong2.png")   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax18 = plt.subplots()

ax18.scatter(np.array(neutLHC.param["tanb"]), np.array(neutLHC.param["massAh3"])/1000., s=3, c='lightblue',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ Neutralino\ LSP\ Excluded\ by\ \Omega_{DM} h^2\ bound} $")

#ax18.scatter(np.array(neutrelic.param["tanb"]), np.array(neutrelic.param["massAh3"])/1000., s=10, c='red',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ 0.09 < \Omega_{DM} h^2\ < 0.14} $")

#ax18.scatter(np.array(neutLHC.muong2_1sig["tanb"]), np.array(neutLHC.muong2_1sig["massAh3"])/1000., s=12, c='yellow',marker='o',linewidth = '0.0',zorder=20,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 1 \sigma }$" )

#ax18.scatter(np.array(neutLHC.muong2_2sig["tanb"]), np.array(neutLHC.muong2_2sig["massAh3"])/1000., s=12, c='y',marker='o',linewidth = '0.0',zorder=19,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 2 \sigma }$" )

ax18.scatter(np.array(neutrelic.Higgsinolike["tanb"]), np.array(neutrelic.Higgsinolike["massAh3"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax18.scatter(np.array(neutrelic.BBRlike["tanb"]), np.array(neutrelic.BBRlike["massAh3"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=30,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

ax18.scatter(np.array(neutrelic.Winolike["tanb"]), np.array(neutrelic.Winolike["massAh3"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=50, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

ax18.scatter(np.array(neutrelic.HRlike["tanb"]), np.array(neutrelic.HRlike["massAh3"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=40, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )


ax18.scatter(np.array(neutrelic.Mixedmchi1["tanb"]), np.array(neutrelic.Mixedmchi1["massAh3"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=60,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )


#ax18.plot(GLUINOMASS/1000., SQUARKSMASS/1000., label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=40,alpha=0.5)

#ax18.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35, linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax18.axis([2.,60.,0.,6.])
plt.xlabel(r"$\displaystyle tan\beta $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{A_1} {\rm\ [TeV]} $", fontsize=20)

ax18.xaxis.set_major_locator(MultipleLocator(10.))
ax18.xaxis.set_minor_locator(MultipleLocator(2.))

ax18.yaxis.set_major_locator(MultipleLocator(1.))
ax18.yaxis.set_minor_locator(MultipleLocator(0.2))

# Set both ticks to be outside
ax18.tick_params(which='both', direction='out')

plt.legend(loc='upper right',frameon=True)

fig.savefig( plotdirpath + projectname + "_massAh3_tanb_forDM.png")   # save the figure to file
plt.close(fig)

#########################################################################

fig, ax19 = plt.subplots()

ax19.scatter(np.array(neutLHC.param["mchi1"])/1000., np.array(neutLHC.param["masshh1"]), s=3, c='lightblue',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ Neutralino\ LSP\ Excluded\ by\ \Omega_{DM} h^2\ bound} $")

#ax19.scatter(np.array(neutrelic.param["tanb"]), np.array(neutrelic.param["massAh3"])/1000., s=10, c='red',marker='o',linewidth = '0.0',zorder=10, label= r"$ {\rm\ 0.09 < \Omega_{DM} h^2\ < 0.14} $")

ax19.scatter(np.array(neutLHC.muong2_1sig["mchi1"])/1000., np.array(neutLHC.muong2_1sig["masshh1"]), s=12, c='yellow',marker='o',linewidth = '0.0',zorder=20,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 1 \sigma }$" )

ax19.scatter(np.array(neutLHC.muong2_2sig["mchi1"])/1000., np.array(neutLHC.muong2_2sig["masshh1"]), s=12, c='y',marker='o',linewidth = '0.0',zorder=19,label= r"$\displaystyle \Delta a_{\mu}\ {\rm in\ 2 \sigma }$" )

#ax19.scatter(np.array(neutrelic.Higgsinolike["tanb"]), np.array(neutrelic.Higgsinolike["massAh3"])/1000., s=12, c='firebrick',marker='o',linewidth = '0.0',zorder=20,label= r"$ {\rm\ Higgsino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax19.scatter(np.array(neutrelic.BBRlike["tanb"]), np.array(neutrelic.BBRlike["massAh3"])/1000., s=12, c='green',marker='o',linewidth = '0.0',zorder=30,label= r"$ {\rm\ Mixed-Binos\ \widetilde{\chi}_1^0\ DM} $" )

#ax19.scatter(np.array(neutrelic.Winolike["tanb"]), np.array(neutrelic.Winolike["massAh3"])/1000., s=12, c='orangered',marker='o',linewidth = '0.0',zorder=50, label= r"$ {\rm\ Wino-like\ \widetilde{\chi}_1^0\ DM} $" )

#ax19.scatter(np.array(neutrelic.HRlike["tanb"]), np.array(neutrelic.HRlike["massAh3"])/1000., s=12, c='lightcoral',marker='o',linewidth = '0.0',zorder=40, alpha=.9, label= r"$ {\rm\ \widetilde{H}_R-like\  \widetilde{\chi}_1^0\ DM} $" )


a#x19.scatter(np.array(neutrelic.Mixedmchi1["tanb"]), np.array(neutrelic.Mixedmchi1["massAh3"])/1000., s=12, c='deepskyblue',marker='o',linewidth = '0.0',zorder=60,label= r"$ {\rm\ Mixed\ \widetilde{\chi}_1^0\ DM} $" )


#ax19.plot(GLUINOMASS/1000., SQUARKSMASS/1000., label=r"$ {\rm\ ATLAS\ Exp.\ limit\ (36.1\ fb^{-1},\ 13\ TeV)} $",color='orange', linewidth=2.0, zorder=40,alpha=0.5)

#ax19.fill_between(gluinoobslim/1000.,squarksobslim/1000., facecolor = 'lightgrey', interpolate=True, alpha=.35, linewidth=0.0,zorder=50,label=r"$ {\rm\ obs.\ limit\ (20.3\ fb^{-1},\ 8\ TeV)} $ ")

ax19.axis([0.,0.6, 0.,130.])
plt.xlabel(r"$\displaystyle tan\beta $", fontsize=20)
plt.ylabel(r"$\displaystyle m_{A_1} {\rm\ [TeV]} $", fontsize=20)

ax19.xaxis.set_major_locator(MultipleLocator(0.1))
ax19.xaxis.set_minor_locator(MultipleLocator(0.05))

ax19.yaxis.set_major_locator(MultipleLocator(20.))
ax19.yaxis.set_minor_locator(MultipleLocator(5.))

# Set both ticks to be outside
ax19.tick_params(which='both', direction='out')

plt.legend(loc='upper right',frameon=True)

fig.savefig( plotdirpath + projectname + "_mchi1_masshh1_formuong2.png")   # save the figure to file
plt.close(fig)

