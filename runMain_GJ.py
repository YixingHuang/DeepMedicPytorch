import os
os.environ['CUDA_VISIBLE_DEVICES'] = "1"

cmd103 = 'py  train.py --gpu 0  --cfg GJ_mixedDataExp'
cmd104 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd105 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd106 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd107 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd108 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd203 = 'py  train.py --gpu 0  --cfg GJ_mixedDataExp2'
cmd204 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp2 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd205 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp2 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd206 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp2 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd207 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp2 --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd208 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp2 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd303 = 'py  train.py --gpu 0  --cfg GJ_mixedDataExp3'
cmd304 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp3 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd305 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp3 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd306 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp3 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd307 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp3 --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd308 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp3 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd403 = 'py  train.py --gpu 0  --cfg GJ_mixedDataExp4'
cmd404 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp4 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd405 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp4 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd406 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp4 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd407 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp4 --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd408 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp4 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'

cmd503 = 'py  train.py --gpu 0  --cfg GJ_mixedDataExp5'
cmd504 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp5 --ckpt model_last.tar --folder testUKER --valid_list testUKER.txt'
cmd505 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp5 --ckpt model_last.tar --folder testUCSF --valid_list testUCSF.txt'
cmd506 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp5 --ckpt model_last.tar --folder testNYU --valid_list testNYU.txt'
cmd507 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp5 --ckpt model_last.tar --folder testBraTS --valid_list testBraTS.txt'
cmd508 = 'py  predict.py --gpu 0  --cfg GJ_mixedDataExp5 --ckpt model_last.tar --folder testStanford --valid_list testStanford.txt'


cmds = [
        cmd103, cmd104, cmd105, cmd106, cmd107, cmd108,
        cmd203, cmd204, cmd205, cmd206, cmd207, cmd208,
        cmd303, cmd304, cmd305, cmd306, cmd307, cmd308,
        cmd403, cmd404, cmd405, cmd406, cmd407, cmd408,
        cmd503, cmd504, cmd505, cmd506, cmd507, cmd508,
]

for cmd in cmds:
    os.system(cmd)