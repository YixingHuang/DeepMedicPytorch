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
cmds = [cmd14]
for cmd in cmds:
    os.system(cmd)