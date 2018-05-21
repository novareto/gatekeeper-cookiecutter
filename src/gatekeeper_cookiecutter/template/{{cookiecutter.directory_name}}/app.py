import os
import sys
import json
import crom
import dolmen.tales
import gatekeeper
import keeper
import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk

from cromlech.auth import BasicAuth
from cromlech.sqlalchemy import create_engine
from dolmen.forms.ztk.fields import registerDefault
from gatekeeper import serve_view
from gatekeeper.admin import Messages, messager
from gatekeeper.login.models import LoginRoot
from gatekeeper.ticket import cipher
from rutter.urlmap import URLMap


# Grokking
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
    grokker
)


# Configuration
CONF = 'config.json'
auth_users = {
    'admin': 'admin',
}

if not os.path.isfile(CONF):
    raise RuntimeError('Configuration file does not exist.')

with open(CONF, "r") as fd:
    config = json.load(fd)


# Database
engine = create_engine(config['db']['uri'], config['db']['key'])
engine.bind(Messages)
Messages.metadata.create_all()


# Login
class LoginRoot(LoginRoot):
    
    def __init__(self, domain, pubkey, dest):
        self.domain = domain
        self.pkey = pubkey
        self.dest = dest

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
mapping['/logout'] = serve_view('logout', root=loginroot)
mapping['/admin'] = BasicAuth(messager(engine), auth_users)

# Middlewares wrapping if needed
application = mapping

print(application, "Application is ready.")
