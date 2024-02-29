#!/bin/bash

sudo apt-get update
sudo apt install python3-pip
pip install -r requirements.txt
python3 data_creation.py
python3 model_preprocessing.py
python3 model_preparation.py
python3 model_testing.py