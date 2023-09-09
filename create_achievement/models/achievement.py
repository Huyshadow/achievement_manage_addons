from odoo import models, fields, api


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Root Model")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    name = fields.Char(string="Name", required=True)
    softCriteria = fields.Integer(string="Soft Criteria", required=True)
    description = fields.Text(string="Description")
    endAt = fields.Datetime()
    startAt = fields.Datetime()
    end_submit_at = fields.Datetime()
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement', required=True)
    manageUnit = fields.Text(default='{}')
    deleteAt = fields.Datetime()
    _sql_constraints = [
        ('achievement_pk', 'PRIMARY KEY (id)', 'Achievement ID must be unique.'),
    ]
