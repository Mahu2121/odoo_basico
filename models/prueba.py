

from odoo import models, fields, api

class prueba(models.Model):


    _name = 'odoo_basico.prueba'
    _description = 'modelo para probar o funcionamento de Odoo'

    name = fields.Char(required=True, size=20, string="Identificador de Prueba")
    description = fields.Text(string="A descripción da Prueba")

    def creaRexistroInformacionPrueba(self):
        creado_id = self.env['odoo_basico.informacion'].create({'name': 'Creado dende prueba'})
        creado_id.descripcion = "Creado dende o modelo pedido"
        creado_id.autorizado = False