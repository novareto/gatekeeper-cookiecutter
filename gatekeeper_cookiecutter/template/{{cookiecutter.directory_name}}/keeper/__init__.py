# -*- coding: utf-8 -*-

from os import path, makedirs, chmod
from Crypto.PublicKey import RSA
from zope.i18nmessageid import MessageFactory
from cromlech.webob import Response
from cromlech.browser.interfaces import ITypedRequest
from dolmen.template import TALTemplate
from dolmen.view import View, make_layout_response


i18n = MessageFactory("gatekeeper")
TEMPLATE_DIR = path.join(path.dirname(__file__), 'templates')


def tal_template(name):
    return TALTemplate(path.join(TEMPLATE_DIR, name))


def create_rsa_pair(pvt_path, pub_path):

    priv = path.isfile(pvt_path)
    pub = path.isfile(pub_path)

    if not priv or not pub:  # IMPORTANT : We override the existing one.

        container = path.dirname(pvt_path)
        if not path.isdir(container):
            makedirs(container)

        container = path.dirname(pub_path)
        if not path.isdir(container):
            makedirs(container)
            
        key = RSA.generate(2048)

        with open(pvt_path, 'wb') as fd:
            chmod(pvt_path, 0o600)
            fd.write(key.exportKey('PEM'))

        pubkey = key.publickey()
        with open(pub_path, 'wb') as fd:
            fd.write(pubkey.exportKey('PEM'))
