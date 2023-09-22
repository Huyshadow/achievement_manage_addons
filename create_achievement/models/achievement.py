from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time, timedelta
from pytz import timezone


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    criteria_ids = fields.One2many(
        'create_achievement.group_criterias', 'parent_id', string="Tiêu chí danh hiệu")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    name = fields.Char(default="", required=True, string="Danh hiệu")
    soft_criteria = fields.Integer(string="Soft Criteria")
    description = fields.Text(string="Mô tả")
    start_at = fields.Datetime(string="Ngày bắt đầu nộp", required=True)
    end_submit_at = fields.Datetime(
        string="Ngày kết thúc nộp", required=True)
    end_at = fields.Datetime(
        string="Ngày kết thúc duyệt", required=True)
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement', required=True)
    manage_unit = fields.Text(default='{}')
    delete_at = fields.Datetime()
    last_updated = fields.Datetime(default=fields.Datetime.now)
    status = fields.Char(
        string="Tình Trạng", compute='_compute_status', store=True)

    name_title = fields.Char(default="Danh hiệu mới", compute="_change_title")

    @api.depends('name')
    def _change_title(self):
        for record in self:
            record.name_title = "Danh hiệu - " + record.name

    def link_to_criteria(self):
        action = self.env.ref(
            "create_achievement.action_cr_group_criteria").sudo().read()[0]
        action.update({
            'name': "Danh sách tiêu chí",
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('parent_id', '=', self.id)],
            'context': {
                'create': True,
                'default_parent_id': self.id,
            },
        })
        return action

    # @api.constains('start_at')
    # def add_start_at(self):
    #     for record in self:

    @api.depends('last_updated')
    def _compute_status(self):
        for record in self:
            if record.end_at and record.start_at:
                if (record.last_updated < record.start_at):
                    record.status = "Trạng thái chờ"
                if (record.last_updated >= record.start_at and record.last_updated <= record.end_at):
                    record.status = "Đang tiến hành"
                if (record.last_updated > record.end_at):
                    record.status = "Đã kết thúc"

    @api.constrains('start_at')
    def _check_start_time(self):
        for record in self:
            tz = timezone('Asia/Bangkok')
            future_date = record.create_date + timedelta(days=1)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            check_time = utc_datetime.replace(tzinfo=None)
            print(check_time)
            if record.start_at < check_time:
                raise ValidationError(
                    "Thời gian bắt đầu phải hơn 1 ngày kể từ khi được tạo")

    @api.constrains('start_at', 'end_at', 'end_submit_at')
    def _check_fields(self):
        for record in self:
            if record.start_at >= record.end_at:
                raise ValidationError(
                    "Thời gian kết thúc duyệt phải sau thời gian bắt đầu nộp")
            if record.start_at >= record.end_submit_at or record.end_submit_at >= record.end_at:
                raise ValidationError(
                    "Thời gian kết thúc nộp phải nằm trong khoảng thời gian bắt đầu và kết thúc duyệt của danh hiệu"
                )

    @api.model
    def default_get(self, fields):
        defaults = super(Achievement, self).default_get(fields)
        if 'start_at' in fields and 'start_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=1)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['start_at'] = utc_datetime.replace(tzinfo=None)
        if 'end_submit_at' in fields and 'end_submit_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=2)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_submit_at'] = utc_datetime.replace(tzinfo=None)
        if 'end_at' in fields and 'end_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=3)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_at'] = utc_datetime.replace(tzinfo=None)
        return defaults

    # @api.model
    # def get_user_last_login(self, user_id):
    #     user = self.env['res.users'].browse(user_id)
    #     last_login = user.last_login
    #     records = self.search([])
    #     records.write({'last_updated': last_login})
