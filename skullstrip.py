#/bin/python




import glob as glob
import pandas as pd
import numpy as np
import os

for patient in glob.glob("/your/path/to/patientfolders/here/*/*image.nii*"):

	#print(patient)
	basename = patient.split("/")[-2]

	ss_name = "your/path/here/output/" + basename + "_image_ss.nii.gz"
	ss_n4_name = "your/path/here/output/" + basename + "_image_ss_n4.nii.gz"

	call(['python3.6 HD-BET/HD_BET/hd-bet', -i $patient -o your/path/here/output/image_ss.nii.gz -device cpu -mode fast']) #can modify this if you have a gpu available
	
	#os.system('python3.6 time python3.6 HD-BET/HD_BET/hd-bet -i $patient -o your/path/here/output/image_ss.nii.gz -device cpu -mode fast' % ])


	print(ss_name, ss_n4_name)



#	output_patient_ss = patient.replace("image.nii.gz","image_ss.nii.").split("/")[-1]
