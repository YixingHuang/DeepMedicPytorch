import os
import configparser

os.environ['CUDA_VISIBLE_DEVICES'] = "1"

session_name = 'SWT_LWF_UKERlast'
total_num_iters = 1
total_num_centers = 5
num_epochs_per_center = 300
episode = 'deepmedic_CWT_general_LWF'
config_file_name = './experiments/' + episode + '.yaml'
# center_IDs = ['UKER', 'UCSF', 'Stanford', 'BraTS', 'NYU'] #
center_IDs = ['UCSF', 'Stanford', 'BraTS', 'NYU', 'UKER']

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

test_data_list= {'NYU': 'testNYU.txt',
                  'UKER': 'testUKER.txt',
                  'Stanford': 'testStanford.txt',
                  'UCSF': 'testUCSF.txt',
                  'BraTS': 'testBraTS.txt'
                  }

train_cmd = 'py  train_LWF.py --gpu 0  --cfg ' + episode
test_cmd_partial = 'py  predict.py --gpu 0  --cfg ' + episode + ' --ckpt model_last.tar '

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


main_model_folder = 'C:/MachineLearning/DeepMedicPytorch/' + session_name + '_models/'
# initial_model = 'C:/MachineLearning/DeepMedicPytorch/Yixing/BM_train_ckpts/deepmedic_jvssPr_BM/model_last.tar'
initial_model = 'C:/MachineLearning/DeepMedicPytorch/Yixing/BM_shuffle_ckpts_UCSF/deepmedic_vss_UCSF_Precision/model_best.tar'
for iter in range(0, total_num_iters):
    for center_idx in range(0, total_num_centers):
        #Training
        if iter == 0 and (center_idx == 0):
            continue
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
        config.set('default', option='train_dir', value=train_model_folder)
        config.set('default', option='data_dir', value=train_data_dir[current_center_name])
        config.set('default', option='test_data_dir', value=test_data_dir[current_center_name])
        config.set('default', option='num_epochs', value=str(num_epochs_per_center))
        if center_IDs[center_idx] == 'NYU':
            config.set('default', option='num_patches', value='10')
        else:
            config.set('default', option='num_patches', value='20')
        if iter == 0 and center_idx == 1:
            config.set('default', option='resume', value=initial_model)
            print(initial_model)
        else:
            resume_path = main_model_folder + model_pre_session_name + '/' + episode + '/model_last.tar'
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
        newstring = newstring.replace(' =', ':')
        newstring = newstring.replace('\t', ' ')
        x.close()
        configfile = open(config_file_name, 'w')
        configfile.write(newstring)
        configfile.close()

        os.system(train_cmd)


        #Test
        config.set('default', option='data_dir', value='C:/Data')
        config.set('default', option='test_data_dir', value='C:/Data')
        configfile = open(config_file_name, 'w')
        config.write(configfile)
        configfile.close()
        x = open(config_file_name)
        newstring = x.read().replace('[default]', '')
        newstring = newstring.replace(' =', ':')
        newstring = newstring.replace('\t', ' ')
        x.close()
        configfile = open(config_file_name, 'w')
        configfile.write(newstring)
        configfile.close()
        for test_center_idx in range(0, total_num_centers):
            test_cmd = test_cmd_partial + '--folder test' + center_IDs[center_idx] + 'Model' \
                       + center_IDs[test_center_idx] + '_' + session_name + '_iter' + str(iter) + ' --valid_list ' + test_data_list[center_IDs[test_center_idx]]
            os.system(test_cmd)







