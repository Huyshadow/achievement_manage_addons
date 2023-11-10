from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    def action_view_user_list_appraiser(self):
        appraiser = self.env['create_achievement.appraise'].search([
            ('user_id', '=', self.env.uid),
            ('achievement_id', '=', self.id),
        ])
        depart_name_list = appraiser.donvis_names.split(',')
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('appraise_submit.view_achievement_user_list_appraise').id,
            'res_model': 'achievement.user.list',
            'target': 'current',
            'domain': [('achievement_id', '=', self.id), ('donvi_code', 'in', depart_name_list), ('user_approve', '=', True)],
        }

    def action_view_appraiser_add_more(self):
        appraiser = self.env['create_achievement.appraise'].search([
            ('user_id', '=', self.env.uid),
            ('achievement_id', '=', self.id),
        ])
        depart_name_list = appraiser.donvis_names.split(',')
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('appraise_submit.inherit_view_achievement_appraiser_more').id,
            'res_model': 'achievement.user.list',
            'target': 'current',
            'domain': [('achievement_id', '=', self.id), ('donvi_code', 'in', depart_name_list), ('user_approve', '=', True), ('submit_at', '>', self.end_at)],
        }
