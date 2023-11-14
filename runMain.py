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


cmd100 = 'py  train.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision2'
cmd101 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision2'
cmd102 = 'py  train.py --gpu 0  --cfg deepmedic_vss_NYU_Precision2'
cmd103 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Precision2'


cmd200 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_36_UCSF --ckpt model_last.tar'
cmd201 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_37_UKER --ckpt model_last.tar'
cmd202 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_38_Stanford --ckpt model_last.tar'
cmd203 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_39_NYU --ckpt model_last.tar'
cmd204 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_40_BraTS --ckpt model_last.tar'

cmd300 = 'py  train.py --gpu 0  --cfg deepmedic_NO_All5Centers'
cmd301 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar'
cmd302 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar --valid_list testBraTS.txt  --folder testBraTS'
cmd303 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar --valid_list testUCSF.txt  --folder testUCSF'
cmd304 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar --valid_list testNYU.txt  --folder testNYU'
cmd305 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar --valid_list testUKER.txt  --folder testUKER'
cmd306 = 'py  predict.py --gpu 0  --cfg deepmedic_NO_All5Centers  --ckpt model_last.tar --valid_list testStanford.txt  --folder testStanford'

cmd312 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testBraTS.txt  --folder testBraTS'
cmd313 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testUCSF.txt  --folder testUCSF'
cmd314 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testNYU.txt  --folder testNYU'
cmd315 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testUKER.txt  --folder testUKER'
cmd316 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testStanford.txt  --folder testStanford'

cmd322 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general  --ckpt model_last.tar --valid_list testBraTS.txt  --folder testBraTS'
cmd323 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general  --ckpt model_last.tar --valid_list testUCSF.txt  --folder testUCSF'
cmd324 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general  --ckpt model_last.tar --valid_list testNYU.txt  --folder testNYU'
cmd325 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general  --ckpt model_last.tar --valid_list testUKER.txt  --folder testUKER'
cmd326 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general  --ckpt model_last.tar --valid_list testStanford.txt  --folder testStanford'

cmd330 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testBraTS.txt  --folder testBraTS_ModelUCSF'
cmd331 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testUCSF.txt  --folder testUCSF_ModelUCSF'
cmd332 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testNYU.txt  --folder testNYU_ModelUCSF'
cmd333 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testUKER.txt  --folder testUKER_ModelUCSF'
cmd334 = 'py  predict.py --gpu 0  --cfg deepmedic_CWT_general_LWF  --ckpt model_last.tar --valid_list testStanford.txt  --folder testStanford_ModelUCSF'
# cmds = [cmd30, cmd31, cmd32, cmd33, cmd34, cmd35, cmd36, cmd37, cmd38]
# cmds = [cmd32, cmd33, cmd34, cmd35, cmd36, cmd37, cmd38, cmd40, cmd41, cmd42, cmd43, cmd44, cmd45, cmd46, cmd47, cmd48]
# cmds = [cmd40, cmd41, cmd42, cmd43, cmd44, cmd45, cmd46, cmd47, cmd48]
# cmds = [cmd53, cmd54, cmd55]
# cmds = [cmd60, cmd61, cmd62, cmd63, cmd64, cmd65]
# cmds = [cmd100, cmd101, cmd102, cmd103]
# cmds = [cmd200, cmd201, cmd202, cmd203, cmd204]
# cmds = [cmd300, cmd301]
# cmds = [cmd312, cmd313, cmd314, cmd315, cmd316]
# cmds = [cmd322, cmd323, cmd324, cmd325, cmd326]
cmds = [cmd330, cmd331, cmd332, cmd333, cmd334]
for cmd in cmds:
    os.system(cmd)