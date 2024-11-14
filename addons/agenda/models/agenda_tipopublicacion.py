# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class tipopublicacion(models.Model):
    _name = 'agenda.tipopublicacion'
    _description = 'Etiqueta asignable a una publicacion'

    name = fields.Char(string="Titulo", required=True)