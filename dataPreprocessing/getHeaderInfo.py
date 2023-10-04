import nibabel as nib

file_name = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BrainMetastases_TRAIN/100113A/100113A_T1post.nii.gz'
proxy = nib.load(file_name)
print(proxy.header)
print(proxy.affine)