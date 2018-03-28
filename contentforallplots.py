Bcontent = NMIX11**2
Wcontent = NMIX12**2
BRcontent = NMIX15**2
HRcontent = (NMIX16**2)+(NMIX17**2)
Hcontent = (NMIX13**2)+(NMIX14**2)


BBR_mchi1=[]
BBR_relic=[]

W_mchi1=[]
W_relic=[]

HR_mchi1=[]
HR_relic=[]

H_mchi1=[]
H_relic=[]

mix_mchi1=[]
mix_relic=[]

i=0

while i < len(LSP):
    if BRcontent[i] + Bcontent[i] > .80:
            BBR_mchi1.append(mchi1[i])
            BBR_relic.append(relic[i])
    
    elif HRcontent[i] > .80:
            HR_mchi1.append(mchi1[i])
            HR_relic.append(relic[i])
 
    elif Wcontent[i] > .80:
            W_mchi1.append(mchi1[i])
            W_relic.append(relic[i])

    elif Hcontent[i] > .80:
            H_mchi1.append(mchi1[i])
            H_relic.append(relic[i])
                                 
    else:
            mix_mchi1.append(mchi1[i])      
            mix_relic.append(relic[i])
            
    i+=1

##################################################################################

fig, ax83 = plt.subplots()

sc83 = ax83.scatter(np.array(BBR_mchi1)/1000.,np.array(BBR_relic),c="lightcoral", s=3, linewidth = '0.0',marker='o',label=r"$ \displaystyle \widetilde{B}_R -\widetilde{B} {\rm\ mixed}$",zorder=10)

sc83 = ax83.scatter(np.array(mix_mchi1)/1000.,np.array(mix_relic),c="darkblue", s=6, linewidth = '0.0',marker='o',label=r"${\rm\ Mixed\ Neutralino}$",zorder=30)

sc83 = ax83.scatter(np.array(H_mchi1)/1000.,np.array(H_relic),c="darkolivegreen", s=10, linewidth = '0.0',marker='o',label=r"$\displaystyle \widetilde{H}- {\rm\ like\ Neutralino} $",zorder=40)

sc83 = ax83.scatter(np.array(HR_mchi1)/1000.,np.array(HR_relic),c="darkgoldenrod", s=3, linewidth = '0.0',marker='o',label=r"$ \displaystyle \widetilde{H}_R- {\rm\ like\ Neutralino} $",zorder=20)

#sc83 = ax83.scatter(np.array(W_mchi1)/1000.,np.array(W_relic),c="black", s=20, linewidth = '0.0',marker='o',label=r"$ \displaystyle \widetilde{W}- {\rm\ like\ Neutralino} $",zorder=50)

ax83.axis([0,1.4,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\chi}_{1}^{0}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)
                             
plt.plot([0, 1.4], [0.09, 0.09], 'k--',zorder=50)
plt.plot([0, 1.4], [0.14, 0.14], 'k--',zorder=50)

ax83.xaxis.set_major_locator(MultipleLocator(0.2))
ax83.xaxis.set_minor_locator(MultipleLocator(0.05))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax83.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True,ncol=2)
leg.set_zorder(700)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_neutralino_relic_DMcontent.png')   # save the figure to file
plt.close(fig)

###################################################################################


