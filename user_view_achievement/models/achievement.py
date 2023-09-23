from odoo import models, fields, api

class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    def action_view_detail_achievement(self):
        return {
            'name': 'Thông tin danh hieu',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('user_view_achievement.view_achievement_detail').id,
            'res_model': 'create_achievement.criteria',
            'res_id': self.id,
            'target': 'current',
            'context': {'search_default_group_criteria': True, 'search_default_category': True},
        }