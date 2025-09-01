from odoo import models, fields

class DemoInsecure(models.Model):
    _name = 'demo.insecure'
    _description = 'Demo Insecure Model'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    api_key = fields.Char(string='API Key')
