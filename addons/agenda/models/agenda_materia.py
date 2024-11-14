# -*- coding: utf-8 -*-
from odoo import models, fields

class materia(models.Model):
    _name = 'agenda.materia'
    _description = 'materia'
    
    name = fields.Char(string="Nombre del materia", required=True)

    #relacion con registro Profesor_Curso
    profesorcurso_id = fields.One2many('agenda.profesorcurso', 'materia_id', string="Profesor enseña materia: en curso:")