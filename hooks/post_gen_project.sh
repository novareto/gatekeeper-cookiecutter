#!/bin/bash

python3.6 -m venv .
./bin/pip install zc.buildout==2.11.3
./bin/buildout
./bin/python generate_keys.py
./bin/pip install mod_wsgi
