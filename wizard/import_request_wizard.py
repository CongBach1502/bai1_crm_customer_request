from odoo import models, fields

class ImportRequestWizard(models.TransientModel):
    _name = 'import.request.wizard'

    lead_id = fields.Many2one('crm.lead')
    file = fields.Binary(required=True)
    file_name = fields.Char()

    def action_import(self):
        pass