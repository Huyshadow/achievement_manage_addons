from odoo import models, fields, api
from datetime import datetime, timedelta


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Root Model")

    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'parent_id', string="Achivement's Criteria")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    name = fields.Char(default="", required=True, string="Achievement's Title")
    soft_criteria = fields.Integer(string="Soft Criteria")
    description = fields.Text(string="Description")
    end_at = fields.Datetime(string="End time")
    start_at = fields.Datetime(string="Start time")
    end_submit_at = fields.Datetime()
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
    last_updated = fields.Datetime()
    status = fields.Char(
        string="Status", compute='_compute_status', store=True)

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
                    record.status = "Incoming"
                if (record.last_updated >= record.start_at and record.last_update <= record.end_at):
                    record.status = "In Progress"
                if (record.last_updated > record.end_at):
                    record.status = "Done"
