# -*- coding: utf-8 -*-
from odoo import http

# class Primero(http.Controller):
#     @http.route('/primero/primero/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/primero/primero/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('primero.listing', {
#             'root': '/primero/primero',
#             'objects': http.request.env['primero.primero'].search([]),
#         })

#     @http.route('/primero/primero/objects/<model("primero.primero"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('primero.object', {
#             'object': obj
#         })