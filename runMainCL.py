import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"


### BRATS dataset

cmd2 = 'py  train.py --gpu 0  --cfg deepmedic_CL_2_UKER'
cmd3 = 'py  train.py --gpu 0  --cfg deepmedic_CL_3_BraTS'
cmd4 = 'py  train.py --gpu 0  --cfg deepmedic_CL_4_NYU'
cmd5 = 'py  train.py --gpu 0  --cfg deepmedic_CL_5_Stanford'

cmd12 = 'py  predict.py --gpu 0  --cfg deepmedic_CL_2_UKER'
cmd13 = 'py  predict.py --gpu 0  --cfg deepmedic_CL_3_BraTS'
cmd14 = 'py  predict.py --gpu 0  --cfg deepmedic_CL_4_NYU'
cmd15 = 'py  predict.py --gpu 0  --cfg deepmedic_CL_5_Stanford'

cmds = [cmd2, cmd3, cmd4, cmd5, cmd12, cmd13, cmd14, cmd15]
for cmd in cmds:
    os.system(cmd)