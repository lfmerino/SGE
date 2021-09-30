# -*- coding: utf-8 -*-
 from odoo import http


# class Dam5(http.Controller):
#     @http.route('/dam5/dam5/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dam5/dam5/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dam5.listing', {
#             'root': '/dam5/dam5',
#             'objects': http.request.env['dam5.dam5'].search([]),
#         })

#     @http.route('/dam5/dam5/objects/<model("dam5.dam5"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dam5.object', {
#             'object': obj
#         })
