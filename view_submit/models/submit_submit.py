from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementSubmit(models.Model):
    _inherit = 'achievement.submit'
    


    def action_expertise_submit(self):
        self.ensure_one()
        form_id = self.env.ref(
            'view_submit.comment_on_user_submit').id
        action = {
            'name': 'Thẩm định tiêu chí',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
            'res_id': self.id,
        }
        return action
