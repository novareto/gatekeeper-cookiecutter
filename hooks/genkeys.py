def create_rsa_pair(pvt_path, pub_path):
    import pdb; pdb.set_trace()
    from Crypto.PublicKey import RSA

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


def create_rsa_keys('apache', 'apache')
