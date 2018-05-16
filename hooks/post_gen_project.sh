#!/bin/bash

python3.6 -m venv .
./bin/pip install -r requirements.txt
./bin/pip install -e .
./bin/buildout
./bin/python generate_keys.py
./bin/pip install mod_wsgi
