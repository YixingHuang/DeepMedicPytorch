import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


cmd503 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_TL'
cmd504 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd505 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd513 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_TL2'
cmd514 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd515 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd523 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_TL3'
cmd524 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd525 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd533 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_TL4'
cmd534 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd535 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd543 = 'py  train.py --gpu 0  --cfg GJ_UKER_Stanford_TL5'
cmd544 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd545 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_TL5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd550 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF'
cmd551 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd552 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd553 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF2'
cmd554 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd555 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd556 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF3'
cmd557 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd558 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd559 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF4'
cmd560 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd561 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd562 = 'py  train_LWF.py --gpu 0  --cfg GJ_UKER_Stanford_LWF5'
cmd563 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd564 = 'py  predict.py --gpu 0  --cfg GJ_UKER_Stanford_LWF5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd600 = 'py  train.py --gpu 0  --cfg GJ_Stanford_independent'
cmd601 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd602 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd610 = 'py  train.py --gpu 0  --cfg GJ_Stanford_independent2'
cmd611 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd612 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd620 = 'py  train.py --gpu 0  --cfg GJ_Stanford_independent3'
cmd621 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd622 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd630 = 'py  train.py --gpu 0  --cfg GJ_Stanford_independent4'
cmd631 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd632 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmd640 = 'py  train.py --gpu 0  --cfg GJ_Stanford_independent5'
cmd641 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd642 = 'py  predict.py --gpu 0  --cfg GJ_Stanford_independent5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd700 = 'py  predict.py --gpu 0  --cfg GJ_UKER_independent --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd701 = 'py  predict.py --gpu 0  --cfg GJ_UKER_independent2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd702 = 'py  predict.py --gpu 0  --cfg GJ_UKER_independent3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd703 = 'py  predict.py --gpu 0  --cfg GJ_UKER_independent4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd704 = 'py  predict.py --gpu 0  --cfg GJ_UKER_independent5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmds = [cmd503, cmd504, cmd505, cmd550, cmd551, cmd552, cmd600, cmd601, cmd602,
        cmd513, cmd514, cmd515, cmd553, cmd554, cmd555, cmd610, cmd611, cmd612,
        cmd523, cmd524, cmd525, cmd556, cmd557, cmd558, cmd620, cmd621, cmd622,
        cmd533, cmd534, cmd535, cmd559, cmd560, cmd561, cmd630, cmd631, cmd632,
        cmd543, cmd544, cmd545, cmd562, cmd563, cmd564, cmd640, cmd641, cmd642,
        cmd700, cmd701, cmd702, cmd703, cmd704,
        ]

for cmd in cmds:
    os.system(cmd)
