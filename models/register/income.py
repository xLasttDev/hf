# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import time

class RegisterIncomes(models.Model):
    _name = 'hf.'
    _description = 'HF: Ingresos'
    _order = 'date desc'
    
    name = fields.Char('Nombre')
    ref = fields.Char('Referencia')

    date = fields.Datetime('Fecha')
    acc_id = fields.Many2one('hf.account', 'Cuenta')
    categ_id = fields.Many2one('hf.category', 'Categoria')
    cashbox_id = fields.Many2one('hf.cashbox', 'Cashbox')
    
    qty = fields.Float('Cantidad')

    amount_import = fields.Float('Monto')
    day_exchange = fields.Float('Cambio al dia')
    company_currency_id = fields.Many2one('Moneda de compañia')
    currency_import_id = fields.Many2one('Moneda de importe')

    detalles = fields.Text('Detalles')

    subtotal = fields.Float('Subtotal')
    total = fields.Float('Total')

    attachment = fields.Binary('Adjunto')
    benef_id = fields.Many2one('res.users', 'Beneficiario')
    contact_id =  fields.Many2one('res.partner', 'Contacto')