from odoo import models, fields, api
from odoo.exceptions import ValidationError
from pytz import timezone
from datetime import datetime, time, timedelta
import os


class AchievementSubmit(models.Model):
    _name = 'achievement.submit'
    _description = 'Achievement Submit'

    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    criteria = fields.Many2one('create_achievement.criteria', 'Tieu chi')
    criteria_id = fields.Integer('ID tiêu chí', related='criteria.id')
    criteria_name = fields.Char('Tên tiêu chí', related='criteria.name')
    criteria_content = fields.Char('Mô tả', related='criteria.content')
    criteria_method = fields.Selection(
        'Phương thức', related='criteria.method', related_sudo=False)
    required_evidence = fields.Boolean(
        'Cần minh chứng', related='criteria.evidence')
    group_criteria_name = fields.Char(
        'Tên tập tiêu chí', related='criteria.parent_id.parent_id.name')
    type_criteria_name = fields.Char(
        'Tên loại tiêu chí', related='criteria.parent_id.name')
    expertise = fields.Selection([
        ('passed', 'Đã đạt'),
        ('not_passed', 'Chưa đạt'),
        ('need_evidence', 'Thiếu minh chứng')
    ], default='')
    depart_manage_comment = fields.Char('Nhận xét của quản lý đơn vị')

    grade = fields.Integer('Điểm')
    is_passed = fields.Boolean('Đã đạt')
    comment = fields.Text(string='Tự nhận xét')
    evidence = fields.Binary(string='Minh Chứng(file .pdf)')
    pdf_name = fields.Char(string='Tên file pdf')
    submit = fields.Boolean('Đã nộp', compute="_check_submit", store=True)
    submit_content = fields.Char(string='Nội dung nộp')

    related_list_string = fields.Char(
        related='criteria_id.value_list_string', related_sudo=False)
    list_selection = fields.Selection(
        '_compute_field_selection', string="Danh sách")

    def _get_selection(self):
        print('Huy')
        print(self.criteria_name)
        for record in self:
            print(self)
        return []

    list_selection = fields.Selection(_get_selection, string="Danh sách")

    @api.depends('grade', 'is_passed', 'comment')
    def _check_submit(self):
        for record in self:
            if record.criteria_method == "thangdiem":
                if record.grade:
                    record.submit = True
                    record.add_user_list()
                    record.submit_content = str(record.grade)
            elif record.criteria_method == "nhiphan":
                if record.is_passed == True:
                    record.submit = True
                    record.add_user_list()
                    record.submit_content = "Đã đạt"
            elif record.criteria_method == "nhanxet":
                if record.comment:
                    record.submit = True
                    record.add_user_list()
                    record.submit_content = record.comment
            else:
                record.submit = False
                record.submit_content = "Chưa điền"

    @api.constrains('evidence')
    def _check_file(self):
        if os.path.splitext(str(self.pdf_name))[1] != '.pdf':
            raise ValidationError("Chỉ nhận file PDF")

    def add_user_list(self):
        for record in self:
            user_id = record.user_id.id
            achievement_id = record.criteria.achievement_id

            tz = timezone('Asia/Bangkok')
            future_date = record.create_date + timedelta(days=0)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            check_time = utc_datetime.replace(tzinfo=None)

            submit_at = check_time

            # Check if a corresponding record already exists, and if not, create it
            existing_achievement_user = self.env['achievement.user.list'].search([
                ('user_id', '=', user_id),
                ('achievement_id', '=', achievement_id),
            ])

            if not existing_achievement_user:
                self.env['achievement.user.list'].create({
                    'user_id': user_id,
                    'user_name': record.user_id.name,
                    'achievement_name': record.criteria.parent_id.parent_id.parent_id.name,
                    'achievement_id': achievement_id,
                    'donvi_name': record.user_id.donvi.name,
                    'submit_at': submit_at
                })
            else:
                existing_achievement_user.write({'submit_at': submit_at})
