import nibabel as nib
import glob
import os
import numpy as np
from scipy.ndimage import affine_transform

def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


def resample(nii_path, seg_path, save_seg_path, seg_ref_name, seg_ref_name_new):

    img = nib.load(nii_path)
    data = img.get_fdata()

    seg = nib.load(seg_path)
    seg_data = seg.get_fdata()

    mask = np.where(data > 0, 1.0, 0)
    seg_data = np.multiply(seg_data, mask)

    resampled_seg = nib.Nifti1Image(seg_data, img.affine)

    # Save the resampled NIfTI image
    resampled_seg.to_filename(save_seg_path)

    # gt = nib.load(seg_ref_name)
    # gt.to_filename(seg_ref_name_new)


def main():
    search = '/mnt/data/zahra/data/test'
    target = '/mnt/data/zahra/DeepMedicPytorch/output/deepmedic_vss_Zurich_Precision_LWF/test_200'

    directories = get_directories(search)
    total_num = len(directories)

    new_suffix = 'normalized.nii.gz'
    norm_suffix = 'normalized.nii.gz'
    seg_suffix = 'segment.nii.gz'
    new_seg_suffix = 'segment.nii.gz'

    for i in range(0, total_num):
        subfolder = directories[i]
        file_name = os.path.join(search, subfolder, new_suffix)
        seg_name = os.path.join(search, subfolder, seg_suffix)
        prediction_name = os.path.join(target, subfolder + '_Segm.nii.gz')
        prediction_name_new = os.path.join(target, subfolder + '_Segm2.nii.gz')
        seg_name_new = os.path.join(target, subfolder + '_SegGT.nii.gz')

        resample(file_name, prediction_name, prediction_name_new, seg_name, seg_name_new)
        print(i)


if __name__ == "__main__":
    main()
