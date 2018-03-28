rejectm0=rejectdata[:,0]
rejectmhf=rejectdata[:,1]

rejectA0=rejectdata[:,3]

rejecttanb=rejectdata[:,5]
rejecttanbp=rejectdata[:,6]
rejectvR=rejectdata[:,7]

rejectmasshh1=rejectdata[:,8]
rejectmasshh2=rejectdata[:,9]
rejectmasshh3=rejectdata[:,10]
rejectmasshh4=rejectdata[:,11]

rejectmassAh3=rejectdata[:,12]
rejectmassAh4=rejectdata[:,13]
rejectmassHpm2=rejectdata[:,14]
rejectmassWZ=rejectdata[:,15]
rejectmassVWm=rejectdata[:,16]
rejectmassVZR=rejectdata[:,17]
rejectgluino=rejectdata[:,18]

rejectmchi1=abs(rejectdata[:,19])
#rejectmchi2=abs(rejectdata[:,20])
#rejectmchi3=abs(rejectdata[:,21])
#rejectmchi4=abs(rejectdata[:,22])
#rejectmchi5=abs(rejectdata[:,23])
#rejectmchi6=abs(rejectdata[:,24])
#rejectmchi7=abs(rejectdata[:,25])
rejectmcha1=abs(rejectdata[:,26])
#rejectmcha2=abs(rejectdata[:,27])

rejectLHC8gluonfusionh1=rejectdata[:,46]
rejectLHC8vectorfusionh1=rejectdata[:,47]
rejectLHC8WHproductionh1=rejectdata[:,48]
rejectLHC8ZHproductionh1=rejectdata[:,49]
rejectLHC8ttHproductionh1=rejectdata[:,50]

rejectLHC8gluonfusionh2=rejectdata[:,51]
rejectLHC8vectorfusionh2=rejectdata[:,52]
rejectLHC8WHproductionh2=rejectdata[:,53]
rejectLHC8ZHproductionh2=rejectdata[:,54]
rejectLHC8ttHproductionh2=rejectdata[:,55]

rejectDAMU=rejectdata[:,86]  

rejectBsmumu=rejectdata[:,89]

rejectprotonSI=rejectdata[:,94]   # Proton Spin Independent Cross-Section
rejectprotonSD=rejectdata[:,95]   # Proton Spin Dependent Cross-Section

rejectneutronSI=rejectdata[:,96]  # Neutron Spin Independent Cross-Section
rejectneutronSD=rejectdata[:,97]  # Neutron Spin Dependent Cross-Section

rejectIcecube=rejectdata[:,102]

rejectmassd1=rejectdata[:,103]
#rejectmassd2=rejectdata[:,104]
#rejectmasss1=rejectdata[:,105]
#rejectmasss2=rejectdata[:,106]
rejectmassb1=rejectdata[:,107]
#rejectmassb2=rejectdata[:,108]

#rejectmassu1=rejectdata[:,109]
#rejectmassu2=rejectdata[:,110]
#rejectmassc1=rejectdata[:,111]
#rejectmassc2=rejectdata[:,112]
rejectmasst1=rejectdata[:,113]
rejectmasst2=rejectdata[:,114]

#rejectmasse1=rejectdata[:,115]
#rejectmasse2=rejectdata[:,116]
rejectmassmu1=rejectdata[:,117]
rejectmassmu2=rejectdata[:,118]
rejectmasstau1=rejectdata[:,119]
#rejectmasstau2=rejectdata[:,120]

rejectMuR=rejectdata[:,312]
rejectMu=rejectdata[:,313]
rejectBmuR=rejectdata[:,314]
rejectBmu=rejectdata[:,315]
rejectvChiRb=rejectdata[:,316]
rejectvChiR=rejectdata[:,317]
rejectvd=rejectdata[:,318]
rejectvu=rejectdata[:,319]
rejectv=rejectdata[:,320]
#rejectbetaH=rejectdata[:,321]

rejectmHd2SUSY=rejectdata[:,322]
rejectmHu2SUSY=rejectdata[:,323]
rejectmCR2SUSY=rejectdata[:,324]
rejectmCRb2SUSY=rejectdata[:,325]
rejectMBBRSUSY=rejectdata[:,326]
rejectM1SUSY=rejectdata[:,327]
rejectM2SUSY=rejectdata[:,328]
rejectM4SUSY=rejectdata[:,328]
rejectM3SUSY=rejectdata[:,330]

rejectmHd2GUT=rejectdata[:,331]
rejectmHu2GUT=rejectdata[:,332]
rejectmCR2GUT=rejectdata[:,333]
rejectmCRb2GUT=rejectdata[:,334]
rejectMBBRGUT=rejectdata[:,335]
rejectM1GUT=rejectdata[:,336]
rejectM2GUT=rejectdata[:,337]
rejectM4GUT=rejectdata[:,338]
rejectM3GUT=rejectdata[:,339]

rejectmassSv1=rejectdata[:,347]


#############################################################################
############################# Extra Calculations ############################

rejectMSUSY=(rejectdata[:,113]*rejectdata[:,114])**(1/2)

###########################################################################
