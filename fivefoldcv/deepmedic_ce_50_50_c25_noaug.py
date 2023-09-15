from subprocess import call

import os

out_dir = '/media/hdd1/pkao/brats2018/output/validation/'

model = 'deepmedic_ce_50_50_c25_noaug'

if not os.path.exists(os.path.join(out_dir, model)): os.mkdir(os.path.join(out_dir, model))

folds = ['fold0', 'fold1', 'fold2', 'fold3', 'fold4']

for fold in folds:
	cfg_name = model+'_'+fold

	out = os.path.join(out_dir, model)
	
	call(['python', 'train.py', '--gpu', '1', '--cfg', cfg_name, '--out', out])
