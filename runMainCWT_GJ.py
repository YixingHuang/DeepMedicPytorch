import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


cmd1 = 'py  train.py --gpu 0  --cfg GJ_CWT_1_UKER'

cmd2 = 'py  train.py --gpu 0  --cfg GJ_CWT_2_UCSF'

cmd3 = 'py  train.py --gpu 0  --cfg GJ_CWT_3_Stanford'

cmd4 = 'py  train.py --gpu 0  --cfg GJ_CWT_4_UKER'

cmd5 = 'py  train.py --gpu 0  --cfg GJ_CWT_5_UCSF'

cmd6 = 'py  train.py --gpu 0  --cfg GJ_CWT_6_Stanford'

cmd7 = 'py  train.py --gpu 0  --cfg GJ_CWT_7_UKER'

cmd8 = 'py  train.py --gpu 0  --cfg GJ_CWT_8_UCSF'

cmd9 = 'py  train.py --gpu 0  --cfg GJ_CWT_9_Stanford'

cmd10 = 'py  train.py --gpu 0  --cfg GJ_CWT_10_UKER'

cmd11 = 'py  train.py --gpu 0  --cfg GJ_CWT_11_UCSF'

cmd12 = 'py  train.py --gpu 0  --cfg GJ_CWT_12_Stanford'

cmd13 = 'py  train.py --gpu 0  --cfg GJ_CWT_13_UKER'

cmd14 = 'py  train.py --gpu 0  --cfg GJ_CWT_14_UCSF'

cmd15 = 'py  train.py --gpu 0  --cfg GJ_CWT_15_Stanford'

cmd16 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd17 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd18 = 'py  predict.py --gpu 0  --cfg GJ_CWT_15_Stanford --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd19 = 'py  predict.py --gpu 0  --cfg GJ_CWT_13_UKER --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd20 = 'py  predict.py --gpu 0  --cfg GJ_CWT_14_UCSF --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

#UCSF only
cmd21 = 'py  train.py --gpu 0  --cfg GJ_UCSF_independent'
cmd22 = 'py  predict.py --gpu 0  --cfg GJ_UCSF_independent --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd23 = 'py  train_LWF.py --gpu 0  --cfg GJ_UCSF_LWF2'
cmd24 = 'py  predict.py --gpu 0  --cfg GJ_UCSF_LWF2 --ckpt model_last.tar --folder testUCSF --valid_list testSwap.txt'
# cmds = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9, cmd10, cmd11, cmd12, cmd13, cmd14, cmd15, cmd16, cmd17, cmd18, cmd19, cmd20]


cmd101 = 'py  train.py --gpu 0  --cfg GJ_CWT2_1_UKER'

cmd102 = 'py  train.py --gpu 0  --cfg GJ_CWT2_2_Stanford'

cmd103 = 'py  train.py --gpu 0  --cfg GJ_CWT2_3_BraTS'

cmd104 = 'py  train.py --gpu 0  --cfg GJ_CWT2_4_UKER'

cmd105 = 'py  train.py --gpu 0  --cfg GJ_CWT2_5_Stanford'

cmd106 = 'py  train.py --gpu 0  --cfg GJ_CWT2_6_BraTS'

cmd107 = 'py  train.py --gpu 0  --cfg GJ_CWT2_7_UKER'

cmd108 = 'py  train.py --gpu 0  --cfg GJ_CWT2_8_Stanford'

cmd109 = 'py  train.py --gpu 0  --cfg GJ_CWT2_9_BraTS'

cmd110 = 'py  train.py --gpu 0  --cfg GJ_CWT2_10_UKER'

cmd111 = 'py  train.py --gpu 0  --cfg GJ_CWT2_11_Stanford'

cmd112 = 'py  train.py --gpu 0  --cfg GJ_CWT2_12_BraTS'

cmd113 = 'py  train.py --gpu 0  --cfg GJ_CWT2_13_UKER'

cmd114 = 'py  train.py --gpu 0  --cfg GJ_CWT2_14_Stanford'

cmd115 = 'py  train.py --gpu 0  --cfg GJ_CWT2_15_BraTS'

cmd116 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd117 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd118 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_15_BraTS --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd119 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_13_UKER --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd120 = 'py  predict.py --gpu 0  --cfg GJ_CWT2_14_Stanford --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd121 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd122 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd123 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
# cmds = [cmd24]
# cmds = [cmd101, cmd102, cmd103, cmd104, cmd105, cmd106, cmd107, cmd108, cmd109, cmd110, cmd111, cmd112, cmd113, cmd114, cmd115, cmd116, cmd117, cmd118, cmd119, cmd120]
cmds = [cmd121, cmd122, cmd123]
for cmd in cmds:
    os.system(cmd)
