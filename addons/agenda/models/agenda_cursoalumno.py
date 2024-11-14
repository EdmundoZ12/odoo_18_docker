# agenda_curso_alumno_rel.py
from odoo import models, fields
from datetime import datetime

class cursoalumno(models.Model):
    _name = 'agenda.cursoalumno'
    _description = 'Relación entre Curso y Alumno con Año'
    
    curso_id = fields.Many2one('agenda.curso', string="Curso", required=True, ondelete="cascade")
    alumno_id = fields.Many2one('agenda.alumno', string="Alumno", required=True, ondelete="cascade")
    gestion = fields.Date(string="Gestión", default=lambda self: datetime.now().strftime('%Y-01-01'))
