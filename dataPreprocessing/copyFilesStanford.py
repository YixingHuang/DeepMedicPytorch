import glob
import os
import shutil

label_path = 'C:/Data/BrainMetShare/*_labelmap_registered.nii.gz'
label_suffix = '_labelmap_registered.nii.gz'
input_suffix = '_normed_registered_n4.nii.gz'
label_names = glob.glob(label_path)
new_folder = 'C:/Data/StanfordMetShare/'
for name in label_names:
    patient_name = os.path.basename(name)
    patient_ID = patient_name[:-len(label_suffix)]
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
