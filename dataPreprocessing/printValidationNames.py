import glob
import os

label_path = 'C:/normalised2/*-label.nii.gz'
label_suffix = '-label.nii.gz'
input_suffix = '.nii.gz'
label_names = glob.glob(label_path)
source_folder = 'S:/AI_Radiation/Huang/FixedLabelsDataset/*_fixed-label.nii.gz'
label_names2 = glob.glob(source_folder)
label2_suffix = "_fixed-label.nii.gz"
for name in label_names[600:]:
    patient_name = os.path.basename(name)
    patient_name2 = patient_name.replace(label_suffix, label2_suffix)
    tag = 0
    for name2 in label_names2:
        patient = '!!' + os.path.basename(name2)
        if patient == patient_name2:
            tag = 1
            break
    if tag == 1:
        print(patient_name[:-13])
