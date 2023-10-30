import tensorflow as tf
from tensorflow.python.training import py_checkpoint_reader
import numpy as np
import os
import configparser
# from numba import cuda
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


total_num_iters = 6
total_num_centers = 5
num_epochs_per_center = 10
runModel = 'py deepMedicRun -model ./examples/configFiles/deepMedicBM/model/modelConfig_wide1_deeper.cfg '
config_file_name = './experiments/deepmedic_CWT_general.yaml'
center_IDs = ['UKER', 'UCSF', 'Stanford', 'BraTS', 'NYU']

train_data_dir = {'NYU': 'C:/Data/NYU_Release2',
                  'UKER': 'C:/Data/UKER_BM_Channel1',
                  'Stanford': 'C:/Data/StanfordMetShare',
                  'UCSF': 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TRAIN_resample',
                  'BraTS': 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
                  }
test_data_dir = {'NYU': 'C:/Data/NYU_Release2',
                  'UKER': 'C:/Data/UKER_BM_Channel1',
                  'Stanford': 'C:/Data/StanfordMetShare',
                  'UCSF': 'C:/Data/UCSF_BrainMetastases_v1.2/UCSF_BM_TEST_resample',
                  'BraTS': 'C:/Data/ASNR-MICCAI-BraTS2023-MET-Challenge-TrainingData_combined'
                  }

train_cmd = 'py  train.py --gpu 0  --cfg deepmedic_CWT_general'
test_cmd = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general --ckpt model_last.tar --folder '

assert total_num_centers == len(center_IDs), 'the number of centers must be equal to the number of center_IDs'

state_dict = {}
var_dict = {}

config = configparser.ConfigParser()  # open a new cfg parser to avoid memories from the previous cfg
config.optionxform = str
# config_test.read(test_config_name)
fp = open(config_file_name)
newstring = '[default]\n' + fp.read()  # insert a section name
config.read_string(newstring)
fp.close()

session_name = 'CWT_LWF'
main_model_folder = 'C:/MachineLearning/DeepMedicPytorch/CWT_models/'
for iter in range(0, total_num_iters):
    for center_idx in range(0, total_num_centers):

        # the situation that center_idx = 0
        pre_center_name = center_IDs[(center_idx + total_num_centers - 1) % total_num_centers]
        pre_model_iter = iter if center_idx > 0 else iter - 1
        current_center_name = center_IDs[center_idx]
        print('HYX: currently running iteration ' + str(iter) + ' center ' + center_IDs[center_idx]
              + "pre_model_iter " + str(pre_model_iter))
        model_session_name = current_center_name + '_' + session_name + '_' + str(iter) + '_' \
                             + str(num_epochs_per_center)
        model_pre_session_name = pre_center_name + '_' + session_name + '_' + str(pre_model_iter) + '_' + str(
            num_epochs_per_center)

        train_model_folder = main_model_folder + model_session_name
        config.set('default', option='train_dir', value='None')
        config.set('default', option='data_dir', value=train_data_dir[current_center_name])
        config.set('default', option='test_data_dir', value=test_data_dir[current_center_name])
        config.set('default', option='num_epochs', value=str(num_epochs_per_center))
        if iter == 0 and center_idx == 0:
            config.set('default', option='resume', value='None')
        else:
            resume_path = main_model_folder + model_pre_session_name + '/model_last.tar'
            print(resume_path)
            if os.path.isfile(resume_path):
                config.set('default', option='resume', value=resume_path)
            else:
                print("=> no checkpoint found at '{}'".format(resume_path))

        configfile = open(config_file_name, 'w')
        config.write(configfile)
        configfile.close()
        x = open(config_file_name)
        newstring = x.read().replace('[default]', '')
        x.close()
        configfile = open(config_file_name, 'w')
        configfile.write(newstring)
        configfile.close()

        os.system(train_cmd)

