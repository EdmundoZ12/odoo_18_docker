# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class comentario(models.Model):
    _name = 'agenda.comentario'
    _description = 'Comentario de una publicacion'

    contenido = fields.Text(string="Contenido", required=True)
    fecha_hora = fields.Datetime(string="Fecha y Hora", default=fields.Datetime.now, readonly=True, required=True)

    # Relación directa con el usuario creador, y obtención del tipo a través de res.users
    usuario_creador_id = fields.Many2one('res.users', string="Usuario Creador", default=lambda self: self.env.user, readonly=True)
    tipo_usuario_creador = fields.Selection(related='usuario_creador_id.agenda_tipo_usuario', string="Tipo de Usuario", readonly=True, store=True)

    #relacion a publicacion
    publicacion_id = fields.Many2one('agenda.publicacion', string="Comentario",required=True, readonly=True)