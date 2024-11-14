# -*- coding: utf-8 -*-
from odoo import models, fields

class users(models.Model):
    _inherit = 'res.users'

    # Relaciones One2many con cada uno de los roles
    agenda_administrativo_id = fields.One2many('agenda.administrativo','user_id', string="Administrativo")
    agenda_profesor_id = fields.One2many('agenda.profesor','user_id', string="Profesor")
    agenda_tutor_id = fields.One2many('agenda.tutor','user_id', string="Tutor")
    agenda_alumno_id = fields.One2many('agenda.alumno','user_id', string="Alumno")

    # Campo computado para el tipo de usuario
    agenda_tipo_usuario = fields.Selection(
        [('administrativo', 'Administrativo'), 
         ('profesor', 'Profesor'), 
         ('tutor', 'Tutor'),
         ('alumno', 'Alumno')],
        string="Tipo de Usuario",
        store=True
    )