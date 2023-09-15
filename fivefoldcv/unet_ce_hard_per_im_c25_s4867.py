from subprocess import call

import os

out_dir = '/media/hdd2/pkao/brats2018/output/training/'

model = 'unet_ce_hard_per_im_c25_s4867'

if not os.path.exists(os.path.join(out_dir, model)): os.mkdir(os.path.join(out_dir, model))

#folds = ['fold0', 'fold1', 'fold2', 'fold3', 'fold4']

folds = ['fold4']

for fold in folds:
	cfg_name = model+'_'+fold

	out = os.path.join(out_dir, model)
	
	call(['python', 'train_unet.py', '--gpu', '1', '--cfg', cfg_name, '--out', out])
