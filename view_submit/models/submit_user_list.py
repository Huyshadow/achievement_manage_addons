from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementSubmit(models.Model):
    _inherit = 'achievement.user.list'

    edit_right = fields.Boolean(compute='_compute_edit_right')

    @api.depends('status_user')
    def _compute_edit_right(self):
        for record in self:
            if record.status_user =="Đã đạt (A)" or record.status_user =="Cần bổ sung (B)" :
                record.edit_right = True
            else:
                record.edit_right = False


    def action_view_detail_achievement(self):
        if self.env.user.is_fill_info == False:
            raise ValidationError(
                    "Vui lòng cập nhập thông tin trước khi nộp hồ sơ")
        else:
            return {
            'name': self.achievement_id.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('user_view_achievement.view_achievement_detail_user').id,
            'res_model': 'create_achievement.criteria',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('achievement_id', '=', self.achievement_id.id)],
            'context': {'search_default_group_criteria': True, 'search_default_category': True},
        }

    def action_view_detail_bosung(self):
        if self.env.user.is_fill_info == False:
            raise ValidationError(
                    "Vui lòng cập nhập thông tin trước khi nộp hồ sơ")
        else:
            return {
            'name': self.user_name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('appraise_submit.view_achievement_detail_nop_bo_sung').id,
            'res_model': 'achievement.submit',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id), ('expertise','=', 'need_evidence')],
            'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True},
        }
        
    @api.depends('user_approve')
    def action_view_user_submit(self):
        context = {'search_default_display_group_name': True,
                   'search_default_type_criteria_name': True, }
        for record in self:
            if record.appraise_status == "pending":
                if record.user_approve == False:
                    context['general_buttons'] = [{
                        'action': "duyet_huy",
                        'name': "Duyệt",
                        'model': 'achievement.submit'
                    },
                    ]
                else:
                    context['discard_buttons'] = [{
                        'action': "duyet_huy",
                        'name': "Hủy",
                        'model': 'achievement.submit'
                    }]
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
                'context': context,
            }
