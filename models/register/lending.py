# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import time

class RegisterLending(models.Model):
    _name = 'hf.lending'
    _description = 'HF: Prestamos'
    _order = 'date asc'
    
    name = fields.Char('Nombre')
    ref = fields.Char('Referencia')

    date = fields.Datetime('Fecha')
    date_limit = fields.Datetime('Fecha limite')
    date_deadlines = fields.Many2one('Plazos de pago')

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
    user_id = fields.Many2one('res.users', 'Prestamista')
    benef_id = fields.Many2one('res.partner', 'Deudor')


