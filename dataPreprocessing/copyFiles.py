import glob
import os
import shutil

label_path = 'C:/normalised2/*-label.nii.gz'
label_suffix = '-label.nii.gz'
input_suffix = '.nii.gz'
label_names = glob.glob(label_path)
new_folder = 'C:/Data/UKER_BM/'
for name in label_names:
    patient_name = os.path.basename(name)
    patient_ID = patient_name[:-13]
    input_name = name.replace(label_suffix, input_suffix)
    input_patient_name = patient_name.replace(label_suffix, input_suffix)
    target_label_name = new_folder + patient_ID + "/" + patient_name
    target_input_name = new_folder + patient_ID + "/" + input_patient_name
    # print(target_input_name)
    # print(input_patient_name)
    target_folder = new_folder + patient_ID
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    shutil.copy2(name, target_label_name)
    shutil.copy2(input_name, target_input_name)
