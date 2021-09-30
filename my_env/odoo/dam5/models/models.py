# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class dam5(models.Model):
#     _name = 'dam5.dam5'
     _name = 'res.partner'
#     _description = 'dam5.dam5'

     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
