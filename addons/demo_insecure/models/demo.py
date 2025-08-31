from odoo import models, fields, api

class DemoInsecure(models.Model):
    _name = 'demo.insecure'
    _description = 'Demo Insecure Model'

    name = fields.Char(string='Name')
    secret = fields.Char(string='Secret')

    @api.model
    def find_secret(self, user_input):
        # Vulnerabilidad: SQL Injection
        query = f"SELECT secret FROM demo_insecure WHERE name = '{user_input}'"
        self.env.cr.execute(query)
        result = self.env.cr.fetchone()
        return result[0] if result else None