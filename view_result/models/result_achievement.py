from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Result_Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    def action_view_user_list_result_depart(self):
        unit_manage = self.env['res.users'].search([
            ('id', '=', self.env.uid),
        ])
        depart_unit = unit_manage.donvi.code
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('view_result.view_achievement_user_list_result').id,
            'res_model': 'achievement.user.list',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('achievement_id', '=', self.id), ('donvi_code', '=', depart_unit), ('user_approve', '=', True)],
        }
