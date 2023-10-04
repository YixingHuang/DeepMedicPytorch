import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

## UKER  dataset
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


### BRATS dataset

cmd30 = 'py  train.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision'
cmd31 = 'py  train.py --gpu 0  --cfg deepmedic_vss_BraTS'
cmd32 = 'py  train.py --gpu 0  --cfg deepmedic_vss_BraTS_Sensitivity'

cmd33 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS'
cmd34 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision'
cmd35 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Sensitivity'

cmd36 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS --ckpt model_last.tar  --folder test_last'
cmd37 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision --ckpt model_last.tar  --folder test_last'
cmd38 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Sensitivity --ckpt model_last.tar  --folder test_last'

cmd40 = 'py  train.py --gpu 0  --cfg deepmedic_vss_NYU_Precision'
cmd41 = 'py  train.py --gpu 0  --cfg deepmedic_vss_NYU'
cmd42 = 'py  train.py --gpu 0  --cfg deepmedic_vss_NYU_Sensitivity'

cmd43 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Precision'
cmd44 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU'
cmd45 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Sensitivity'

cmd46 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Precision --ckpt model_last.tar  --folder test_last'
cmd47 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU --ckpt model_last.tar  --folder test_last'
cmd48 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Sensitivity --ckpt model_last.tar  --folder test_last'


cmd50 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF_Precision'
cmd51 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF'
cmd52 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF_Sensitivity'

cmd53 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF_Precision'
cmd54 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF'
cmd55 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF_Sensitivity'


cmd60 = 'py  train.py --gpu 0  --cfg deepmedic_vss_Stanford_Precision'
cmd61 = 'py  train.py --gpu 0  --cfg deepmedic_vss_Stanford'
cmd62 = 'py  train.py --gpu 0  --cfg deepmedic_vss_Stanford_Sensitivity'

cmd63 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Stanford_Precision'
cmd64 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Stanford'
cmd65 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Stanford_Sensitivity'
# cmds = [cmd30, cmd31, cmd32, cmd33, cmd34, cmd35, cmd36, cmd37, cmd38]
# cmds = [cmd32, cmd33, cmd34, cmd35, cmd36, cmd37, cmd38, cmd40, cmd41, cmd42, cmd43, cmd44, cmd45, cmd46, cmd47, cmd48]
# cmds = [cmd40, cmd41, cmd42, cmd43, cmd44, cmd45, cmd46, cmd47, cmd48]
cmds = [cmd53, cmd54, cmd55]
# cmds = [cmd60, cmd61, cmd62, cmd63, cmd64, cmd65]
for cmd in cmds:
    os.system(cmd)