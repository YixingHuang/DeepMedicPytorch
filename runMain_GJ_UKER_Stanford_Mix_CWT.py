import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd100 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_mix'
cmd101 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd102 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd103 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_mix2'
cmd104 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd105 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd106 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_mix3'
cmd107 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd108 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd109 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_mix4'
cmd110 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd111 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd112 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_mix5'
cmd113 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd114 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_mix5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


# The CWT config files, which was not provided.
cmd200 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER2_r2'
cmd201 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford2_r2'
cmd202 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER3_r2'
cmd203 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford3_r2'
cmd204 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER4_r2'
cmd205 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r2'
cmd206 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd207 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd300 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER2_r3'
cmd301 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford2_r3'
cmd302 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER3_r3'
cmd303 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford3_r3'
cmd304 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER4_r3'
cmd305 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r3'
cmd306 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd307 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd400 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER2_r4'
cmd401 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford2_r4'
cmd402 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER3_r4'
cmd403 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford3_r4'
cmd404 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER4_r4'
cmd405 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r4'
cmd406 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd407 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd500 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER2_r5'
cmd501 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford2_r5'
cmd502 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER3_r5'
cmd503 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford3_r5'
cmd504 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_UKER4_r5'
cmd505 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r5'
cmd506 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd507 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF_Stanford4_r5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmds = [cmd200, cmd201, cmd202, cmd203, cmd204, cmd205, cmd206, cmd207,
        cmd300, cmd301, cmd302, cmd303, cmd304, cmd305, cmd306, cmd307,
        cmd400, cmd401, cmd402, cmd403, cmd404, cmd405, cmd406, cmd407,
        cmd500, cmd501, cmd502, cmd503, cmd504, cmd505, cmd506, cmd507,
        ]
for cmd in cmds:
    os.system(cmd)