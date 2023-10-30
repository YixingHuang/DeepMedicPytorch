import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


def main():

    search = 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TEST_resample'
    # search = '/mnt/data/zahra/data/test'
    directories = get_directories(search)
    total_num = len(directories)

    # for i in range(44, 70):
    for i in range(0, 1):
        # subfolder = directories[i]
        subfolder = 'BraTS-MET-00692-000'
        print(subfolder)
        input_file = os.path.join(search, subfolder, subfolder + '-t1c_bias_norm.nii.gz')
        cmd = 'pyl createBrainParcellation.py -i ' + input_file +' -o C:/MachineLearning/DeepMedicPytorch/BrainParcellation/HarvardOxford-sub/UCSF_test -n ' + subfolder
        os.system(cmd)


if __name__ == "__main__":
    main()
