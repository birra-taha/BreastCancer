import six
import ants
import glob
import re
import numpy as np
import time
import SimpleITK as sitk
import pandas as pd
import radiomics
from radiomics import featureextractor
extractor = featureextractor.RadiomicsFeatureExtractor()
extractor.enableImageTypes()

big_df = pd.DataFrame()

for patient in glob.glob("your/path/here/output/main_patient_folders/*"):
	image = patient + "/image_ss_n4.nii.gz"
	patient_orig_image = ants.image_read(image)
	origin_original_scan = patient_orig_image.origin
	full_list = glob.glob(patient + "/*")
    #find all the segmentations (subtract out all the nonsegmentations)
#	print(patient_orig_image)
	r = re.compile(".*image*|.*tsv*")
	tt = list(filter(r.match,full_list))
	seg_list = list(set(full_list) - set(tt))
    ##############
#	print(seg_list)
#	count+=1
	print("Patient #: %s" % (patient))
	df = pd.DataFrame()

	#create an organized dataframe where columns are features, subtract out all the diagnostics, first column is the segmentation name
	for segmentation in seg_list:
		try:
			result = extractor.execute(image, segmentation)		#call pyradiomics here
			rt = [("Segmentation_Name", segmentation.split("/")[-1].replace(".nii.gz", ""))] + [(x,y) for x,y in zip(result.keys(), result.values()) if "diagnostics" not in x]
			df2 = pd.DataFrame(rt).T
			df2.columns = df2.iloc[0]
			df2 = df2.iloc[1:]
			df = pd.concat([df,df2])
		except:
			continue
	df.to_csv(patient + "/radiomic_features.tsv", sep="\t", header=True, index=False)
