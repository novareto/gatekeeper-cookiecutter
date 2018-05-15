#!./bin/python
# -*- coding: utf-8 -*-

from app import Configuration


with Configuration('config.json') as config:
    from keeper import create_rsa_pair
    create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])
