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
            # 'res_id': self.user_id.id,
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id)],
            'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True,
                        'discard_buttons': [{
                            'action': "huy_duyet",
                            'name': "Hủy",
                            'model': 'achievement.submit'
                        }],
                        'general_buttons': [{
                            'action': "duyet",
                            'name': "Duyệt",
                            'model': 'achievement.submit'
                        },
                        ],
                        },

        }

    # def action_accept_submit(self):
    #     for record in self:
    #         record.env['achievement.user.list'].write({
    #             'result': True
    #         })
