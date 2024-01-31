import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd1 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF_LWF'
cmd2 = 'py  predict.py --gpu 0  --cfg NO_UCSF_LWF -ckpt model_last.tar -folder test'

cmd606 = 'py  predict.py --gpu 0  --cfg deepmedic_jvssPr_BM -ckpt model_last.tar -folder testLastUCSF'

cmd3 = 'py  train_LWF.py --gpu 0  --cfg NO_NYU_LWF'
cmd4 = 'py  predict.py --gpu 0  --cfg NO_NYU_LWF -ckpt model_last.tar -folder test'

cmd5 = 'py  train_LWF.py --gpu 0  --cfg NO_Stanford_LWF'
cmd6 = 'py  predict.py --gpu 0  --cfg NO_Stanford_LWF -ckpt model_last.tar -folder test'

cmd7 = 'py  train_LWF.py --gpu 0  --cfg NO_BraTS_LWF'
cmd8 = 'py  predict.py --gpu 0  --cfg NO_BraTS_LWF -ckpt model_last.tar -folder test'


cmd10 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_BraTS_Precision -ckpt model_last.tar -folder testUKER'
cmd11 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_NYU_Precision -ckpt model_last.tar -folder testUKER'
cmd12 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Stanford_Precision -ckpt model_last.tar -folder testUKER'
cmd13 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF_Precision -ckpt model_last.tar -folder testUKER'
cmd14 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_Zurich_Precision -ckpt model_last.tar -folder testUKER'


cmd20 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF2_LWF'
cmd21 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_LWF -ckpt model_last.tar -folder test'
cmd22 = 'py  train.py --gpu 0  --cfg NO_UCSF2_TL'
cmd23 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_TL -ckpt model_last.tar -folder test'
cmd24 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF2_Precision'
cmd25 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF2_Precision -ckpt model_last.tar -folder test'

cmd26 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_LWF -ckpt model_last.tar -folder testUKER'
cmd27 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_TL -ckpt model_last.tar -folder testUKER'
cmd28 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF2_Precision -ckpt model_last.tar -folder testUKER'

cmd30 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF2_LWF'
cmd31 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_LWF -ckpt model_last.tar -folder test'
cmd32 = 'py  train.py --gpu 0  --cfg NO_UCSF2_TL'
cmd23 = 'py  predict.py --gpu 0  --cfg NO_UCSF2_TL -ckpt model_last.tar -folder test'
cmd24 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF2_Precision'
cmd25 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF2_Precision -ckpt model_last.tar -folder test'

cmd40 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF'
cmd41 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF -ckpt model_last.tar -folder test'
cmd42 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL'
cmd43 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL -ckpt model_last.tar -folder test'
cmd44 = 'py  train.py --gpu 0  --cfg deepmedic_vss_UCSF4_Precision'
cmd45 = 'py  predict.py --gpu 0  --cfg deepmedic_vss_UCSF4_Precision -ckpt model_last.tar -folder test'

cmd50 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF2'
cmd51 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF2 -ckpt model_last.tar -folder test'
cmd52 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL2'
cmd53 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL2 -ckpt model_last.tar -folder test'

cmd60 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF3'
cmd61 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF3 -ckpt model_last.tar -folder test'
cmd62 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL3'
cmd63 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL3 -ckpt model_last.tar -folder test'


cmd80 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF4'
cmd81 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF4 -ckpt model_last.tar -folder test'
cmd82 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL4'
cmd83 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL4 -ckpt model_last.tar -folder test'

cmd90 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF5'
cmd91 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF5 -ckpt model_last.tar -folder test'
cmd92 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL5'
cmd93 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL5 -ckpt model_last.tar -folder test'

cmd100 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF4_LWF6'
cmd101 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_LWF6 -ckpt model_last.tar -folder test'
cmd102 = 'py  train.py --gpu 0  --cfg NO_UCSF4_TL6'
cmd103 = 'py  predict.py --gpu 0  --cfg NO_UCSF4_TL6 -ckpt model_last.tar -folder test'


cmd150 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF5_LWF2'
cmd151 = 'py  predict.py --gpu 0  --cfg NO_UCSF5_LWF2 -ckpt model_last.tar -folder test'
cmd160 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF5_LWF3'
cmd161 = 'py  predict.py --gpu 0  --cfg NO_UCSF5_LWF3 -ckpt model_last.tar -folder test'
cmd170 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF5_LWF4'
cmd171 = 'py  predict.py --gpu 0  --cfg NO_UCSF5_LWF4 -ckpt model_last.tar -folder test'
cmd180 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF5_LWF5'
cmd181 = 'py  predict.py --gpu 0  --cfg NO_UCSF5_LWF5 -ckpt model_last.tar -folder test'
cmd190 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF5_LWF6'
cmd191 = 'py  predict.py --gpu 0  --cfg NO_UCSF5_LWF6 -ckpt model_last.tar -folder test'

cmds = [cmd150, cmd151, cmd160, cmd161, cmd170, cmd171, cmd180, cmd181, cmd190, cmd191]
for cmd in cmds:
    os.system(cmd)