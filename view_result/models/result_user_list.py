from odoo import models, fields, api
from pytz import timezone
from datetime import datetime, time, timedelta


class ResultUserList(models.Model):
    _inherit = 'achievement.user.list'

    def user_detail_result_view(self):
        return {
            'name': self.user_name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('view_result.view_user_submit_detail_view_result').id,
            'res_model': 'achievement.submit',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id)],
            'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True},
        }
