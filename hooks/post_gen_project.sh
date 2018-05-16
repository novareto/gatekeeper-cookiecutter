#!/bin/bash

python3.6 -m venv .
./bin/pip install zc.buildout==2.11.3
./bin/buildout
pip install -r requirements.txt
pip install -e .
./bin/python generate_keys.py
./bin/pip install mod_wsgi
