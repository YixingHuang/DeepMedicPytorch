import nibabel as nib
import glob
import os
import numpy as np
from scipy.ndimage import affine_transform

def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


def resample(nii_path, resampled_nii_path, seg_path, save_seg_path):

    img = nib.load(nii_path)
    data = img.get_fdata()

    seg = nib.load(seg_path)
    seg_data = seg.get_fdata()

    # Define the source and target affine transformations
    src_affine = img.affine
    src_voxel_size = np.abs(np.diag(src_affine))

    # Create a target affine that maintains the rotation of the original affine
    # but has the desired voxel sizes
    rotation_matrix = src_affine[:3, :3] / src_voxel_size[:3, None]
    target_voxel_size = np.array([1, 1, 1])
    target_affine = np.eye(4)
    target_affine[:3, :3] = rotation_matrix * target_voxel_size[:, None]

    # Compute the centers of original and target volumes
    original_center = np.array(data.shape) / 2.0
    resampled_center = np.array([240, 240, 155]) / 2.0

    # Get the translation required to align centers in world coordinates
    original_center_world = np.dot(src_affine, list(original_center) + [1])[:3]
    resampled_center_world = np.dot(target_affine, list(resampled_center) + [1])[:3]
    translation = original_center_world - resampled_center_world

    # Incorporate the translation to the target affine
    target_affine[:3, 3] = translation

    # Calculate the resampling affine matrix
    resampling_affine = np.linalg.inv(src_affine).dot(target_affine)

    # Resample the image using affine transformation
    resampled_data = affine_transform(
        input=data,
        matrix=resampling_affine[:3, :3],  # 3x3 affine transformation
        offset=resampling_affine[:3, 3],  # Translation vector
        output_shape=(240, 240, 155),  # New shape
        order=1  #

    )

    resampled_seg_data = affine_transform(
        input=seg_data,
        matrix=resampling_affine[:3, :3],  # 3x3 affine transformation
        offset=resampling_affine[:3, 3],  # Translation vector
        output_shape=(240, 240, 155),  # New shape
        order=3  # Cubic spline interpolation
    )
    resampled_seg_data = np.where(resampled_seg_data > 0.1, 1, 0)
    # Create a new NIfTI image with the resampled data and target affine
    resampled_img = nib.Nifti1Image(resampled_data, target_affine)

    # Save the resampled NIfTI image
    resampled_img.to_filename(resampled_nii_path)

    resampled_seg = nib.Nifti1Image(resampled_seg_data, target_affine)

    # Save the resampled NIfTI image
    resampled_seg.to_filename(save_seg_path)

def main():
    # search = 'C:/Data/NYU_Release2'
    search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BrainMetastases_TRAIN'
    target = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TRAIN_resample'
    # search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BraTS-METS/UCSF_BraTS-METS_metsSRI'
    directories = get_directories(search)
    total_num = len(directories)
    # new_suffix = '-t1c_bias_norm.nii.gz'
    # norm_suffix = '-t1c_bias_norm_ud.nii.gz'
    new_suffix = '_T1post.nii.gz'
    norm_suffix = '-t1ce.nii.gz'
    seg_suffix = '_seg.nii.gz'
    new_seg_suffix = '-seg.nii.gz'
    for i in range(0, total_num):
        if i == 134: continue
        subfolder = directories[i]
        file_name = os.path.join(search, subfolder, subfolder + new_suffix)
        seg_name = os.path.join(search, subfolder, subfolder + seg_suffix)
        save_folder = os.path.join(target, subfolder)
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        save_name = os.path.join(target, subfolder, subfolder + norm_suffix)
        save_seg_name = os.path.join(target, subfolder, subfolder + new_seg_suffix)
        resample(file_name, save_name, seg_name, save_seg_name)
        print(i)


if __name__ == "__main__":
    main()