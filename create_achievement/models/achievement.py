from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Root Model")

    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'parent_id', string="Tiêu chí danh hiệu")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    name = fields.Char(default="", required=True, string="Danh hiệu")
    soft_criteria = fields.Integer(string="Soft Criteria")
    description = fields.Text(string="Mô tả")
    end_at = fields.Datetime(string="Ngày kết thúc nộp", required=True)
    start_at = fields.Datetime(string="Ngày bắt đầu nộp", required=True)
    end_submit_at = fields.Datetime(
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

    def link_to_criteria(self):
        return {
            'name': "Danh sách tiêu chí",
            'res_model': 'create_achievement.criteria',
            'type': 'ir.actions.act_window',
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'target': 'self',
            'context': {
                'create': True,
            },
        }

    def update_last_updated_field(self):
        records = self.search([])
        current_datetime = fields.Datetime.now()
        records.write({'last_updated': current_datetime})
        print(records)

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

    @api.constrains('start_at', 'end_at', 'end_submit_at')
    def _check_fields(self):
        for record in self:
            if record.start_at >= record.end_at:
                raise ValidationError(
                    "Thời gian kết thúc nộp phải sau thời gian bắt đầu nộp")
            if record.start_at >= record.end_submit_at or record.end_at <= record.end_submit_at:
                raise ValidationError(
                    "Thời gian kết thúc duyệt phải nằm trong khoảng thời gian bắt đầu và kết thúc của danh hiệu"
                )
