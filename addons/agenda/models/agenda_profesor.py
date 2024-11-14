# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = "agenda.profesor"
    _description = "profesor"

    name = fields.Char(string="Nombre", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de terminacion")
    estado = fields.Char(string="Estado", compute="_compute_estado", store=False)

    # relacion a usuario
    user_id = fields.Many2one("res.users", string="Usuario del Profesor", required=True)
    employee_id = fields.Many2one("hr.employee", string="Empleado", required=True)
    email = fields.Char(string="Email del Usuario", related="user_id.email", store=True)

    # relacion mucho a muchos con curso simulada con una tabla en medio
    curso_ids = fields.One2many("agenda.profesorcurso", "profesor_id", string="Cursos")

    # publicaciones visibles al profesor
    publicaciones_visibles = fields.Many2many(
        "agenda.publicacion", string="Publicaciones visibles"
    )

    @api.depends("fecha_fin")
    def _compute_estado(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_fin and record.fecha_fin <= today:
                record.estado = "Terminado"
            else:
                record.estado = "Activo"

    @api.model
    def create(self, vals):
        record = super(profesor, self).create(vals)
        # Actualizar el tipo de usuario en res.users
        if record.user_id:
            record.user_id.agenda_tipo_usuario = "profesor"
            # Asignar el grupo de Profesor al usuario si existe
        group_profesor = self.env.ref(
            "agenda.group_agenda_profesor", raise_if_not_found=False
        )
        if not group_profesor:
            raise ValueError(
                "El grupo 'Profesor' no existe o no está correctamente definido."
            )

        if record.user_id:
            record.user_id.sudo().write({"groups_id": [(4, group_profesor.id)]})
            record.user_id.sudo().action_reset_password()
        return record
