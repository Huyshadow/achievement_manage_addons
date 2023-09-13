from odoo import models, fields, api

class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'
    
    def action_view_detail_achievement(self):
        action = self.env['ir.actions.actions'].with_context(active_id=self.id)._for_xml_id('user_view_achievement.action_view_detail_achievement')
        return action

    def get_name(self):
        return {
            'name': self.name,
            'status': self.status,
        }


