import os
import json
from keeper import create_rsa_pair

CONF = 'config.json'

if not os.path.isfile(CONF):
    raise RuntimeError('Configuration file does not exist.')

with open(CONF, "r") as fd:
    config = json.load(fd)
    
create_rsa_pair(config['crypto']['privkey'], config['crypto']['pubkey'])
