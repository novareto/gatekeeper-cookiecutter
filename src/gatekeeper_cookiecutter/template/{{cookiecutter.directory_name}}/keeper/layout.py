# -*- coding: utf-8 -*-

import crom
from zope.interface import Interface
from gatekeeper.layout import Layout
from cromlech.browser import IRequest, ILayout


@crom.component
@crom.sources(IRequest, Interface)
@crom.target(ILayout)
class GKLayout(Layout):
    pass
