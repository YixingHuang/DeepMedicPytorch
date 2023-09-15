from subprocess import call

import os

out_dir = '/media/hdd2/pkao/brats2018/output/training/'

model = 'deepmedic_ce_c25_45_60_75_b50_mb50_all_s0104'

if not os.path.exists(os.path.join(out_dir, model)): os.mkdir(os.path.join(out_dir, model))

folds = ['fold0', 'fold1', 'fold2', 'fold3', 'fold4']

for fold in folds:
	cfg_name = model+'_'+fold

	out = os.path.join(out_dir, model)
	
	call(['python', 'train.py', '--gpu', '3', '--cfg', cfg_name, '--out', out])
