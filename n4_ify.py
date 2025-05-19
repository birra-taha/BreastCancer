#!/bin/python




import glob as glob
import pandas as pd
import numpy as np
import os
import ants 

for patient in glob.glob("your/path/here/output/ss/*"):

	#print(patient)
	basename = patient.split("/")[-1].replace("_image_ss.nii.gz", "")

	print(basename)
	ss_n4_name = "your/path/here/output/ss_n4/" + basename + "_image_ss_n4.nii.gz"
	print(ss_n4_name)
	ants_orig_img = ants.image_read(patient)
	ants_orig_img_corrected = ants.n4_bias_field_correction(ants_orig_img)
	ants_orig_img_corrected.to_filename(ss_n4_name)
	print(patient)
