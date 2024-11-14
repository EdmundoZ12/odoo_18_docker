# -*- coding: utf-8 -*-

from odoo import models, fields, api


class administrativo(models.Model):
    _name = "agenda.administrativo"
    _description = "administrativo"

    name = fields.Char(string="Nombre", required=True)
    cargo = fields.Char(string="Cargo", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de terminacion")
    estado = fields.Char(string="Estado", compute="_compute_estado", store=False)

    # relacion a usuario
    user_id = fields.Many2one(
        "res.users", string="Usuario del administrativo", required=True
    )

    employee_id = fields.Many2one("hr.employee", string="Empleado", required=True)
    email = fields.Char(string="Email del Usuario", related="user_id.email", store=True)

    # publicaciones visibles al administrativo
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
        record = super(administrativo, self).create(vals)

        # Actualizar el tipo de usuario en res.users
        if record.user_id:
            record.user_id.agenda_tipo_usuario = "administrativo"
            # Asignar el grupo de Administrador
            group_administrador = self.env.ref(
                "agenda.group_agenda_administrativo", raise_if_not_found=False
            )
            if not group_administrador:
                raise ValueError(
                    "El grupo 'Administrativo' no existe o no está correctamente definido."
                )

            if record.user_id:
                record.user_id.sudo().write(
                    {"groups_id": [(4, group_administrador.id)]}
                )
                record.user_id.sudo().action_reset_password()  # Enviar invitación
        return record
