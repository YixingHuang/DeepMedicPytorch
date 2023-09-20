import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd0 = 'py  prepBM.py'
cmd1 = 'py  train.py --gpu 0  --cfg deepmedic_ce_BM'
cmd2 = 'py  train.py --gpu 0  --cfg deepmedic_ce'
cmd3 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM'
cmd4 = 'py  train.py --gpu 0  --cfg deepmedic_ce_BM4'
cmd5 = 'py  predict.py --gpu 0  --cfg deepmedic_ce_BM4'
cmds = [cmd1]
for cmd in cmds:
    os.system(cmd)