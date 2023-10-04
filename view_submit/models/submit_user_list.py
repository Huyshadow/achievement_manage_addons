from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementSubmit(models.Model):
    _inherit = 'achievement.user.list'


    def action_view_user_submit(self):
        return {
        'name': self.user_name,
        'type': 'ir.actions.act_window',
        'view_mode': 'tree',
        'view_id': self.env.ref('view_submit.view_user_submit_detail').id,
        'res_model': 'achievement.submit',
        'res_id': self.user_id,
        'target': 'current',
        'flags': {'hasSelectors': False},
        'domain': [('achievement_id', '=', self.achievement_id),('user_id','=',self.user_id)],
    }
    def action_accept_submit(self):
        for record in self:
            record.env['achievement.user.list'].write({
                'result': True
            })
        