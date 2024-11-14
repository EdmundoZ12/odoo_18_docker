# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class publicacion(models.Model):
    _name = 'agenda.publicacion'
    _description = 'Publicación de la Agenda'

    name = fields.Char(string="Titulo", required=True)
    contenido = fields.Text(string="Contenido", required=True)
    archivo_ids = fields.Many2many('ir.attachment', string="Archivos Adjuntos")
    fecha = fields.Date(string="Fecha", default=fields.Date.context_today, required=True)
    tipo_publicacion = fields.Many2one('agenda.tipopublicacion', required=True)

    # Relación directa con el usuario creador, y obtención del tipo a través de res.users
    usuario_creador_id = fields.Many2one('res.users', string="Usuario Creador", default=lambda self: self.env.user, readonly=True)
    tipo_usuario_creador = fields.Selection(related='usuario_creador_id.agenda_tipo_usuario', string="Tipo de Usuario", readonly=True, store=True)

    # Relaciones de visibilidad para cada tipo de usuario
    visible_administrativos = fields.Many2many('agenda.administrativo', string="Visible para administrativos")
    visible_profesores = fields.Many2many('agenda.profesor', string="Visible para Profesores")
    visible_tutores = fields.Many2many('agenda.tutor', string="Visible para Tutores")
    visible_alumnos = fields.Many2many('agenda.alumno', string="Visible para Alumnos")

    # comentarios
    comentario_ids = fields.One2many('agenda.comentario', 'publicacion_id', string="Comentarios")