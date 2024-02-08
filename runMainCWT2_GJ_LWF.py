import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


cmd1 = 'py  train.py --gpu 0  --cfg GJ_CWT2_1_UKER'

cmd2 = 'py  train.py --gpu 0  --cfg GJ_CWT2_2_Stanford_LWF'

cmd3 = 'py  train.py --gpu 0  --cfg GJ_CWT2_3_BraTS_LWF'

cmd4 = 'py  train.py --gpu 0  --cfg GJ_CWT2_4_UKER_LWF'

cmd5 = 'py  train.py --gpu 0  --cfg GJ_CWT2_5_Stanford_LWF'

cmd6 = 'py  train.py --gpu 0  --cfg GJ_CWT2_6_BraTS_LWF'

cmd7 = 'py  train.py --gpu 0  --cfg GJ_CWT2_7_UKER_LWF'

cmd8 = 'py  train.py --gpu 0  --cfg GJ_CWT2_8_Stanford_LWF'

cmd9 = 'py  train.py --gpu 0  --cfg GJ_CWT2_9_BraTS_LWF'

cmd10 = 'py  train.py --gpu 0  --cfg GJ_CWT2_10_UKER_LWF'

cmd11 = 'py  train.py --gpu 0  --cfg GJ_CWT2_11_Stanford_LWF'

cmd12 = 'py  train.py --gpu 0  --cfg GJ_CWT2_12_BraTS_LWF'

cmd13 = 'py  train.py --gpu 0  --cfg GJ_CWT2_13_UKER_LWF'

cmd14 = 'py  train.py --gpu 0  --cfg GJ_CWT2_14_Stanford_LWF'

cmd15 = 'py  train.py --gpu 0  --cfg GJ_CWT2_15_BraTS_LWF'

cmd16 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd17 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS_LWF --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd18 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS_LWF --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'

cmd19 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_13_UKER_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd20 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_14_Stanford_LWF --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmds = [cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14, cmd15, cmd16, cmd17, cmd18, cmd19, cmd20]
for cmd in cmds:
    os.system(cmd)
