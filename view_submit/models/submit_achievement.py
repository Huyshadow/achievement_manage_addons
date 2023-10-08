from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    def action_view_user_list(self):
        return {
        'name': self.name,
        'type': 'ir.actions.act_window',
        'view_mode': 'tree',
        'view_id': self.env.ref('view_submit.view_achievement_user_list').id,
        'res_model': 'achievement.user.list',
        'res_id': self.id,
        'target': 'current',
        'flags': {'hasSelectors': False},
        'domain': [('achievement_id', '=', self.id)],
    }
