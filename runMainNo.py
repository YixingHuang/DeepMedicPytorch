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

cmd200 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF6_LWF'
cmd201 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_LWF -ckpt model_last.tar -folder test'
cmd202 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF6_LWF2'
cmd203 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_LWF2 -ckpt model_last.tar -folder test'
cmd204 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF6_LWF3'
cmd205 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_LWF3 -ckpt model_last.tar -folder test'
cmd206 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF6_LWF4'
cmd207 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_LWF4 -ckpt model_last.tar -folder test'
cmd208 = 'py  train_LWF.py --gpu 0  --cfg NO_UCSF6_LWF4'
cmd209 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_LWF5 -ckpt model_last.tar -folder test'

cmd210 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL3'
cmd211 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_TL3 -ckpt model_last.tar -folder test'

cmd212 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL4'
cmd213 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_TL4 -ckpt model_last.tar -folder test'

cmd220 = 'py  train.py --gpu 0  --cfg NO_UKER'
cmd221 = 'py  predict.py --gpu 0  --cfg NO_UKER -ckpt model_best.tar -folder test'


cmd230 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL1'
cmd231 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_TL1 -ckpt model_last.tar -folder test'

cmd232 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL2'
cmd233 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_TL2 -ckpt model_last.tar -folder test'


cmd234 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL5'
cmd235 = 'py  predict.py --gpu 0  --cfg NO_UCSF6_TL5 -ckpt model_last.tar -folder test'

cmd236 = 'py  train.py --gpu 0  --cfg NO_UCSF6_TL6'


cmd240 = 'py  train.py --gpu 0  --cfg NO_UCSF7_TL1'
cmd241 = 'py  predict.py --gpu 0  --cfg NO_UCSF7_TL1 -ckpt model_best.tar -folder test'

cmd242 = 'py  train.py --gpu 0  --cfg NO_UCSF7_TL2'
cmd243 = 'py  predict.py --gpu 0  --cfg NO_UCSF7_TL2 -ckpt model_best.tar -folder test'

cmd244 = 'py  train.py --gpu 0  --cfg NO_UCSF7_TL3'
cmd245 = 'py  predict.py --gpu 0  --cfg NO_UCSF7_TL3 -ckpt model_best.tar -folder test'

cmd246 = 'py  train.py --gpu 0  --cfg NO_UCSF7_TL4'
cmd247 = 'py  predict.py --gpu 0  --cfg NO_UCSF7_TL4 -ckpt model_best.tar -folder test'

cmd250 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF'
cmd251 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd252 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd300 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF2'
cmd301 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd302 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd303 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF3'
cmd304 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd305 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd306 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF4'
cmd307 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd308 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd309 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF5'
cmd310 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd312 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd313 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF6'
cmd314 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF6 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd315 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF6 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd316 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF7'
cmd317 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF7 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd318 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF7 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd319 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF8'
cmd320 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF8 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd321 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF8 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd322 = 'py  train.py --gpu 0  --cfg NO_UKER_UCSF9'
cmd323 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF9 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd324 = 'py  predict.py --gpu 0  --cfg NO_UKER_UCSF9 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
# cmds = [cmd300, cmd301, cmd302, cmd303, cmd304, cmd305, cmd306, cmd307, cmd308, cmd309, cmd310, cmd312, cmd313, cmd314, cmd315, cmd316, cmd317, cmd318, cmd319, cmd320, cmd321, cmd322, cmd323, cmd324]


cmd401 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd402 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd403 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'
cmd404 = 'py  predict.py --gpu 0  --cfg deepmedic_ESTRO_BraTS_LWF3 --ckpt model_last.tar --folder testBraTSRegNorm --valid_list testBraTS.txt'


cmd500 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm'
cmd501 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd502 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd503 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL'
cmd504 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd505 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd510 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm2'
cmd511 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd512 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd513 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL2'
cmd514 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd515 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd520 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm3'
cmd521 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd522 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd523 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL3'
cmd524 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd525 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd530 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm4'
cmd531 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd532 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd533 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL4'
cmd534 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd535 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd540 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm5'
cmd541 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd542 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd543 = 'py  train.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL5'
cmd544 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd545 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_TL5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd550 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF'
cmd551 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd552 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd553 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF2'
cmd554 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd555 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd556 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF3'
cmd557 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd558 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd559 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF4'
cmd560 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd561 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd562 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF5'
cmd563 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd564 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd570 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha'
cmd571 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd572 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd573 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha2'
cmd574 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd575 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd576 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha3'
cmd577 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd578 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd579 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha4'
cmd580 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd581 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd582 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5'
cmd583 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd584 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd585 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha6'
cmd586 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha6 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd587 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha6 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd588 = 'py  train_LWF.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5_2'
cmd589 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5_2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd590 = 'py  predict.py --gpu 0  --cfg NO_UKER_regnorm_UCSF_LWF_alpha5_2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'

cmd600 = 'py  train.py --gpu 0  --cfg NO_UCSF_regnorm'
cmd601 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd602 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd610 = 'py  train.py --gpu 0  --cfg NO_UCSF_regnorm2'
cmd611 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd612 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd620 = 'py  train.py --gpu 0  --cfg NO_UCSF_regnorm3'
cmd621 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd622 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd630 = 'py  train.py --gpu 0  --cfg NO_UCSF_regnorm4'
cmd631 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd632 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmd640 = 'py  train.py --gpu 0  --cfg NO_UCSF_regnorm5'
cmd641 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd642 = 'py  predict.py --gpu 0  --cfg NO_UCSF_regnorm5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'


cmds = [cmd588, cmd589, cmd590]
for cmd in cmds:
    os.system(cmd)
