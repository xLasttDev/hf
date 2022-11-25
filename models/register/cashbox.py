# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
import time

class RegisterCashBox(models.Model):
    _name = 'hf.cashbox'
    _description = 'HF: Caja Base'
    _order = 'name asc'
    
    name = fields.Char('Nombre')

    #? PENDIENTE POR ACTIVAR UNA VEZ SE ACTIVEN LOS OTROS MODELOS
    # income_ids = fields.One2many('hf.income', 'cashbox_id', 'Ingresos')
    # expense_ids = fields.One2many('hf.expense', 'cashbox_id', 'Egresos')
    # lending_ids = fields.One2many('hf.lending', 'cashbox_id', 'Prestamos')


    period_year = fields.Char('Año')
    period_start = fields.Date('Periodo de Inicio')
    period_end = fields.Date('Periodo de Fin')

    # income_vs_expense = fields.Many2many('')


 
