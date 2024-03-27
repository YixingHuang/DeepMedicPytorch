# Deepmedic Pytorch Version

## Official implementation for our manuscript "Deep Learning Brain Metastases Autosegmentation: Multicenter Insights on Privacy-Preserving Model Training and Generalizability"

The official Tensorflow version of DeepMedic for our prior [Medical Physics paper](https://doi.org/10.1002/mp.15863) for brain metastases autosegmentation is publicly available [here](https://github.com/YixingHuang/DeepMedicPlus)

## Citation

The manuscript is currently under review of the Green Journal.


## Dependencies

Our environment: Python 3.8, Pytorch 1.12.0+cu113


The Pytorch DeepMedic requires a multicrop library for segment sampling to overcome the class imbalance problem. The original implementation of multicrop from [thuyen](https://github.com/thuyen/multicrop) is outdated. Please find the latest version in my [repository](https://github.com/YixingHuang/multicrop), which should be compatible with latest Pytorch versions.





Special thanks to [pykao](https://github.com/pykao/BraTS2018-tumor-segmentation) for the original Pytorch DeepMedic implementation. My implementation was built based on it.
