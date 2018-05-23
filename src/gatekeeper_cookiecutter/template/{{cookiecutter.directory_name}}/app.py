import os
import sys
import json
import crom
import dolmen.tales
import gatekeeper
import keeper
import grokker, dolmen.view, dolmen.forms.base, dolmen.forms.ztk
from dolmen.forms.ztk.fields import registerDefault

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
from gatekeeper.admin import Messages
from cromlech.sqlalchemy import create_engine

engine = create_engine(config['db']['uri'], config['db']['key'])
engine.bind(Messages)
Messages.metadata.create_all()


# Login
from gatekeeper.login.models import LoginRoot

class LoginRoot(LoginRoot):
    displayMessages = True

    def __init__(self, engine, domain, pubkey, dest):
        self.engine = engine
        self.domain = domain
        self.pkey = pubkey
        self.dest = dest


loginroot = LoginRoot(
    engine,
    config['global']['domain'],
    config['crypto']['privkey'],
    config['global']['dest'],
)

# The application.
from cromlech.auth import BasicAuth
from gatekeeper import serve_view
from gatekeeper.admin import messager
from gatekeeper.ticket import cipher
from rutter.urlmap import URLMap


mapping = URLMap()
mapping['/'] = cipher(serve_view(
    'login', root=loginroot), None, config['crypto']['cipher'])
mapping['/unauthorized'] = serve_view('unauthorized', root=loginroot)
mapping['/timeout'] = serve_view('timeout', root=loginroot)
mapping['/logout'] = serve_view('logout', root=loginroot)
mapping['/admin'] = BasicAuth(auth_users)(messager(engine))

# Middlewares wrapping if needed
application = mapping

print(application, "Application is ready.")
