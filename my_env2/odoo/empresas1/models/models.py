# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models
from datetime import datetime

class empresas(models.Model):
    _name = 'ej.empresas'
    #_name = 'res.partner'
    Nombre = fields.Text(string='Nombre de la empresa', required=True)
    Id = fields.Integer(string='Id', required=True)
    Edad = fields.Integer(string='Edad', required=True)
   # NIF = fields.Text(string='NIF de la empresa', required=True)
    #Calle = fields.Text(string='Calle', required=True)
   # CP = fields.Text(string='Codigo Postal', required=True)
    #Ciudad = fields.Text(string='Ciudad', required=True)
	#ciudad email web
