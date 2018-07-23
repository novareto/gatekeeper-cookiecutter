#!/bin/bash
python3.6 -m venv .
source ./bin/activate
pwd
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
python generate_keys.py
