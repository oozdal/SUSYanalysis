import os, glob
import fnmatch, shutil

######################################################################
###### Edit these paths to use this code for another projects #######

projectdirpath = '/gs/scratch/oozdal/mBLRISS/NonunigauginomchiBLR/'
outfilespath = projectdirpath + 'out_files/'

#####################################################################

numberofcollectedSLHA=len(fnmatch.filter(os.listdir(outfilespath), 'stem.*'))
print "Number of collected SLHA files before = ", numberofcollectedSLHA
startnumber = numberofcollectedSLHA + 1

#####################################################

numberof_fdir = len(fnmatch.filter(os.listdir(projectdirpath), 'f*'))

for i in range(numberof_fdir):
    fno = i+1
    fpath = projectdirpath+'f'+str(fno)
    os.chdir(fpath)
    print '#########################################################'
    print 'Inserted directory', 'f'+str(fno) 

    
    numberofoutfiles = len(fnmatch.filter(os.listdir(fpath), '0*.out'))
    print 'Number of new SLHA files in f'+str(fno), numberofoutfiles
    
    if(numberofoutfiles > 0):
          for filename in glob.glob('0*.out'):
              newSLHAname = 'stem.'+str(startnumber)
              os.rename(filename, newSLHAname)
#             shutil.copy2(newSLHAname, outfilespath)
              shutil.move(newSLHAname, outfilespath) 
              print(filename)," is renamed as stem."+str(startnumber)
              startnumber+=1
    else:
          print 'No new SLHA file in f'+str(fno)


os.chdir(projectdirpath)

print '\n'
print '#########################################################\n'
print 'SUMMARY\n'
print 'Number of collected SLHA files before this run = ', numberofcollectedSLHA, '\n'
totalcollected = startnumber - 1
print 'Number of collected SLHA files during this run = ' , totalcollected-numberofcollectedSLHA, '\n'
print 'Total number of collected SLHA files = ', totalcollected

