# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: July 1st, 2026
# | Last update..: July 1st, 2026
# | Course.......: Kaggle - Intro to Machine Learning - Basic Data Exploration
# | WhatIs.......: Housing Analysis with Pandas - Main
# +----------------------------------------------------------------------------++
# ------------------------- Instructions -----------------------
# Mana mana tutu tuturu

# ------------ Resources / Documentation involved -------------
# Basic Data Exploration: https://www.kaggle.com/code/dansbecker/basic-data-exploration

# Original dataset (Melbourne Housing Snapshot): https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

# ------------------------- Libraries -------------------------
from kaggle.api.kaggle_api_extended import KaggleApi
import os  # os.path.exists(path)
import pandas as pd

# -------------------------- Imports --------------------------


# ------------------------- Functions -------------------------


# ------------------------- Variables -------------------------
DATASET_FOLDER = 'input/melbourne-housing-snapshot'
DATASET_FILE_NAME = 'melb_data.csv'
DATASET_PATH = f'{DATASET_FOLDER}/{DATASET_FILE_NAME}'
DATASET_ID = 'dansbecker/melbourne-housing-snapshot'

# --------------------------- Code ----------------------------
try:
    with open(f'{DATASET_FOLDER}/{DATASET_FILE_NAME}'): pass
except FileNotFoundError:
    print(f'[!] File not found. Downloading dataset at {DATASET_FOLDER}')
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(DATASET_ID, path=DATASET_FOLDER, unzip=True)
    print("File successfully downloaded")


housingData = pd.read_csv(DATASET_PATH)
print(housingData.describe())

# count -> how many rows have non-missing values
# std -> standard deviation

print("Fin")
