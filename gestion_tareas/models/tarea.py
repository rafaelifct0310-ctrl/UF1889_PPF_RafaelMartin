from odoo import models, fields

class Tarea(models.Model):
    _name = "gestion.tarea"
    _descripcion = "Tarea realizada sobre cliente"
    _order = "fecha desc, id desc"

    nombre = fields.Char(
        string_name="Nombre de la tarea",
        required=True
    )

    cliente_id = fields.Many2one(
        cmodel_name="res.partner",
        string="Cliente",
        required=True
    )

    fecha = fields.Date(
        string="Fecha",
        default=fields.Date.context_today,
        required=True
    )

    estado = fields.Selection(
        selection = [
            ("pendiente", "Pendiente"),
            ("finalizada", "Finalizada"),
        ],
        string = "Estado",
        default = "pendiente",
        required = True
    )

    def action_marcar_finalizada(self):
        for tarea in self:
            tarea.estado = "finalizada"

    def obtener_tareas_por_clientes(self, cliente_id):
        return self.search([
            ("cliente_id", "=", cliente_id)
        ])

    def obtener_tareas_pendientes(self):
        return self.search([
            ("estado", "=", "pendiente")
        ])
