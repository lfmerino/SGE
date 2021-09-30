# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models
from datetime import datetime

class dam1(models.Model):
    _name = 'res.partner'
    _inherit ='res.partner'
    id = fields.Integer(string='Id del registro', required=True)

    name = fields.Text(string='Nombre de la empresa', required=True)

    vat = fields.Text(string='NIF de la empresa', required=True)

    lang = fields.Text(string='Idioma', required=True)

    street = fields.Text(string='Calle', required=True)

    zip = fields.Text(string='Codigo Postal', required=True)

    city = fields.Text(string='Ciudad', required=True)

    phone = fields.Integer(string='Telefono de la empresa', required=True)

    email = fields.Text(string='Email', required=True)

    website = fields.Text(string='Pagina web', required=True)

