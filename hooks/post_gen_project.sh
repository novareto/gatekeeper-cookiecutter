#!/bin/bash

openssl genrsa -out privkey.pem 1024
openssl rsa -in privkey.pem -out pubkey.pem -pubout
