# JUST TEST FILE IGNORE WHEN REVIEW (DELETE ON DEPLOY)

from odoo import models, fields, api

class User(models.Model):
    _inherit = 'ir.ui.menu'
    
    @api.model
    def get_first_groupname(self):
        if groups_id:
            first_group = groups_id[0]
            return first_group.name
        return False
        
