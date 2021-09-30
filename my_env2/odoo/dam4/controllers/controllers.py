# -*- coding: utf-8 -*-
from odoo import http


# class Dam4(http.Controller):
#     @http.route('/dam4/dam4/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dam4/dam4/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dam4.listing', {
#             'root': '/dam4/dam4',
#             'objects': http.request.env['dam4.dam4'].search([]),
#         })

#     @http.route('/dam4/dam4/objects/<model("dam4.dam4"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dam4.object', {
#             'object': obj
#         })
