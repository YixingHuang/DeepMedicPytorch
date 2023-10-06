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

cmd22 = 'py  train.py --gpu 0  --cfg deepmedic_FT_2_BraTS'
cmd23 = 'py  train.py --gpu 0  --cfg deepmedic_FT_3_NYU'
cmd24 = 'py  train.py --gpu 0  --cfg deepmedic_FT_4_Stanford'
cmd25 = 'py  train.py --gpu 0  --cfg deepmedic_FT_5_UKER'

cmd26 = 'py  predict.py --gpu 0  --cfg deepmedic_FT_2_BraTS'
cmd27 = 'py  predict.py --gpu 0  --cfg deepmedic_FT_3_NYU'
cmd28 = 'py  predict.py --gpu 0  --cfg deepmedic_FT_4_Stanford'
cmd29 = 'py  predict.py --gpu 0  --cfg deepmedic_FT_5_UKER'

centers = ['UCSF', 'UKER', 'Stanford', 'NYU', 'BraTS']
general_cmd = 'py  train.py --gpu 0  --cfg deepmedic_CWT_'
test_cmd = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_'
# cmds = [cmd2, cmd3, cmd4, cmd5, cmd12, cmd13, cmd14, cmd15]
# cmds = [cmd22, cmd23, cmd24, cmd25, cmd26, cmd27, cmd28, cmd29]
# for cmd in cmds:
#     os.system(cmd)

# for idx in range(1, 20):
#     cmd = general_cmd + str(idx + 1) + '_' + centers[idx % 5]
#     print(cmd)
#     os.system(cmd)

# for idx in range(15, 20):
#     cmd = test_cmd + str(idx + 1) + '_' + centers[idx % 5]
#     print(cmd)
#     os.system(cmd)

for idx in range(20, 45):
    if idx >= 40:
        cmd = test_cmd + str(idx - 5 + 1) + '_' + centers[idx % 5]
    else:
        cmd = general_cmd + str(idx + 1) + '_' + centers[idx % 5]

    print(cmd)
    os.system(cmd)


