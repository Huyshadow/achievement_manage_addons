from odoo import models, fields, api
from pytz import timezone
from datetime import datetime, time, timedelta

class AchievementSubmit(models.Model):
    _inherit = 'achievement.user.list'
    last_expertise_at = fields.Datetime(string="Thời gian thẩm định cuối", compute = '_compute_last_expertise', store = True)
    last_expertise_committe = fields.Char(string="Tên người thẩm định cuối")
    final_expertise = fields.Selection([
        ('passed', 'Đã đạt(A)'),
        ('need_evidence', 'Thiếu minh chứng(B)'),
        ('not_passed', 'Không đạt(C)'),
        ('not_expertise','Chưa thẩm định')
    ], string="Kết quả thẩm định", default='not_expertise')
    final_review = fields.Text(string="Nhận xét tổng")

    @api.depends('submit_list.expertise','submit_list.depart_manage_comment')
    def _compute_last_expertise(self):
        for record in self:
            tz = timezone('Asia/Bangkok')
            current_local_time = datetime.now(tz) - timedelta(hours=7)
            utc = current_local_time.strftime('%Y-%m-%d %H:%M:%S')
            record.last_expertise_at = utc
            record.last_expertise_committe = self.env.user.name
    
    def action_view_user_submit_appraiser(self):
        approve_status = self.achievement_id.open_approve
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
                            'general_buttons': [{
                                'action': "duyet",
                                'name': "Thẩm định",
                                'model': 'achievement.submit'
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
                            'general_buttons': [{
                                'action': "duyet",
                                'name': "Thẩm định toàn bộ hồ sơ",
                                'model': 'achievement.submit'
                            }]},
            }
