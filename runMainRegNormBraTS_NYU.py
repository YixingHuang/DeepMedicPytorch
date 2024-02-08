import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


cmd503 = 'py  train.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_TL'
cmd504 = 'py  predict.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_TL --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd505 = 'py  predict.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_TL --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd513 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL2'
cmd514 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd515 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL2 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd523 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL3'
cmd524 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd525 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL3 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd533 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL4'
cmd534 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd535 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL4 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd543 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL5'
cmd544 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd545 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_TL5 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd550 = 'py  train_LWF.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_LWF'
cmd551 = 'py  predict.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_LWF --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd552 = 'py  predict.py --gpu 0  --cfg NO_BraTS_regnorm_NYU_LWF --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'

cmd553 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF2'
cmd554 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd555 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF2 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd556 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF3'
cmd557 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd558 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF3 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd559 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF4'
cmd560 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd561 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF4 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd562 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF5'
cmd563 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd564 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_NYU_LWF5 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd600 = 'py  train.py --gpu 0  --cfg NO_NYU_regnorm'
cmd601 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd602 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd610 = 'py  train.py --gpu 0  --cfg NO_NYU_regnorm2'
cmd611 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd612 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm2 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd620 = 'py  train.py --gpu 0  --cfg NO_NYU_regnorm3'
cmd621 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd622 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm3 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd630 = 'py  train.py --gpu 0  --cfg NO_NYU_regnorm4'
cmd631 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd632 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm4 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmd640 = 'py  train.py --gpu 0  --cfg NO_NYU_regnorm5'
cmd641 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd642 = 'py  predict.py --gpu 0  --cfg NO_NYU_regnorm5 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'


cmds = [cmd550, cmd551, cmd552]
for cmd in cmds:
    os.system(cmd)
