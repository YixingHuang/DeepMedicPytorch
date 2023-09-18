import glob
import os
import shutil

label_path = 'C:/normalised2/*-label.nii.gz'
label_suffix = '-label.nii.gz'
input_suffix = '.nii.gz'
label_names = glob.glob(label_path)
new_folder = 'C:/Data/UKER_BM/'
for name in label_names[600:]:
    patient_name = os.path.basename(name)
    patient_ID = patient_name[:-13]
    input_name = name.replace(label_suffix, input_suffix)
    input_patient_name = patient_name.replace(label_suffix, input_suffix)
    target_label_name = new_folder + patient_ID + "/" + patient_name
    target_input_name = new_folder + patient_ID + "/" + input_patient_name
    # print(target_input_name)
    # print(input_patient_name)
    target_folder = new_folder + patient_ID
    coordinates22 = target_folder + "/" + patient_ID + "22x22x22_coords.pkl"
    coordinates22new = target_folder + "/" + patient_ID + "_22x22x22_coords.pkl"
    coordinates25 = target_folder + "/" + patient_ID + "25x25x25_coords.pkl"
    coordinates25new = target_folder + "/" + patient_ID + "_25x25x25_coords.pkl"
    coordinates28 = target_folder + "/" + patient_ID + "28x28x28_coords.pkl"
    coordinates28new = target_folder + "/" + patient_ID + "_28x28x28_coords.pkl"
    data = target_folder + "/" + patient_ID + "data_f32.pkl"
    datanew = target_folder + "/" + patient_ID + "_data_f32.pkl"
    if os.path.exists(coordinates22new):
        os.remove(coordinates22)
    elif not os.path.exists(coordinates22):
        continue
    else:
        os.rename(coordinates22, coordinates22new)
    if os.path.exists(coordinates25new):
        os.remove(coordinates25)
    elif not os.path.exists(coordinates25):
        continue
    else:
        os.rename(coordinates25, coordinates25new)
    if os.path.exists(coordinates28new):
        os.remove(coordinates28)
    elif not os.path.exists(coordinates28):
        continue
    else:
        os.rename(coordinates28, coordinates28new)
    if os.path.exists(datanew):
        os.remove(data)
    elif not os.path.exists(data):
        continue
    else:
        os.rename(data, datanew)
