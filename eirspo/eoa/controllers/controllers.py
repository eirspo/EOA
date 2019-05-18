# -*- coding: utf-8 -*-
from odoo import http

class Eoa(http.Controller):
    @http.route('/eoa/eoa/', auth='public')
    def index(self, **kw):
        return "Hello, world"
