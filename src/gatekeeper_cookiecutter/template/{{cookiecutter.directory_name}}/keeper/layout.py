# -*- coding: utf-8 -*-

import crom
from zope.interface import Interface
from gatekeeper.layout import Layout
from gatekeeper.admin import get_valid_messages
from cromlech.browser import IRequest, ILayout
from cromlech.sqlalchemy import SQLAlchemySession


@crom.component
@crom.sources(IRequest, Interface)
@crom.target(ILayout)
class GKLayout(Layout):

    def get_messages(self):
        with SQLAlchemySession(self.context.engine) as session:
            messages = get_valid_messages(session)
        return messages
