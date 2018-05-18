#!/bin/bash

python3.6 -m venv .
./bin/pip install --upgrade pip
./bin/pip install -r requirements.txt
./bin/pip install -e .
./bin/python generate_keys.py
