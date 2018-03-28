SvLeft=(SNUMIX11**2)+(SNUMIX12**2)+(SNUMIX13**2)
SvRight=(SNUMIX14**2)+(SNUMIX15**2)+(SNUMIX16**2)
Scalar=(SNUMIX17**2)+(SNUMIX18**2)+(SNUMIX19**2)

SvLeft_relic=[]
SvLeft_massd1=[]
SvLeft_gluino=[]
SvLeft_mchi1=[]
SvLeft_protonSI=[]
SvLeft_neutronSI=[]
SvLeft_nucleonSI=[]

SvLeft_fixedprotonSI=[]
SvLeft_fixedneutronSI=[]
SvLeft_fixednucleonSI=[]

SvLeft_nucleonSIstrength=[]
SvLeft_massSv1=[]


#######################################

SvRight_relic=[]
SvRight_massd1=[]
SvRight_gluino=[]
SvRight_mchi1=[]
SvRight_protonSI=[]
SvRight_neutronSI=[]
SvRight_nucleonSI=[]

SvRight_fixedprotonSI=[]
SvRight_fixedneutronSI=[]
SvRight_fixednucleonSI=[]

SvRight_nucleonSIstrength=[]
SvRight_massSv1=[]

########################################

Scalar_relic=[]
Scalar_massd1=[]
Scalar_gluino=[]
Scalar_mchi1=[]
Scalar_protonSI=[]
Scalar_neutronSI=[]
Scalar_nucleonSI=[]

Scalar_fixedprotonSI=[]
Scalar_fixedneutronSI=[]
Scalar_fixednucleonSI=[]

Scalar_nucleonSIstrength=[]
Scalar_massSv1=[]

########################################

mixedSv_relic=[]
mixedSv_massd1=[]
mixedSv_gluino=[]
mixedSv_mchi1=[]
mixedSv_protonSI=[]
mixedSv_neutronSI=[]
mixedSv_nucleonSI=[]

mixedSv_fixedprotonSI=[]
mixedSv_fixedneutronSI=[]
mixedSv_fixednucleonSI=[]

mixedSv_nucleonSIstrength=[]
mixedSv_massSv1=[]

########################################

i=0

while i < len(input):
    if SvLeft[i] > .70:
        SvLeft_relic.append(relic[i])
        SvLeft_mchi1.append(mchi1[i])
        SvLeft_protonSI.append(protonSI[i])
        SvLeft_neutronSI.append(neutronSI[i])
        SvLeft_massd1.append(massd1[i])
        SvLeft_gluino.append(gluino[i])
        SvLeft_nucleonSI.append(nucleonSI[i])
        SvLeft_fixedprotonSI.append(fixedprotonSI[i])
        SvLeft_fixednucleonSI.append(fixednucleonSI[i])
        SvLeft_nucleonSIstrength.append(nucleonSIstrength[i])
        SvLeft_massSv1.append(massSv1[i])

    elif SvRight[i] > .70:
        SvRight_relic.append(relic[i])
        SvRight_mchi1.append(mchi1[i])
        SvRight_protonSI.append(protonSI[i])
        SvRight_neutronSI.append(neutronSI[i])
        SvRight_massd1.append(massd1[i])
        SvRight_gluino.append(gluino[i])
        SvRight_nucleonSI.append(nucleonSI[i])
        SvRight_fixedprotonSI.append(fixedprotonSI[i])
        SvRight_fixednucleonSI.append(fixednucleonSI[i])
        SvRight_nucleonSIstrength.append(nucleonSIstrength[i])
        SvRight_massSv1.append(massSv1[i])

    elif Scalar[i] > .70:
        Scalar_relic.append(relic[i])
        Scalar_mchi1.append(mchi1[i])
        Scalar_protonSI.append(protonSI[i])
        Scalar_neutronSI.append(neutronSI[i])
        Scalar_massd1.append(massd1[i])
        Scalar_gluino.append(gluino[i])
        Scalar_fixedprotonSI.append(fixedprotonSI[i])
        Scalar_nucleonSI.append(nucleonSI[i])
        Scalar_fixednucleonSI.append(fixednucleonSI[i])
        Scalar_nucleonSIstrength.append(nucleonSIstrength[i])
        Scalar_massSv1.append(massSv1[i])

    else:
        mixedSv_relic.append(relic[i])  
        mixedSv_mchi1.append(mchi1[i])
        mixedSv_protonSI.append(protonSI[i])
        mixedSv_neutronSI.append(neutronSI[i])
        mixedSv_massd1.append(massd1[i])
        mixedSv_gluino.append(gluino[i])
        mixedSv_fixedprotonSI.append(fixedprotonSI[i])
        mixedSv_nucleonSI.append(nucleonSI[i])
        mixedSv_fixednucleonSI.append(fixednucleonSI[i])
        mixedSv_nucleonSIstrength.append(nucleonSIstrength[i])
        mixedSv_massSv1.append(massSv1[i])

    i+=1

################################################################



##################################################################################

fig, ax12 = plt.subplots()

#sc12 = ax12.scatter(np.array(SvLeft_massSv1)/1000.,np.array(SvLeft_relic),c="green", s=25, linewidth = '0.0',marker='o', label=r"$\displaystyle \widetilde{\nu}_{L} {\rm\ -like\ DM} $",zorder=10)

sc12 = ax12.scatter(np.array(SvRight_massSv1)/1000.,np.array(SvRight_relic),c="darkblue", s=10, linewidth = '0.0',marker='o', label=r"$\displaystyle \widetilde{\nu}_{R} {\rm\ -like\ DM} $",zorder=30)

sc12 = ax12.scatter(np.array(Scalar_massSv1)/1000.,np.array(Scalar_relic),c="olivedrab", s=15, linewidth = '0.0',marker='o', label=r"$\displaystyle \widetilde{\nu}_{S} {\rm\ -like\ DM} $",zorder=40)

sc12 = ax12.scatter(np.array(mixedSv_massSv1)/1000.,np.array(mixedSv_relic),c="orange", s=10, linewidth = '0.0',marker='o', label=r"$\displaystyle \widetilde{\nu}_{R}-\widetilde{\nu}_{S} {\rm\ mixed\ DM} $",zorder=20)


ax12.axis([0,1.,1e-3,1e4])
plt.xlabel(r"$\displaystyle m_{\widetilde{\nu}_{1}} {\rm\ [TeV]} $", fontsize=20)
plt.ylabel(r"$\displaystyle \Omega_{DM}h^{2} $ ", fontsize=20)

plt.plot([0, 1.], [0.09, 0.09], 'k--',zorder=50)
plt.plot([0, 1.], [0.14, 0.14], 'k--',zorder=50)

ax12.xaxis.set_major_locator(MultipleLocator(0.1))
ax12.xaxis.set_minor_locator(MultipleLocator(0.025))

#plt.xscale('log')
plt.yscale('log')

# Set both ticks to be outside
ax12.tick_params(which='both', direction='out')

leg = plt.legend(loc='lower right',frameon=True,ncol=1)
leg.set_zorder(700)

fig.savefig('/Users/oozdal/projects/mchiRBLR/plot/nonBL_sneutrino_relic_DMcontent.png')   # save the figure to file

plt.close(fig)

###################################################################################
