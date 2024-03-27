# Deepmedic Pytorch Version

# Official implementation for our manuscript "Deep Learning Brain Metastases Autosegmentation: Multicenter Insights on Privacy-Preserving Model Training and Generalizability"

The official Tensorflow version of DeepMedic for our prior [Medical Physics paper](https://doi.org/10.1002/mp.15863) for brain metastases autosegmentation is publicly available [here](https://github.com/YixingHuang/DeepMedicPlus)

## Citation

The system was employed for our research presented in [1,2], where the we integrate multiple DeepMedics and 3D U-Nets in order to get a robust tumor segmentation mask. We also utilize the brain parcellation masks for the purpose of bringing the location information to DeepMedic and 3D U-Net. If the use of the software or the idea of the paper positively influences your endeavours, please cite [1,2].

[1] **Po-Yu Kao**, Thuyen Ngo, Angela Zhang, Jefferson Chen, and B. S. Manjunath, "[Brain Tumor Segmentation and Tractographic Feature Extraction from Structural MR Images for Overall Survival Prediction.](https://arxiv.org/abs/1807.07716)"  International MICCAI Brainlesion Workshop. Springer, Cham, 2018.

[2] **Po-Yu Kao**, Shailja Shailja, Jiaxiang Jiang, Angela Zhang, Amil Khan, Jefferson W. Chen, and B. S. Manjunath, "[Improving Patch-Based Convolutional Neural Networks for MRI Brain Tumor Segmentation by Leveraging Location Information](https://www.frontiersin.org/articles/10.3389/fnins.2019.01449/full)" Front. Neurosci. 13:1449. doi: 10.3389/fnins.2019.01449 


## Dependencies

Python3.6

Pytorch0.4.0

`pip install git+https://github.com/pykao/pytorch-v0.4.0@pytorch_0.4.0_poyu`

Install custom pytorch kernels from https://github.com/thuyen/multicrop

`pip install git+https://github.com/thuyen/multicrop.git`

## Required Python libraries

nibabel, nipype, natsort, SimpleITK

`pip install nibabel,nipype,natsort,SimpleITK`

## Required Sofware

FSL (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation)

## Existing Brain Parcellation in Subject Space for BraTS2018 dataset

The Harvard-Oxford subcortical atlases in subject space are stored at `BrainParcellation/HarvardOxford-sub`

## Create the HarvardOxford Subcortical Brain Parcellation to Subject Space for New BraTS Subject

```
python createBrainParcellation.py -i /DIR_TO_MR_T1.nii.gz -o /DIR_TO_SAVE_THE_BRAIN_PARCELLATION -n SUBJECT_NAME
```

The output brain parcellation will be named as SUBJECT_NAME_HarvardOxford-sub.nii.gz

## Using Brain Parcellation on DeepMedic and 3D U-Net

For using the brain parcellation on DeepMedic and 3D U-Net, please change the paths in `data/parcellation.py` accordingly

## How to run

### Change:

```
experiments/settings.yaml
```

to point to data directories. These are general settings, applied to all
experiments. Additional experiment-specific configuration will overwrite
these.

### Split data to 5 fold train/valid splits:

```
python split.py
```

### Preprocess data (look at the script for more details):

```
python prep.py
```

### Prepare parcellation data:

For using the brain parcellation for DeepMedic and 3D U-Net, please change the paths in `data/parcellation.py` accordingly

```
python data/parcellation.py
```

### For standard DeepMedic, run:
```
python train.py --gpu 0 --cfg deepmedic_ce
```

### For DeepMedic with 12-by-12-by-12 output mask, run: 
```
python train_12.py --gpu 0 --cfg deepmedic_ce_28x20x12
```

### For DeepMedic with 6-by-6-by-6 output mask, run: 
```
python train_6.py --gpu 0 --cfg deepmedic_ce_22X18X6
```

### For 3D U-Net run:
```
python train_unet.py --gpu 0 --cfg unet_dice2
```

### Prediction

To make predictions, run `predict.py`, `predict_6.py`, `predict_12.py` or `predict_unet.py` with similar arguments

### Submission

To make submissions, look at `make_submission.py`

### Memory Issue (Data Compression)

If you do not have enough memory to save the output probability maps, you are able to compress these maps to uint16 format by `compress_data.py`

To make submissions with compressed probability maps, please refer to `ensemble_methods.py`



Special thanks to [Thuyen Ngo](https://github.com/thuyen).
