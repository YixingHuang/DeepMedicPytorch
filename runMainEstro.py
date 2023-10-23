import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

## UKER  dataset

cmd0 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL'

cmd1 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL'

cmd2 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF'

cmd3 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF'

cmd4 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF2'

cmd5 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF2 -ckpt model_last.tar'

cmd6 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3'

cmd7 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 -ckpt model_last.tar'

cmd100 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF4'

cmd101 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF4 -ckpt model_last.tar'

cmd102 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF5'

cmd103 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF5 -ckpt model_last.tar'

cmd104 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF6'

cmd105 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF6 -ckpt model_last.tar'


cmd106 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF7'

cmd107 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF7 -ckpt model_last.tar -folder test50'

cmd113 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 -ckpt model_epoch_49.tar -folder test50'

cmd114 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF4 -ckpt model_epoch_49.tar -folder test50'

cmd115 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF5 -ckpt model_epoch_49.tar -folder test50'

cmd116 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF6 -ckpt model_epoch_49.tar -folder test50'

cmd117 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF7 -ckpt model_epoch_49.tar -folder test50'


cmd10 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL'

cmd11 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL'

cmd12 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF'

cmd13 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF'


cmd20 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_NYU_TL'

cmd21 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_NYU_TL'

cmd22 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_NYU_LWF'

cmd23 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_NYU_LWF'


cmd30 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UCSF_TL'

cmd31 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UCSF_TL'

cmd32 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_UCSF_LWF'

cmd33 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UCSF_LWF'


cmd200 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF2'
cmd201 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF2 -ckpt model_epoch_37.tar -folder test50'
cmd202 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF2'

cmd203 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF3'
cmd204 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF3 -ckpt model_epoch_37.tar -folder test50'
cmd205 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF3'

cmd206 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF4'
cmd207 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF4 -ckpt model_epoch_37.tar -folder test50'
cmd208 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF4'

cmd209 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF5'
cmd210 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF5 -ckpt model_epoch_37.tar -folder test50'
cmd211 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF5'

cmd212 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF6'
cmd213 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF6 -ckpt model_epoch_37.tar -folder test50'
cmd214 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF6'


cmd220 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF2 -folder testUKER'
cmd221 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF3 -folder testUKER'
cmd222 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF4 -folder testUKER'
cmd223 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF5 -folder testUKER'
cmd224 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_LWF6 -folder testUKER'


cmd225 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 -folder testUKER'
cmd226 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF4 -folder testUKER'
cmd227 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF5 -folder testUKER'
cmd228 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF6 -folder testUKER'
cmd229 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF7 -folder testUKER'


cmd230 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL3'
cmd231 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL3 -folder testUKER'
cmd232 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL4'
cmd233 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL4 -folder testUKER'

cmd234 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL3'
cmd235 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_TL4'


cmd300 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation'
cmd301 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation -ckpt model_last.tar -folder testLast'
cmd302 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation2'
cmd303 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation2 -ckpt model_last.tar -folder testLast'

cmd304 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation -ckpt model_epoch_150.tar -folder test150'
cmd305 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_parcellation2 -ckpt model_epoch_150.tar -folder test150'

cmd306 = 'py  train_LWF.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL3'
cmd307 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL3 -ckpt model_epoch_37.tar -folder test50UKER'
cmd308 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL3 -folder testUKER'
cmd309 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_Stanford_TL3 -folder test'

cmd400 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat1'
cmd401 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat1'
cmd402 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat2'
cmd403 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat2'
cmd404 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat3'
cmd405 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat3'
cmd406 = 'py  train.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat4'
cmd407 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_UKER_repeat4'



cmd450 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Zurich_Precision_LWF -ckpt model_epoch_150.tar -folder test150'
cmd451 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Zurich_Precision_TL -ckpt model_last.tar -folder testLast'
cmd452 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Zurich_Precision_TL -ckpt model_epoch_150.tar -folder test150'


cmd460 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssPr_BM -ckpt model_last.tar -folder testLastBraTS'
# cmds = [cmd10, cmd11, cmd12, cmd13, cmd20, cmd21, cmd22, cmd23, cmd30, cmd31, cmd32, cmd33]
# cmds = [cmd2, cmd3, cmd12, cmd13]
# cmds = [cmd100, cmd101, cmd102, cmd103, cmd104, cmd105, cmd106, cmd107]
# cmds = [cmd113, cmd114, cmd115, cmd116, cmd117]
# cmds = [cmd201, cmd202, cmd203, cmd204, cmd205, cmd206, cmd207, cmd208, cmd209, cmd210, cmd211, cmd212, cmd213, cmd214]
# cmds = [cmd220, cmd221, cmd222, cmd223, cmd224, cmd225, cmd226, cmd227, cmd228, cmd229]
# cmds = [cmd230, cmd231, cmd232, cmd233]
# cmds = [cmd300, cmd301, cmd302, cmd303]
# cmds = [cmd304, cmd305]
# cmds = [cmd309]
# cmds = [cmd400, cmd401, cmd402, cmd403, cmd404, cmd405, cmd406, cmd407]
# cmds = [cmd450, cmd451, cmd452]
cmds = [cmd460]
for cmd in cmds:
    os.system(cmd)