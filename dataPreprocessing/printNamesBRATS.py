import glob
import os
import random
def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


# search = 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
# search = 'C:/Data/NYU_Release2'
# search ='C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BrainMetastases_TRAIN'
# search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BraTS-METS/UCSF_BraTS-METS_metsSRI'
# search = 'C:/Data/StanfordMetShare'
# search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TRAIN_resample'
search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TEST_resample'
directories = get_directories(search)
random.shuffle(directories)
for name in directories:
    print(name)
