

from odoo import models, fields, api

class prueba(models.Model):


    _name = 'odoo_basico.prueba'
    _description = 'modelo para probar o funcionamento de Odoo'

    name = fields.Char(required=True, size=20, string="Identificador de Prueba")
    description = fields.Text(string="A descripción da Prueba")

    descripcionPrueba = fields.Text(string="A descripción da Linea")
    pesoPrueba = fields.Float(string="Peso en Kgs:", digits=(6, 2), default=2.7)

    informacion_prueba_ids = fields.Many2many("odoo_basico.informacion",
                                       string="Rexistro de Información",
                                       relation="odoo_basico_prueba_informacion",
                                       column1="prueba_id", column2="informacion_prueba_id")

    def creaRexistroInformacionPrueba(self):
        creado_id = self.env['odoo_basico.informacion'].create({'name': 'Creado dende prueba'})
        creado_id.descripcion = "Creado dende o modelo pedido"
        creado_id.autorizado = False

