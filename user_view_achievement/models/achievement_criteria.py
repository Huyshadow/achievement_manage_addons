from odoo import models, fields, api
from pytz import timezone
from datetime import datetime, time, timedelta


class AchivementCriteria(models.Model):
    _inherit = 'create_achievement.criteria'

    submit_ids = fields.One2many(
        'achievement.submit', 'criteria', 'Bản nộp')
    is_submitted = fields.Boolean(
        'Xác nhận nộp', compute='_compute_is_submitted')
    status = fields.Char(
        string="Tình Trạng", compute='_compute_status')

    @api.onchange('is_submitted')
    def _compute_status(self):
        for record in self:
            if record.is_submitted == True:
                record.status = "Đã nộp"
            else:
                record.status = "Chưa nộp"

    @api.depends('submit_ids')
    def _compute_is_submitted(self):
        for record in self:
            record.is_submitted = record.submit_ids.filtered(
                lambda s: s.user_id == self.env.user and s.submit == True)[:1] or False

    def action_submit_criteria(self):
        self.ensure_one()
        form_id = self.env.ref(
            'user_view_achievement.achievement_submit_view_form').id
        action = {
            'name': 'Nộp chỉ tiêu',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
        }
        current_submission = self.submit_ids.filtered(
            lambda s: s.user_id == self.env.user)[:1]
        if current_submission:
            action.update({
                'res_id': current_submission.id,
            })
        else:
            self.add_user_list()
            new_submission = self.env['achievement.submit'].search([
                ('criteria','=', self.id),
                ('user_id.id','=', self.env.uid)
            ])
            action.update({
                'res_id': new_submission.id,
            })
        return action

    def add_user_list(self):
        for record in self:
            user_id = self.env.user
            achievement_id = record.achievement_id

            tz = timezone('Asia/Bangkok')
            current_local_time = datetime.now(tz) - timedelta(hours=7)
            string_time = current_local_time.strftime('%Y-%m-%d %H:%M:%S')
            submit_at = string_time

            # Check if a corresponding record already exists, and if not, create it
            existing_achievement_user = self.env['achievement.user.list'].search([
                ('user_id.id', '=', user_id.id),
                ('achievement_id.id', '=', achievement_id),
            ])

            if not existing_achievement_user:
                user = self.env['achievement.user.list'].create({
                    'achievement_id': achievement_id,
                    'donvi_id': user_id.donvi.id,
                    'submit_at': submit_at,
                })
                criteria_list = self.env['create_achievement.criteria'].search([
                    ('achievement_id', '=', achievement_id),
                ])
                for criteria in criteria_list:
                    exist = self.env['achievement.submit'].search([
                        ('criteria_id', '=', criteria.id),
                        ('user_id.id', '=', user_id.id),
                    ])
                    if not exist:
                        self.env['achievement.submit'].create({
                            'criteria': criteria.id,
                            'submit_content': "Chưa điền",
                            'submit': False,
                            'parent_id': user.id
                        })
            else:
                existing_achievement_user.write({'submit_at': submit_at})
