import os
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

def get_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories


def main():

    search = '/mnt/data/zahra/data/train'
    # search = '/mnt/data/zahra/data/test'
    directories = get_directories(search)
    total_num = len(directories)

    for i in range(100, 130):
        subfolder = directories[i]
        print(subfolder)
        input_file = os.path.join(search, subfolder, 'normalizedUKER.nii.gz')
        cmd = 'python createBrainParcellation.py -i ' + input_file +' -o /mnt/data/zahra/DeepMedicPytorch/BrainParcellation/HarvardOxford-sub/training -n ' + subfolder
        os.system(cmd)


if __name__ == "__main__":
    main()
