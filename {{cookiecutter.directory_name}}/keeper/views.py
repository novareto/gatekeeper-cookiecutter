# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import IURL
from cromlech.webob import Response
from dolmen.forms.base import name, context, form_component
from dolmen.view import View, make_layout_response, view_component
from gatekeeper.login.form import BaseLoginForm
from gatekeeper.login.models import LoginRoot
from . import tal_template


@form_component
@name('login')
@context(LoginRoot)
class Login(BaseLoginForm):
    responseFactory = Response
    make_response = make_layout_response
    template = tal_template('form.pt')

    def back(self, login):
        return "https://{{cookiecutter.uri}}"

    @property
    def action_url(self):
        url = IURL(self.context, self.request, default=None)
        return url

    def authenticate(self, login, password):
        print ('HANS PETER KALUS')
        if login == "0101010001" and password == "passwort":
            return ['testasd.kuvb.de', ]
        return []


@view_component
@name('logout')
@context(LoginRoot)
class Logout(View):
    responseFactory = Response
    template = tal_template('form.pt')

    def render(self):
        pass
    
    def make_response(self, result):
        response = view.responseFactory()
        response.delete_cookie('auth_pubtkt', domain=self.context.domain)
        response.status = 302
        response.location = '/'
        return response
