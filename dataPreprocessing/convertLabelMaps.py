import nibabel as nib
import glob
import os
import numpy as np


def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def main():
    # search = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
    search = 'C:/Data/NYU_Release2'
    directories = get_directories(search)
    total_num = len(directories)
    new_suffix = '-seg.nii.gz'
    norm_suffix = '-seg_ce.nii.gz'
    for i in range(0, total_num):

        subfolder = directories[i]
        file_name = os.path.join(search, subfolder, subfolder + new_suffix)
        proxy = nib.load(file_name)
        mri_data = proxy.get_fdata()
        aff = proxy.affine
        mri_data = np.where((mri_data == 3) | (mri_data == 1), 1, 0)
        img_nifti = nib.Nifti1Image(mri_data, aff)
        save_name = os.path.join(search, subfolder, subfolder + norm_suffix)
        nib.save(img_nifti, save_name)
        print(i)


if __name__ == "__main__":
    main()