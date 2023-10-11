from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time, timedelta
from pytz import timezone


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    criteria_ids = fields.One2many(
        'create_achievement.group_criterias', 'parent_id', string="Tập tiêu chí danh hiệu")

    name = fields.Char(default="", required=True, string="Danh hiệu")
    description = fields.Text(string="Mô tả")
    start_at = fields.Datetime(string="Ngày bắt đầu nộp", required=True)
    end_submit_at = fields.Datetime(
        string="Ngày kết thúc nộp", required=True)
    end_at = fields.Datetime(
        string="Ngày kết thúc duyệt", required=True)
    delete_at = fields.Datetime()
    last_updated = fields.Datetime(
        default=fields.Datetime.now())
    status = fields.Char(
        string="Tình Trạng", compute='_compute_status', store=True)

    name_title = fields.Char(default="Danh hiệu mới", compute="_change_title")
    computed_numbers = fields.Integer(
        'Function for sort', compute='_compute_numbers', store=True)

    @api.depends('criteria_ids')
    def _compute_numbers(self):
        for record in self:
            number = 1  # Initialize the number to start from 1
            for group_criteria in record.criteria_ids:
                group_criteria.display_name = str(
                    number) + '. ' + group_criteria.name
                number += 1

    @api.depends('name')
    def _change_title(self):
        for record in self:
            record.name_title = "Danh hiệu - " + record.name

    @api.depends('last_updated', 'status')
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
            future_date = record.create_date + timedelta(days=0)
            default_time = time(hour=0, minute=0, second=0)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            check_time = utc_datetime.replace(tzinfo=None)
            if record.start_at < check_time:
                raise ValidationError(
                    "Thời gian bắt đầu phải kể từ ngày khi được tạo")

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
            future_date = current_date + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_submit_at'] = utc_datetime.replace(tzinfo=None)
        if 'end_at' in fields and 'end_at' not in defaults:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = datetime.now(tz).date()
            future_date = current_date + timedelta(days=2)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(future_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            defaults['end_at'] = utc_datetime.replace(tzinfo=None)
        return defaults

    @api.onchange('end_submit_at')
    def set_time_end_submit_at(self):
        for record in self:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = record.end_submit_at + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(current_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            print(utc_datetime)
            print(utc_datetime.replace(tzinfo=None))
            record.end_submit_at = utc_datetime.replace(tzinfo=None)

    @api.onchange('end_at')
    def set_time_end_at(self):
        for record in self:
            tz = timezone('Asia/Bangkok')  # Set the desired timezone
            current_date = record.end_at + timedelta(days=1)
            default_time = time(hour=23, minute=59, second=59)
            naive_datetime = datetime.combine(current_date, default_time)
            local_datetime = tz.localize(naive_datetime)
            utc_datetime = local_datetime.astimezone(timezone('UTC'))
            record.end_at = utc_datetime.replace(tzinfo=None)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        records = super(Achievement, self).search_read(
            domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        access_time = datetime.now()
        for record in records:
            self.browse(record['id']).write({'last_updated': access_time})
        return records

    def save_and_redirect(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'create_achievement.BackClientAction',
        }
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Danh sách danh hiệu',
        #     'res_model': 'create_achievement.achievement',
        #     'view_type': 'form,tree',
        #     'view_mode': 'tree',
        #     'target': 'current',
        #     'context': {
        #         'create': True
        #     }
        # }

        # text = """Lưu danh hiệu thành công"""
        # query = 'delete from display_dialog_box'
        # self.env.cr.execute(query)
        # value = self.env['display.dialog.box'].sudo().create({'text': text})
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Thông báo',
        #     'res_model': 'display.dialog.box',
        #     'view_type': 'form',
        #     'view_mode': 'form',
        #     'target': 'new',
        #     'res_id': value.id
        # }
