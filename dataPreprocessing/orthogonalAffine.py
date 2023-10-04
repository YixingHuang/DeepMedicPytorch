import numpy as np
import nibabel as nib
import os
def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    return Q

def changeAffine(input_name, save_name):

    img = nib.load(input_name)
    # Extract the rotation part of the affine matrix
    rotation = img.affine[:3, :3]

    # Orthogonalize the rotation matrix
    orthogonal_rotation = gram_schmidt_columns(rotation)

    # Replace the rotation part of the affine with the orthogonalized matrix
    new_affine = img.affine.copy()
    new_affine[:3, :3] = orthogonal_rotation

    # Create a new NIfTI image with the orthogonalized affine
    new_img = nib.Nifti1Image(img.get_fdata(), new_affine)

    # Save the corrected NIfTI image
    new_img.to_filename(save_name)


def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories



def main():
    # search = 'C:/Data/NYU_Release2'
    search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TRAIN_resample'

    directories = get_directories(search)
    total_num = len(directories)
    # new_suffix = '-t1c_bias_norm.nii.gz'
    # norm_suffix = '-t1c_bias_norm_ud.nii.gz'

    new_suffix = '-t1ce.nii.gz'

    for i in range(0, total_num):

        subfolder = directories[i]
        file_name = os.path.join(search, subfolder, subfolder + new_suffix)
        changeAffine(file_name, file_name)
        print(i)


if __name__ == "__main__":
    main()