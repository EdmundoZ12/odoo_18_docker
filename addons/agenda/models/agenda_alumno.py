# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class alumno(models.Model):
    _name = "agenda.alumno"
    _description = "Alumno"

    name = fields.Char(string="Nombre del Alumno", required=True)
    user_id = fields.Many2one("res.users", string="Usuario del Alumno", required=True)
    email = fields.Char(string="Email del Usuario", related="user_id.email", store=True)

    # curso actual computado
    curso_actual = fields.Char(
        string="Curso Actual", compute="_compute_curso_actual", store=True
    )

    # Relación muchos-a-uno con tutor
    tutor_id = fields.Many2one("agenda.tutor", string="Tutor", required=True)

    # mucho a muchos
    curso_ids = fields.One2many("agenda.cursoalumno", "alumno_id", string="Cursos")

    # publicaciones visibles al alumno
    publicaciones_visibles = fields.Many2many(
        "agenda.publicacion", string="Publicaciones visibles"
    )

    @api.depends("curso_ids")
    def _compute_curso_actual(self):
        current_year = datetime.now().year
        for alumno in self:
            # Filtrar curso en el año actual y asignar el nombre del curso
            cursos_actuales = alumno.curso_ids.filtered(
                lambda c: c.gestion.year == current_year
            )
            alumno.curso_actual = (
                cursos_actuales[0].curso_id.name if cursos_actuales else "Sin curso"
            )

    @api.model
    def create(self, vals):
        record = super(alumno, self).create(vals)
        # Actualizar el tipo de usuario en res.users
        if record.user_id:
            record.user_id.agenda_tipo_usuario = "alumno"
            # Asignar el grupo de record
            group_record = self.env.ref(
                "agenda.group_agenda_alumno", raise_if_not_found=False
            )
            if not group_record:
                raise ValueError(
                    "El grupo 'Alumno' no existe o no está correctamente definido."
                )

            if record.user_id:
                record.user_id.sudo().write({"groups_id": [(4, group_record.id)]})
                record.user_id.sudo().action_reset_password()  # Enviar invitación
        return record
