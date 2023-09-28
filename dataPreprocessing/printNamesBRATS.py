import glob
import os

def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


# search = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
search = 'C:/Data/NYU_Release2'
directories = get_directories(search)
for name in directories:
    print(name)
