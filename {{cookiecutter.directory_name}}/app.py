#!./bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json


class Configuration(object):

    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise RuntimeError('Configuration file does not exist.')
        self.environ = filename

    def __enter__(self):
        with open(self.environ, "r") as fd:
            env = json.load(fd)
        return env['conf']

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Configuration('config.json') as config:

    import crom
    import dolmen.tales
    import gatekeeper
    import keeper
    import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
    from dolmen.forms.ztk.fields import registerDefault
    from gatekeeper.ticket import cipher

    crom.monkey.incompat()
    crom.implicit.initialize()
    registerDefault()

    crom.configure(
        dolmen.forms.base,
        dolmen.forms.ztk,
        dolmen.tales,
        dolmen.view,
        keeper,
        gatekeeper,
        grokker,
    )

    from gatekeeper import serve_view
    from gatekeeper.login.models import LoginRoot
    from rutter.urlmap import URLMap

    class LoginRoot(LoginRoot):

        def __init__(self, domain, pubkey, dest):
            self.domain = domain
            self.pkey = pubkey
            self.dest = dest

    # Login
    loginroot = LoginRoot(
        config['global']['domain'],
        config['crypto']['privkey'],
        config['global']['dest'],
    )

    # The application.
    mapping = URLMap()
    mapping['/'] = cipher(serve_view(
        'login', root=loginroot), None, config['crypto']['cipher'])
    mapping['/unauthorized'] = serve_view('unauthorized', root=loginroot)
    mapping['/timeout'] = serve_view('timeout', root=loginroot)

    # Middlewares wrapping if needed
    application = mapping

    print(application, "Application is ready.")
