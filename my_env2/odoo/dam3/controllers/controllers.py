# -*- coding: utf-8 -*-
# from odoo import http


# class Dam3(http.Controller):
#     @http.route('/dam3/dam3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dam3/dam3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dam3.listing', {
#             'root': '/dam3/dam3',
#             'objects': http.request.env['dam3.dam3'].search([]),
#         })

#     @http.route('/dam3/dam3/objects/<model("dam3.dam3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dam3.object', {
#             'object': obj
#         })
