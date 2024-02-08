import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


cmd1 = 'py  train.py --gpu 0  --cfg GJ_CWT_1_UKER'

cmd2 = 'py  train.py --gpu 0  --cfg GJ_CWT_2_UCSF_LWF'

cmd3 = 'py  train.py --gpu 0  --cfg GJ_CWT_3_Stanford_LWF'

cmd4 = 'py  train.py --gpu 0  --cfg GJ_CWT_4_UKER_LWF'

cmd5 = 'py  train.py --gpu 0  --cfg GJ_CWT_5_UCSF_LWF'

cmd6 = 'py  train.py --gpu 0  --cfg GJ_CWT_6_Stanford_LWF'

cmd7 = 'py  train.py --gpu 0  --cfg GJ_CWT_7_UKER_LWF'

cmd8 = 'py  train.py --gpu 0  --cfg GJ_CWT_8_UCSF_LWF'

cmd9 = 'py  train.py --gpu 0  --cfg GJ_CWT_9_Stanford_LWF'

cmd10 = 'py  train.py --gpu 0  --cfg GJ_CWT_10_UKER_LWF'

cmd11 = 'py  train.py --gpu 0  --cfg GJ_CWT_11_UCSF_LWF'

cmd12 = 'py  train.py --gpu 0  --cfg GJ_CWT_12_Stanford_LWF'

cmd13 = 'py  train.py --gpu 0  --cfg GJ_CWT_13_UKER_LWF'

cmd14 = 'py  train.py --gpu 0  --cfg GJ_CWT_14_UCSF_LWF'

cmd15 = 'py  train.py --gpu 0  --cfg GJ_CWT_15_Stanford_LWF'

cmd16 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd17 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford_LWF --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd18 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford_LWF --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd19 = 'py  predict.py --gpu 0  --cfg GJ_CWT_13_UKER_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd20 = 'py  predict.py --gpu 0  --cfg GJ_CWT_14_UCSF_LWF --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmds = [cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14, cmd15, cmd16, cmd17, cmd18, cmd19, cmd20]
for cmd in cmds:
    os.system(cmd)
