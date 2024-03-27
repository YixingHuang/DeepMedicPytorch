# Deepmedic Pytorch Version

## Official implementation for our manuscript "Deep Learning Brain Metastases Autosegmentation: Multicenter Insights on Privacy-Preserving Model Training and Generalizability"

## Prior Tensorflow version:

The official Tensorflow version of DeepMedic for our prior [Medical Physics paper](https://doi.org/10.1002/mp.15863) for brain metastases autosegmentation is publicly available [here](https://github.com/YixingHuang/DeepMedicPlus). This is a Pytorch implementation, which is convenient than the Tensorflow version for further modifications.



## Citation

The manuscript is currently under review of the Green Journal.

## Instructions

This implementation was modified from the [source](https://github.com/pykao/BraTS2018-tumor-segmentation), where we have added our proposed volume-level sensitivity-specificity (VSS) loss, knowledge distillation loss (KDL), naive transfer learning (TL), and learning without forgetting (LWF) training framework. Most instructions from the [source](https://github.com/pykao/BraTS2018-tumor-segmentation) still work here.

### Training scripts

The overall training and prediction scripts can be found with the names of [runMain_GJ.py](https://github.com/YixingHuang/DeepMedicPytorch/blob/main/runMain_GJ.py) and [runMain_GJ_UKER_Stanford.py](https://github.com/YixingHuang/DeepMedicPytorch/blob/main/runMain_GJ_UKER_Stanford.py). The scripts work for both Windows and Linux environments. But you need to modify the data paths correspondingly.

### Pretrained models

We have shared several pretrained models, which can be very beneficial for you to evaluate the model performance on your in-house data. You can also apply naive transfer learning (TL) and learning without forgetting (LWF) to improve the model performance. We are glad if you share your evaluation performance or comments/feedback with us.

The pretrained models include UKER independent training, Stanford independent training, TL of UKER -> Stanford, LWF of UKER -> Stanford, mixed training of UKER + Stanford, mixed training of five centers (UKER, Stanford, UCSF, NYU and BraTS). Each setting has 5 repeats with different random seeds.

### Open issues

Free free to open an issue, if you get any problems running this code.

## Dependencies

Our environment: Python 3.8, Pytorch 1.12.0+cu113

### multicrop library
The Pytorch DeepMedic requires a multicrop library for segment sampling to overcome the class imbalance problem. The original implementation of multicrop from [thuyen](https://github.com/thuyen/multicrop) is outdated. Please find the latest version in my [repository](https://github.com/YixingHuang/multicrop), which should be compatible with latest Pytorch versions.


## Acknowledgement
Special thanks to [pykao](https://github.com/pykao/BraTS2018-tumor-segmentation) for the original Pytorch DeepMedic implementation. My implementation was built based on it.
