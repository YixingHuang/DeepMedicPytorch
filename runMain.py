import os

cmd0 = 'py  prepBM.py'
cmd1 = 'py  train.py --gpu 1  --cfg deepmedic_ce'

cmds = [cmd1]
for cmd in cmds:
    os.system(cmd)