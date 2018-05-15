#!/bin/bash

virtualenv . -p "/usr/bin/python3.5"
source bin/activate
pip install zc.buildout==2.11.3
./bin/buildout
python generate_keys.py
pip install mod_wsgi
