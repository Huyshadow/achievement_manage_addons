from odoo import models, fields, api
from pytz import timezone
from datetime import datetime, time, timedelta


class AchievementSubmit(models.Model):
    _inherit = 'achievement.user.list'

    status_user = fields.Selection([
        ('Đã đạt (A)', 'Đã đạt (A)'),
        ('Cần bổ sung (B)', 'Cần bổ sung (B)'),
        ('Không đạt (C)', 'Không đạt (C)')
    ], string="Kết quả thẩm định")
    note_user = fields.Text(string="Nhận xét tổng")
    temp_note = fields.Text(
        string="Ghi chú", compute='_compute_temp_note', store=True)
    last_expertise_at = fields.Datetime(
        string="Thời gian thẩm định cuối", compute='_compute_last_expertise', store=True)
    last_expertise_committe = fields.Char(string="Tên người thẩm định cuối")

    @api.depends('submit_list.expertise', 'submit_list.depart_manage_comment')
    def _compute_temp_note(self):
        for record in self:
            khongdat = "Không đạt:"
            canbosung = "Cần bổ sung:"
            have_type_bosung = False
            have_type_khongdat = False
            record.temp_note = ""
            for submit in record.submit_list:
                print(submit.expertise)
                if submit.expertise == 'need_evidence':
                    if submit.depart_manage_comment:
                        have_type_bosung = True
                        canbosung = canbosung + '\n' + "+ " + submit.criteria_content + \
                            " (" + submit.depart_manage_comment + ")"
                if submit.expertise == 'not_passed':
                    if submit.depart_manage_comment:
                        have_type_khongdat = True
                        khongdat = khongdat + '\n' + "+ " + submit.criteria_content + \
                            " (" + submit.depart_manage_comment + ")"
            if have_type_bosung:
                record.temp_note = canbosung + '\n'
            if have_type_khongdat:
                record.temp_note += khongdat + '\n'
            record.note_user = record.temp_note
            # if difference:
            #     record.note_user += difference
            record.note_user = record.note_user.rstrip('\n')

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

    def popup(self):
        appraise_status = self.appraise_status
        if appraise_status == 'end':
            text = """Đã hết thời gian thẩm định"""
        else:
            text = """Chưa tới thời gian thẩm định"""
        query = 'delete from display_dialog_box'
        self.env.cr.execute(query)
        value = self.env['display.dialog.box'].sudo().create({'text': text})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Thông báo',
            'res_model': 'display.dialog.box',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_id': value.id
        }

    @api.depends('submit_list.expertise', 'submit_list.depart_manage_comment', 'status_user')
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
            appraise_status = self.appraise_status
            if record.status_user != False:
                name = record.status_user
            else:
                name = "Thẩm định"
            if appraise_status == 'active':
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
                                    'action': "popup",
                                    'name': name,
                                    'model': 'achievement.user.list'
                                }]},
                }

    def custom_button(self):
        return

    def delete_trash_data(self):
        submit_list = self.env['achievement.user.list'].search([])
        for submit in submit_list:
            submit.write({
                'last_expertise_at': None,
                'last_expertise_committe': None,
                'temp_note': None,
                'note_user': None,
            })

    @api.depends('status_user')
    def action_view_user_submit_appraiser_B_type(self):
        for record in self:
            appraise_status = self.appraise_status
            if record.status_user != False:
                name = record.status_user
            else:
                name = "Thẩm định"
            if appraise_status == 'active':
                return {
                    'name': self.user_name,
                    'type': 'ir.actions.act_window',
                    'view_mode': 'tree',
                    'view_id': self.env.ref('appraise_submit.view_user_submit_detail_appraise_open').id,
                    'res_model': 'achievement.submit',
                    'target': 'current',
                    'flags': {'hasSelectors': False},
                    'domain': [('criteria.parent_id.parent_id.parent_id.id', '=', self.achievement_id.id), ('user_id', '=', self.user_id.id), ('expertise', '=', 'need_evidence')],
                    'context': {'search_default_display_group_name': True, 'search_default_type_criteria_name': True,
                                'appraise_buttons': [{
                                    'action': "appraise",
                                    'name': name,
                                    'model': 'achievement.user.list'
                                }]},
                }
            else:
                appraise_status = self.appraise_status
                if appraise_status == 'end':
                    text = """Đã hết thời chấm bổ sung"""
                else:
                    text = """Chưa tới thời gian chấm bổ sung"""
                query = 'delete from display_dialog_box'
                self.env.cr.execute(query)
                value = self.env['display.dialog.box'].sudo().create({
                    'text': text})
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'Thông báo',
                    'res_model': 'display.dialog.box',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'target': 'new',
                    'res_id': value.id
                }
