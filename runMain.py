import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

## UKER  dataset

cmd0 = 'py  prep.py'
cmd1 = 'py  train.py --gpu 0  --cfg deepmedic_ce'
cmd2 = 'py  predict.py --gpu 0  --cfg deepmedic_ce'
cmds =[cmd1, cmd2]
for cmd in cmds:
    os.system(cmd)