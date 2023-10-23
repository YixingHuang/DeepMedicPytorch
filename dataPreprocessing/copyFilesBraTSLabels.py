import glob
import os
import shutil


def check_system():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        if 'linux' in os.uname().sysname.lower():
            return 'Linux'
        else:
            return os.uname().sysname
    else:
        return 'Unknown'

def main():
    root = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
    txt_file = 'train.txt'
    file_list = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined/train.txt'
    target_folder = 'C:/Data/BraTS_training_labels/'
    subjects = open(file_list).read().splitlines()
    seg_suffix = '-seg_ce_ud.nii.gz'
    if check_system() == 'Windows':
        names = [sub.split('//')[-1] for sub in subjects]
    else:
        names = [sub.split('/')[-1] for sub in subjects]
    paths = [os.path.join(root, sub, name + '_') for sub, name in zip(subjects, names)]
    for sub, name in zip(subjects, names):
        print(sub, name)
        path = os.path.join(root, sub, name + seg_suffix)
        target_seg_name = target_folder + name + seg_suffix
        shutil.copy2(path, target_seg_name)
    #
    # label_path = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
    # label_suffix = '-label.nii.gz'
    # input_suffix = '.nii.gz'
    # label_names = glob.glob(label_path)
    # new_folder = 'C:/Data/UKER_BM/'
    # for name in label_names:
    #     patient_name = os.path.basename(name)
    #     patient_ID = patient_name[:-13]
    #     input_name = name.replace(label_suffix, input_suffix)
    #     input_patient_name = patient_name.replace(label_suffix, input_suffix)
    #     target_label_name = new_folder + patient_ID + "/" + patient_name
    #     target_input_name = new_folder + patient_ID + "/" + input_patient_name
    #     # print(target_input_name)
    #     # print(input_patient_name)
    #     target_folder = new_folder + patient_ID
    #     if not os.path.exists(target_folder):
    #         os.makedirs(target_folder)
    #     shutil.copy2(name, target_label_name)
    #     shutil.copy2(input_name, target_input_name)


if __name__ == '__main__':
    main()

