import nibabel as nib
import glob
import os
import numpy as np


def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def main():
    # search = 'C:/Data/NYU_Release2'
    # search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BrainMetastases_TRAIN'
    search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BraTS-METS/UCSF_BraTS-METS_metsSRI'
    directories = get_directories(search)
    total_num = len(directories)
    # new_suffix = '-t1c_bias_norm.nii.gz'
    # norm_suffix = '-t1c_bias_norm_ud.nii.gz'
    new_suffix = '-seg_ce.nii.gz'
    norm_suffix = '-seg_ce_ud.nii.gz'
    for i in range(0, total_num):

        subfolder = directories[i]
        file_name = os.path.join(search, subfolder, subfolder + new_suffix)
        proxy = nib.load(file_name)

        mri_data = proxy.get_fdata()[:, ::-1, :]
        aff = proxy.affine
        img_nifti = nib.Nifti1Image(mri_data, aff)
        save_name = os.path.join(search, subfolder, subfolder + norm_suffix)
        nib.save(img_nifti, save_name)
        print(i)


if __name__ == "__main__":
    main()