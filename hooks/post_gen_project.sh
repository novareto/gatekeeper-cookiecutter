#!/bin/bash

virtualenv . -p "/usr/bin/python3.5"
source bin/activate
python bootstrap.py
./bin/buildout
./bin/python generate_keys.py
