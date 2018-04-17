import os

var = raw_input("Please enter prep to prepare directories, submit for job submission: ")

for i in range(2,91):
	if var == "prep":
		os.system("mkdir f" + str(i))
		with open("GenerateNewSLHA.py", 'r') as file:
            		filedata = file.read()
	
        	# Replace the target string
        	filedata = filedata.replace('startpoint', str((i-1)*2000))
		filedata = filedata.replace('endpoint', str(i*2000))

        	# Write the file out again
        	with open("f" + str(i) + "/GenerateNewSLHA_f" + str(i) + ".py", 'w') as newfile:
            		newfile.write(filedata)

		os.system("cp LesHouches.in.NaturalNonUniGauginoBLRinvSeesaw f" + str(i) + "/")
		os.system("cp pyslha-3.2.1/pyslha.py f" + str(i) +"/")

		with open("jobread.pbs", 'r') as jobfile:
                        jobfiledata = jobfile.read()

                # Replace the target string
                jobfiledata = jobfiledata.replace('directoryname', "f"+str(i))
                jobfiledata = jobfiledata.replace('filename', "GenerateNewSLHA_f"+str(i)+".py")

                # Write the file out again
                with open("f" + str(i) + "/jobsubmit_f" + str(i) + ".pbs", 'w') as newjobfile:
                        newjobfile.write(jobfiledata)		


	if var == "submit":
		os.system("cd f" + str(i) + " " + "&&" + " " + "qsub jobsubmit_f" + str(i) + ".pbs")
#		os.system("cd f" + str(i) + " " + "&&" + " " + "python GenerateNewSLHA_f" + str(i) + ".py")

