# Detection and Classification Using Multi-Layer Perceptrons

## Setup

1. **Create a virtual environment** and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Dataset

### Brain Tumor (MRI)
- Download the dataset from [Kaggle: Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset/data).
- Extract the `Train` and `Test` folders to the `Data/Brain_Tumor` folder in the main project directory.

### Fetus (Ultrasound)
- Download the dataset from [Kaggle: Ultrasound Fetus Dataset](https://www.kaggle.com/datasets/orvile/ultrasound-fetus-dataset/data).
- Extract the `train` and `test` folders to the `Data/Fetus` folder in the main project directory.

### Liver (Ultrasound)
- Download the dataset from [Kaggle: Annotated Ultrasound Liver images Dataset](https://www.kaggle.com/datasets/orvile/annotated-ultrasound-liver-images-dataset).
- Extract the `727660` folder to main project directory and run `python liver_test_train_data.py`.
- Delete the `727660` folder in the main project directory.


## Directory
After the setup is completed, the file directory should look like this:

```
├── Data
│   ├── Brain_Tumor
│   │   ├── Train
│   │   └── Test
│   ├── Fetus
│   │   ├── train
│   │   └── test
|   └── Liver
│       ├── train
│       └── test
├── Models
│   ├── brain_tumor_model.h5
│   ├── fetus_model.h5
│   └── liver_model.h5
├── venv/
├── brain_tumor_mlp_model_detection.ipynb
├── fetus_mlp_model_detection.ipynb
├── liver_mlp_model_detection.ipynb
├── liver_test_train_data.py
├── requirements.txt
├── venv/
└── README.md
```


