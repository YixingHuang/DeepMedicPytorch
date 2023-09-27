import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd0 = 'py  prepBM.py'
cmd1 = 'py  train.py --gpu 0  --cfg deepmedic_ce_BM'
cmd2 = 'py  train.py --gpu 0  --cfg deepmedic_ce'
cmd3 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM'
cmd4 = 'py  train.py --gpu 0  --cfg deepmedic_ce_BM4'
cmd5 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM4'
cmd6 = 'py  train.py --gpu 0  --cfg deepmedic_ce_BM2'
cmd7 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM2'
cmd8 = 'py  train.py --gpu 0  --cfg deepmedic_vss_BM'
cmd9 = 'py  train.py --gpu 0  --cfg deepmedic_jvssS_BM'
cmd10 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM'
cmd11 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BM'
cmd12 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssS_BM'
cmd13 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM --ckpt model_epoch_209.tar'
cmd14 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BM --ckpt model_epoch_248.tar'
cmd15 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssS_BM --ckpt model_epoch_243.tar'

cmd16 = 'py  train.py --gpu 0  --cfg deepmedic_jvssPr_BM'
cmd17 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssPr_BM'
cmd18 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssPr_BM --ckpt model_last.tar  --folder test_last'

cmd20 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM --ckpt model_last.tar  --folder test_last'
cmd21 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BM --ckpt model_last.tar  --folder test_last'
cmd22 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssS_BM --ckpt model_last.tar  --folder test_last'
cmds = [cmd20, cmd21, cmd22]
for cmd in cmds:
    os.system(cmd)