from odoo import models, fields, api
from pytz import timezone
from datetime import datetime, time, timedelta


class AchievementSubmit(models.Model):
    _inherit = 'achievement.user.list'

    status_user = fields.Selection([
        ('Đã đạt(A)', 'Đã đạt(A)'), 
        ('Thiếu minh chứng(B)', 'Thiếu minh chứng(B)'), 
        ('Không đạt(C)', 'Không đạt(C)')
    ], string="Kết quả thẩm định")
    note_user = fields.Text(string="Nhận xét tổng")
    last_expertise_at = fields.Datetime(
        string="Thời gian thẩm định cuối", compute='_compute_last_expertise', store=True)
    last_expertise_committe = fields.Char(string="Tên người thẩm định cuối")
    def appraise(self):
        return {
            'name': 'Thẩm định tiêu chí',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('appraise_submit.view_achievement_user_list_appraise_form').id,
            'res_model': 'achievement.user.list',
            'target': 'new',
            'res_id': self.id
        }

    @api.depends('submit_list.expertise', 'submit_list.depart_manage_comment','status_user')
    def _compute_last_expertise(self):
        for record in self:
            tz = timezone('Asia/Bangkok')
            current_local_time = datetime.now(tz) - timedelta(hours=7)
            utc = current_local_time.strftime('%Y-%m-%d %H:%M:%S')
            record.last_expertise_at = utc
            record.last_expertise_committe = self.env.user.name

    @api.depends('status_user')
    def action_view_user_submit_appraiser(self):
        for record in self:
            approve_status = self.achievement_id.open_approve
            name = "Thẩm định"
            if record.status_user != False:
                name = record.status_user
            if approve_status:
                return {
                    'name': self.user_name,
                    'type': 'ir.actions.act_window',
                    'view_mode': 'tree',
                    'view_id': self.env.ref('appraise_submit.view_user_submit_detail_appraise_open').id,
                    'res_model': 'achievement.submit',
                    'target': 'current',
                    'flags': {'hasSelectors': False},
                    'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id)],
                    'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True,
                                'appraise_buttons': [{
                                    'action': "appraise",
                                    'name': name,
                                    'model': 'achievement.user.list'
                                }]},
                }
            else:
                return {
                    'name': self.user_name,
                    'type': 'ir.actions.act_window',
                    'view_mode': 'tree',
                    'view_id': self.env.ref('appraise_submit.view_user_submit_detail_appraise_close').id,
                    'res_model': 'achievement.submit',
                    'target': 'current',
                    'flags': {'hasSelectors': False},
                    'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id)],
                    'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True,
                                'appraise_buttons': [{
                                    'action': "appraise",
                                    'name': name,
                                    'model': 'achievement.user.list'
                                }]},
                }

    def custom_button(self):
        return
