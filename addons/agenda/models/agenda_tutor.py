# -*- coding: utf-8 -*-
from odoo import models, fields, api


class tutor(models.Model):
    _name = "agenda.tutor"
    _description = "Tutor"

    name = fields.Char(string="Nombre del Tutor", required=True)
    telefono = fields.Char(string="Teléfono")
    direccion = fields.Char(string="Dirección")

    # Usuario del tutor
    user_id = fields.Many2one("res.users", string="Usuario del Tutor", required=True)

    # Relación uno-a-muchos con alumnos
    alumno_ids = fields.One2many("agenda.alumno", "tutor_id", string="Alumnos")

    # publicaciones visibles al tutor
    publicaciones_visibles = fields.Many2many(
        "agenda.publicacion", string="Publicaciones visibles"
    )

    @api.model
    def create(self, vals):
        record = super(tutor, self).create(vals)
        # Actualizar el tipo de usuario en res.users
        if record.user_id:
            record.user_id.agenda_tipo_usuario = "tutor"
            # Asignar el grupo de Tutor
        group_tutor = self.env.ref(
            "agenda.group_agenda_tutor", raise_if_not_found=False
        )
        if not group_tutor:
            raise ValueError(
                "El grupo 'Tutor' no existe o no está correctamente definido."
            )

        if record.user_id:
            record.user_id.sudo().write({"groups_id": [(4, group_tutor.id)]})
            record.user_id.sudo().action_reset_password()  # Enviar invitación
        return record
