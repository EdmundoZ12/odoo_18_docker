# -*- coding: utf-8 -*-
from odoo import models, fields


class curso(models.Model):
    _name = "agenda.curso"
    _description = "curso"

    name = fields.Char(string="Nombre del curso", required=True)
    seccion = fields.Selection(
        [("a", "A"), ("b", "B"), ("c", "C")],
        default="a",
        string="Seccion",
        required=True,
    )

    grado = fields.Selection(
        [
            ("kinder", "Kinder"),
            ("primaria", "Primaria"),
            ("secundaria", "Secundaria"),
        ],
        default="1",
        string="Grado",
        required=True,
    )

    # Relacion a alumnos
    alumno_ids = fields.One2many("agenda.cursoalumno", "curso_id", string="Alumnos")

    # relacion mucho a muchos con curso simulada con una tabla en medio
    profesor_ids = fields.One2many(
        "agenda.profesorcurso", "curso_id", string="Profesores"
    )
