neutralino_DAMU=[]
neutralino_tanb=[]
neutralino_mhf=[]
neutralino_m0=[]
neutralino_A0=[]
neutralino_masshh1=[]
neutralino_masshh2=[]
neutralino_masshh3=[]
neutralino_masshh4=[]
neutralino_massAh3=[]
neutralino_massAh4=[]
neutralino_vR=[]
neutralino_massVZR=[]
neutralino_BRZpallleptons=[]
neutralino_relic=[]
neutralino_mchi1=[]
neutralino_BRZpsleptons=[]
neutralino_BRZjets=[]
neutralino_BRZXX=[]
neutralino_ys3_GUT=[]
neutralino_yv3_GUT=[]
neutralino_MuR=[]
neutralino_Mu=[]
neutralino_MSUSY=[]
neutralino_vR=[]
neutralino_BmuR=[]
neutralino_Bmu=[]


sneutrino_DAMU=[]
sneutrino_tanb=[]
sneutrino_mhf=[]
sneutrino_m0=[]
sneutrino_A0=[]
sneutrino_masshh1=[]
sneutrino_masshh2=[]
sneutrino_masshh3=[]
sneutrino_masshh4=[]
sneutrino_massAh3=[]
sneutrino_massAh4=[]
sneutrino_vR=[]
sneutrino_massVZR=[]
sneutrino_BRZpallleptons=[]
sneutrino_relic=[]
sneutrino_mchi1=[]
sneutrino_BRZpsleptons=[]
sneutrino_BRZjets=[]
sneutrino_BRZXX=[]
sneutrino_ys3_GUT=[]
sneutrino_yv3_GUT=[]
sneutrino_MuR=[]
sneutrino_Mu=[]
sneutrino_MSUSY=[]
sneutrino_vR=[]
sneutrino_BmuR=[]
sneutrino_Bmu=[]

i=0



while i < len(input):
    if LSP[i] == 1000022:
        neutralino_DAMU.append(DAMU[i])
        neutralino_tanb.append(tanb[i])
        neutralino_mhf.append(mhf[i])
        neutralino_m0.append(m0[i])
        neutralino_A0.append(A0[i])
        neutralino_masshh2.append(masshh2[i])
        neutralino_masshh1.append(masshh1[i])
        neutralino_masshh3.append(masshh3[i])
        neutralino_masshh4.append(masshh4[i])
        neutralino_massAh3.append(massAh3[i])
        neutralino_massAh4.append(massAh4[i])
        neutralino_vR.append(vR[i])
        neutralino_massVZR.append(massVZR[i])
        neutralino_BRZpallleptons.append(BRZpallleptons[i])
        neutralino_relic.append(relic[i])
        neutralino_mchi1.append(mchi1[i])
        neutralino_BRZpsleptons.append(BRZpsleptons[i])
        neutralino_BRZjets.append(BRZjets[i])
        neutralino_BRZXX.append(BRZXX[i])
        neutralino_ys3_GUT.append(ys3_GUT[i])
        neutralino_yv3_GUT.append(yv3_GUT[i])
        neutralino_MuR.append(MuR[i])
        neutralino_Mu.append(Mu[i])
        neutralino_MSUSY.append(MSUSY[i])
        neutralino_BmuR.append(BmuR[i])
        neutralino_Bmu.append(Bmu[i])

    if LSP[i] == 1000012:
        sneutrino_DAMU.append(DAMU[i])
        sneutrino_tanb.append(tanb[i])
        sneutrino_mhf.append(mhf[i])
        sneutrino_m0.append(m0[i])
        sneutrino_A0.append(A0[i])
        sneutrino_masshh2.append(masshh2[i])
        sneutrino_masshh1.append(masshh1[i])
        sneutrino_masshh3.append(masshh3[i])
        sneutrino_masshh4.append(masshh4[i])
        sneutrino_massAh3.append(massAh3[i])
        sneutrino_massAh4.append(massAh4[i])
        sneutrino_vR.append(vR[i])
        sneutrino_massVZR.append(massVZR[i])
        sneutrino_BRZpallleptons.append(BRZpallleptons[i])
        sneutrino_relic.append(relic[i])
        sneutrino_mchi1.append(mchi1[i])
        sneutrino_BRZpsleptons.append(BRZpsleptons[i])
        sneutrino_BRZjets.append(BRZjets[i])
        sneutrino_BRZXX.append(BRZXX[i])
        sneutrino_ys3_GUT.append(ys3_GUT[i])
        sneutrino_yv3_GUT.append(yv3_GUT[i])
        sneutrino_MuR.append(MuR[i])
        sneutrino_Mu.append(Mu[i])
        sneutrino_MSUSY.append(MSUSY[i])
        sneutrino_BmuR.append(BmuR[i])
        sneutrino_Bmu.append(Bmu[i])


    i+=1

#################################################################################################

fig, ax104 = plt.subplots()

ax104.scatter(np.array(neutralino_Mu)/1000., np.array(neutralino_DAMU)*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax104.scatter(np.array(sneutrino_Mu)/1000., np.array(sneutrino_DAMU)*10**10, s=10, c='deepskyblue', marker='o',linewidth = '0.0',zorder=20, label= r"$ {\rm\ Sneutrino\ LSP} $" )

ax104.axis([0,5.0,-5.,60])
plt.xlabel(r"$\displaystyle \mu {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax104.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax104.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax104.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax104.text(6.2, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax104.text(6.2, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax104.text(6.2, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax104.xaxis.set_major_locator(MultipleLocator(0.5))
ax104.xaxis.set_minor_locator(MultipleLocator(0.1))

ax104.yaxis.set_major_locator(MultipleLocator(5))
ax104.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax104.tick_params(which='both', direction='out')

leg = plt.legend(loc='upper right',frameon=True)
leg.set_zorder(100)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_DAMU_Mu_BOTH.png')   # save the figure to file
plt.close(fig)

##############################################################################################

fig, ax91 = plt.subplots()

ax91.scatter(np.array(neutralino_mhf)/1000., np.array(neutralino_DAMU)*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax91.scatter(np.array(sneutrino_mhf)/1000., np.array(sneutrino_DAMU)*10**10, s=10, c='deepskyblue', marker='o',linewidth = '0.0',zorder=20, label= r"$ {\rm\ Sneutrino\ LSP} $" )

ax91.axis([0.5,3.0,0.0,60])
plt.xlabel(r"$\displaystyle M_{1/2} {\rm\ [TeV]}$", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax91.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax91.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax91.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax91.text(3.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax91.text(3.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax91.text(3.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax91.xaxis.set_major_locator(MultipleLocator(0.5))
ax91.xaxis.set_minor_locator(MultipleLocator(0.1))

ax91.yaxis.set_major_locator(MultipleLocator(5))
ax91.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax91.tick_params(which='both', direction='out')

leg = plt.legend(loc='best',frameon=True)
leg.set_zorder(100)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_DAMU_mhf_BOTH.png')   # save the figure to file
plt.close(fig)

##########################################################################

fig, ax88 = plt.subplots()

ax88.scatter(np.array(neutralino_m0)/1000., np.array(neutralino_DAMU)*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax88.scatter(np.array(sneutrino_m0)/1000., np.array(sneutrino_DAMU)*10**10, s=10, c='deepskyblue', marker='o',linewidth = '0.0',zorder=20, label= r"$ {\rm\ Sneutrino\ LSP} $" )

ax88.axis([0,3.0,0.0,60])
plt.xlabel(r"$\displaystyle m_0 {\rm\ (TeV)} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax88.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax88.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax88.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax88.text(3.1, 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax88.text(3.1, 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax88.text(3.1, 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax88.xaxis.set_major_locator(MultipleLocator(0.5))
ax88.xaxis.set_minor_locator(MultipleLocator(0.1))

ax88.yaxis.set_major_locator(MultipleLocator(5))
ax88.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax88.tick_params(which='both', direction='out')

leg = plt.legend(loc='best',frameon=True)
leg.set_zorder(100)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_DAMU_m0_BOTH.png')   # save the figure to file
plt.close(fig)

#############################################################################################

fig, ax89 = plt.subplots()

ax89.scatter(np.array(neutralino_tanb), np.array(neutralino_DAMU)*10**10, s=10, c='Blue',marker='o',linewidth = '0.0',zorder=10,label= r"$ {\rm\ Neutralino\ LSP} $" )

ax89.scatter(np.array(sneutrino_tanb), np.array(sneutrino_DAMU)*10**10, s=10, c='deepskyblue', marker='o',linewidth = '0.0',zorder=20, label= r"$ {\rm\ Sneutrino\ LSP} $" )

ax89.axis([0,60.0,0.0,60.0])
plt.xlabel(r"$\displaystyle tan\beta $ ", fontsize=20)
plt.ylabel(r"$\displaystyle \Delta a_{\mu} \times 10^{10} $ ", fontsize=20)

ax89.axhspan(20.7,36.7,color='green',fill=True,alpha=.2,linewidth=0.0,zorder=4)
ax89.axhspan(12.7, 44.7,color='yellow',fill=True,alpha=.2,linewidth=0.0,zorder=3)
ax89.axhspan(3.4,55.6,color='navy',fill=True,alpha=.2,linewidth=0.0,zorder=2)

ax89.text(61., 7.4, r"$\displaystyle 3 \sigma$",fontsize=20)
ax89.text(61., 16.2, r"$\displaystyle 2 \sigma$",fontsize=20)
ax89.text(61., 28.3, r"$\displaystyle 1 \sigma$",fontsize=20)

ax89.xaxis.set_major_locator(MultipleLocator(10.0))
ax89.xaxis.set_minor_locator(MultipleLocator(2.0))

ax89.yaxis.set_major_locator(MultipleLocator(5))
ax89.yaxis.set_minor_locator(MultipleLocator(1))

# Set both ticks to be outside
ax89.tick_params(which='both', direction='out')

leg = plt.legend(loc='best',frameon=True)
leg.set_zorder(100)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_DAMU_tanb_BOTH.png')   # save the figure to file
plt.close(fig)
