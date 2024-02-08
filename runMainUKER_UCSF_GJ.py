import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd503 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL'
cmd504 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd505 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'


cmd513 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL2'
cmd514 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL2 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd515 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL2 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'


cmd523 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL3'
cmd524 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL3 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd525 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL3 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'


cmd533 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL4'
cmd534 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL4 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd535 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL4 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'


cmd543 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL5'
cmd544 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL5 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd545 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL5 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'

cmd550 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF'
cmd551 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd552 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'
cmd553 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF2'
cmd554 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF2 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd555 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF2 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'
cmd556 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF3'
cmd557 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF3 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd558 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF3 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'
cmd559 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF4'
cmd560 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF4 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd561 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF4 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'
cmd562 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF5'
cmd563 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF5 --ckpt model_epoch_249.tar --folder testUKER --valid_list testUKER.txt'
cmd564 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF5 --ckpt model_epoch_249.tar --folder testUCSF --valid_list testUCSF.txt'


cmd603 = 'py  train.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL_train50'
cmd604 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL_train50 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd605 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_TL_train50 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd650 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF_train50'
cmd651 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF_train50 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd652 = 'py  predict.py --gpu 0  --cfg GJ_UKER_regnorm_UCSF_LWF_train50 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

# cmds = [cmd503, cmd504, cmd505,
#         cmd513, cmd514, cmd515,
#         cmd523, cmd524, cmd525,
#         cmd533, cmd534, cmd535,
#         cmd543, cmd544, cmd545,
#         cmd550, cmd551, cmd552,
#         cmd553, cmd554, cmd555,
#         cmd556, cmd557, cmd558,
#         cmd559, cmd560, cmd561,
#         cmd562, cmd563, cmd564]
# cmds = [cmd504, cmd505,
#         cmd551, cmd552,
#         cmd514, cmd515,
#         cmd554, cmd555,
#         cmd524, cmd525,
#         cmd557, cmd558,
#         cmd534, cmd535,
#         cmd560, cmd561,
#         cmd544, cmd545,
#         cmd563, cmd564]
# cmds = [cmd603, cmd605, cmd650, cmd652,  ]
# cmds = [cmd603, cmd605, cmd650, cmd652,]
cmds = [cmd605]
for cmd in cmds:
    os.system(cmd)