# agenda_curso_profesor_rel.py
from odoo import models, fields
from datetime import datetime

class profesorcurso(models.Model):
    _name = 'agenda.profesorcurso'
    _description = 'Relación entre profesor y curso con materia'
    
    profesor_id = fields.Many2one('agenda.profesor', string="Profesor", required=True, ondelete="cascade")
    curso_id = fields.Many2one('agenda.curso', string="Curso", required=True, ondelete="cascade")

    #relacion con materias
    materia_id = fields.Many2one('agenda.materia', string="Materia", required=True)
