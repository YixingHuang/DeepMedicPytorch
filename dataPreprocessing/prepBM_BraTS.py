import pickle
import os
import numpy as np
import nibabel as nib
from utils import Parser
import time
from utils.utils import check_system

args = Parser()

patch_shapes = [
        (22, 22, 22),
        (25, 25, 25),
        (28, 28, 28)
        ]

# modalities = ('flair', 't1ce', 't1', 't2')
modalities = ('flair', )
def nib_load(file_name):

    if not os.path.exists(file_name):
        return np.array([1])

    proxy = nib.load(file_name)
    data = proxy.get_fdata()
    proxy.uncache()
    return data


def get_dist2center(patch_shape):
    ndim = len(patch_shape)
    dist2center = np.zeros((ndim, 2) , dtype='int32') # from patch boundaries
    for dim, shape in enumerate(patch_shape) :
        dist2center[dim] = [shape/2 - 1, shape/2] if shape % 2 == 0 \
                else [shape//2, shape//2]
    return dist2center


def process(path, has_label=True, n_channels=1):
    print(path)
    label = np.array(
            nib_load(path[:-1] + '-seg_ce_ud.nii.gz'), dtype='float32', order='C')

    images = np.stack([
        np.array(nib_load(path[:-1] + '-t1c_bias_norm_ud.nii.gz'), dtype='float32', order='C')
        for modal in modalities], -1)

    # print('strides', images.strides)
    # # print(modalities)
    # print(images.shape, label.shape)
    mask = images.sum(-1) > 0
    print('nchannels = ', n_channels)
    for k in range(n_channels):
        x = images[..., k]
        # print(x.shape)
        y = x[mask]
        lower = np.percentile(y, 0.2)
        upper = np.percentile(y, 99.8)
        x[mask & (x < lower)] = lower
        x[mask & (x > upper)] = upper

        y = x[mask]

        # 0.8885
        #x[mask] -= y.mean()
        #x[mask] /= y.std()

        # 0.909
        x -= y.mean()
        x /= y.std()

        #0.8704
        #x /= y.mean()

        images[..., k] = x

    #return images, label

    #output = path + 'data_f32_divm.pkl'
    output = path + 'data_f32.pkl'
    with open(output, 'wb') as f:
        pickle.dump((images, label), f)

    #mean, std = [], []
    #for k in range(4):
    #    x = images[..., k]
    #    y = x[mask]
    #    lower = np.percentile(y, 0.2)
    #    upper = np.percentile(y, 99.8)
    #    x[mask & (x < lower)] = lower
    #    x[mask & (x > upper)] = upper

    #    y = x[mask]

    #    mean.append(y.mean())
    #    std.append(y.std())

    #    images[..., k] = x
    #path = '/home/thuyen/FastData/'
    #output = path + 'data_i16.pkl'
    #with open(output, 'wb') as f:
    #    pickle.dump((images, mask, mean, std, label), f)

    if not has_label:
        return

    for patch_shape in patch_shapes:
        dist2center = get_dist2center(patch_shape)

        sx, sy, sz = dist2center[:, 0]                # left-most boundary
        ex, ey, ez = mask.shape - dist2center[:, 1]   # right-most boundary
        shape = mask.shape
        maps = np.zeros(shape, dtype="int16")
        #(240, 240, 155) 10 229 10 229 10 144 (240, 240, 155)
        maps[sx:ex, sy:ey, sz:ez] = 1

        fg = (label > 0).astype('int16')
        bg = ((mask > 0) * (fg == 0)).astype('int16')

        fg = fg * maps
        bg = bg * maps

        fg = np.stack(fg.nonzero()).T.astype('uint8')
        bg = np.stack(bg.nonzero()).T.astype('uint8')

        suffix = '{}x{}x{}_'.format(*patch_shape)

        output = path + suffix + 'coords.pkl'
        with open(output, 'wb') as f:
            pickle.dump((fg, bg), f)



def doit(dset):
    root, has_label = dset['root'], dset['has_label']
    file_list = os.path.join(root, dset['flist'])
    subjects = open(file_list).read().splitlines()
    if check_system() == 'Windows':
        names = [sub.split('\\')[-1] for sub in subjects]
    else:
        names = [sub.split('/')[-1] for sub in subjects]
    paths = [os.path.join(root, sub, name + '_') for sub, name in zip(subjects, names)]
    for path in paths:
        process(path, has_label, n_channels=len(modalities))


print(args.data_dir)
# train
train_set = {
        'root': args.data_dir,
        'flist': 'train.txt',
        'has_label': True
        }

train2_set = {
        'root': args.data_dir,
        'flist': 'train2.txt',
        'has_label': True
        }
####

val_set = {
        'root': args.test_data_dir, #'/home/thuyen/Data/brats17/Brats17ValidationData',
        'flist': 'val.txt',
        'has_label': True
        }
# test/validation data
test_set = {
        'root': args.test_data_dir, #'/home/thuyen/Data/brats17/Brats17ValidationData',
        'flist': 'test.txt',
        'has_label': False
        }

# docker
doit(train_set)
doit(val_set)
doit(test_set)
# doit(train2_set)

# benchmarking the data reading
# load f32 is faster (0.2s) than load i16 (0.7s)
#def pkload_i16(fname):
#    with open(fname, 'rb') as f:
#        images, mask, mean, std, label = pickle.load(f)
#
#    images = images.astype('float32')
#    for c in range(4):
#        x = images[..., c]
#        x[mask] -= mean[c]
#        x[mask] /= std[c]
#        images[..., c] = x
#
#    return images, label
#
#def pkload(fname):
#    with open(fname, 'rb') as f:
#        return pickle.load(f)
#
#fname = '/home/thuyen/FastData/data_f32.pkl'
#fname = '/home/thuyen/FastData/data_i16.pkl'
#
#start = time.time()
##x = pkload_i16(fname)
#x = pkload(fname)
#print(time.time() - start)


#path = '/media/ssd1/thuyen/Brats17TrainingData/LGG/Brats17_2013_0_1/Brats17_2013_0_1_'
#a2, b2 = process(path, True)
#a1, b1 = pickle.load(open('/home/thuyen/Brats17_2013_0_1_data_f32.pkl', 'rb'))
#x = np.abs(a2-a1)
#print(x.max())

